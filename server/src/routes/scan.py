import uuid

from fastapi import APIRouter
from pydantic import BaseModel

from utils.requests import RouteRequest

router = APIRouter(tags=["scan"])


class ScanRationale(BaseModel):
    reason: str
    confidence: float


@router.get("/scan/text/reason")
async def scan_text_reason(request: RouteRequest, text: str):
    """Returns a possible reason to why the text has been flagged"""
    res = await request.app.send_task("scan.text.reason", text)
    return ScanRationale(reason=res, confidence=0.9)  # will need to adjust later


class ScanRequest(BaseModel):
    text: str


@router.post("/scan/text")
async def scan_text(request: RouteRequest, req: ScanRequest):
    """Scans the text for any inappropriate content"""
    res = await request.app.send_task("scan.text", req.text)
    return res


@router.post("/scan/doc/{id}")
async def scan_doc_via_id(request: RouteRequest, id: uuid.UUID, req: ScanRequest):
    """Scans the document with the given ID"""
    res = await request.app.send_task("scan.doc", id, req.text)
    return res


@router.get("/scan/doc/{id}/reason")
async def scan_doc_id_reason(request: RouteRequest, id: uuid.UUID):
    """Returns a possible reason to why the document has been flagged"""
    res = await request.app.send_task("scan.doc.reason", id)
    return ScanRationale(reason=res, confidence=0.9)
