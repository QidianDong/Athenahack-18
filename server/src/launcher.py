import argparse
import os
import sys
from pathlib import Path

import uvicorn
from celery import Celery
from uvicorn.supervisors import Multiprocess

from core import Server
from routes import router
from utils.config import ServerConfig

config_path = Path(__file__).parent / "config.yml"
config = ServerConfig(config_path)

celery = Celery(
    "template",
    backend=config["redis_uri"],
    broker=config["broker_uri"],
    include=["src.tasks"],
)

app = Server(celery=celery, config=config)
app.include_router(router)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-H",
        "--host",
        default=config["server"]["host"],
        help="The host to bind to. Defaults to value set in config",
    )
    parser.add_argument(
        "-p",
        "--port",
        default=config["server"]["port"],
        help="The port to bind to. Defaults to value set in config",
        type=int,
    )
    parser.add_argument(
        "-nw",
        "--no-workers",
        action="store_true",
        default=False,
        help="Runs no workers",
    )
    parser.add_argument("-w", "--workers", default=os.cpu_count() or 1, type=int)

    args = parser.parse_args(sys.argv[1:])
    use_workers = not args.no_workers
    worker_count = args.workers

    config = uvicorn.Config(
        "launcher:app", port=args.port, host=args.host, access_log=True
    )

    server = uvicorn.Server(config)

    if use_workers:
        config.workers = worker_count
        sock = config.bind_socket()

        runner = Multiprocess(config, target=server.run, sockets=[sock])
    else:
        runner = server

    celery.start()
    runner.run()
