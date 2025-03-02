## Broker settings.
broker_url = "amqp://guest:guest@localhost:5672//"

## Using the database to store task state and results.
result_backend = "redis://localhost/0"
imports = ("tasks.scan",)

task_annotations = {"tasks.add": {"rate_limit": "10/s"}}
