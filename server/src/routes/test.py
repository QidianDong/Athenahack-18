from fastapi import APIRouter

from utils.requests import RouteRequest

router = APIRouter(tags=["test"])


@router.get("/test/task")
async def test_task(request: RouteRequest, x: int, y: int):
    res = await request.app.send_task("scan.add", x, y)
    return {"result": res}
