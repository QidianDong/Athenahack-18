import torch
from pydantic import BaseModel
from transformers import AutoModelForMaskedLM, AutoTokenizer, pipeline


class PredictedResult(BaseModel, frozen=True):
    text: str
    label: str
    score: float


class Predictor:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("GroNLP/hateBERT")
        self.model = AutoModelForMaskedLM.from_pretrained(
            "GroNLP/hateBERT", torch_dtype=torch.float32
        )
        self.classifier = pipeline(
            "text-classification", model="cardiffnlp/twitter-roberta-base-hate"
        )

    def predict(self, texts: list[str]) -> list[PredictedResult]:
        results = self.classifier(texts)
        return [
            PredictedResult(text=text, label=res["label"], score=res["score"])
            for text, res in zip(texts, results)
        ]
