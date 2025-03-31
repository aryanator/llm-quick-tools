import re
from transformers import pipeline

class PromptEvaluator:
    def __init__(self):
        self._toxicity_model = pipeline(
            "text-classification", 
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def evaluate(self, prompt: str, task: str = "general") -> dict:
        """Score prompt quality"""
        return {
            "length": self._length_score(prompt),
            "clarity": self._clarity_score(prompt),
            "toxicity": self._toxicity_score(prompt),
            "task_alignment": self._task_alignment(prompt, task)
        }

    def _length_score(self, prompt: str) -> float:
        return min(1, len(prompt) / 100)  # Normalize to 0-1

    def _clarity_score(self, prompt: str) -> float:
        return 1 - (prompt.count('?') / 3)  # Penalize multiple questions

    def _toxicity_score(self, prompt: str) -> float:
        result = self._toxicity_model(prompt)[0]
        return result['score'] if result['label'] == 'NEGATIVE' else 0

    def _task_alignment(self, prompt: str, task: str) -> float:
        task_keywords = {
            "qa": ["what", "why", "how", "explain"],
            "creative": ["write", "story", "poem"],
            "general": ["you", "help", "tell"]
        }
        matches = sum(kw in prompt.lower() for kw in task_keywords.get(task, []))
        return matches / max(1, len(task_keywords.get(task, [])))