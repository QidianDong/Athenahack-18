import uuid

from launcher import celery

from ..ml import Predictor

predictor = Predictor()


@celery.task(name="scan.text.reason")
def scan_text_reason(texts: list[str]) -> list[str]:
    return [result.label for result in predictor.predict(texts)]


@celery.task(name="scan.text")
def scan_text(texts: list[str]):
    return [result for result in predictor.predict(texts)]


@celery.task(name="scan.doc")
def scan_doc(id: uuid.UUID, text: str):
    raise NotImplementedError


@celery.task(name="scan.doc.reason")
def scan_doc_reason(id: uuid.UUID):
    raise NotImplementedError
