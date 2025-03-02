import re
import uuid

from fastapi import APIRouter
from pydantic import BaseModel

from utils.requests import RouteRequest

router = APIRouter(tags=["scan"])


class ScanRationale(BaseModel):
    text: str
    reason: str
    confidence: float


@router.get("/scan/text/reason")
async def scan_text_reason(request: RouteRequest, text: str):
    """Returns a possible reason to why the text has been flagged"""
    res = await request.app.send_task(
        "scan.text.reason", re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)
    )
    return [
        ScanRationale(text=item.text, reason=item.label, confidence=item.score)
        for item in res
    ]


class ScanRequest(BaseModel):
    text: str


@router.post("/scan/text")
async def scan_text(request: RouteRequest, req: ScanRequest):
    """Scans the text for any inappropriate content"""
    res = await request.app.send_task(
        "scan.text", re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", req.text)
    )
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
