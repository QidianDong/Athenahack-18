import uuid

from launcher import celery


@celery.task(name="scan.text.reason")
def scan_text_reason(text: str):
    return "This is a placeholder"


@celery.task(name="scan.text")
def scan_text(text: str):
    return "This is a placeholder"


@celery.task(name="scan.doc")
def scan_doc(id: uuid.UUID, text: str):
    return "This is a placeholder"


@celery.task(name="scan.doc.reason")
def scan_doc_reason(id: uuid.UUID):
    return "This is a placeholder"
