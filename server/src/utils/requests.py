from fastapi import Request

from core import Server


class RouteRequest(Request):
    app: Server
