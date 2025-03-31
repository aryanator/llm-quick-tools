import random
from typing import Literal, Dict, Optional
import json
from pathlib import Path

class MockLLM:
    def __init__(
        self,
        mode: Literal["echo", "random", "template"] = "echo",
        template_pack: Optional[str] = None
    ):
        self.mode = mode
        self.templates = self._load_template_pack(template_pack) or {
            # Core templates (20 essential ones)
            "hello": "Hello! How can I assist you today?",
            "goodbye": "Goodbye! Have a great day!",
            "thanks": "You're welcome!",
            "joke": "Why don't scientists trust atoms? Because they make up everything!",
            "help": "I can help with general questions, jokes, and translations.",
            
            # Customer support (15 templates)
            "refund": "Refunds typically process within 5-7 business days.",
            "return": "You can return items within 30 days with receipt.",
            "track order": "Your order #{} will arrive on {}.".format(
                random.randint(1000,9999), 
                random.choice(["Monday", "Tuesday", "Wednesday"])
            ),
            
            # Tech support (10 templates)
            "password reset": "Visit our website to reset your password.",
            "login issues": "Please clear your browser cache and try again.",
            
            # E-commerce (10 templates)
            "price": "The current price is ${:.2f}.".format(random.uniform(10, 100)),
            "discount": "Use code SAVE20 for 20% off your first order!"
        }

    def _load_template_pack(self, pack_name: Optional[str]) -> Optional[Dict[str, str]]:
        """Load pre-defined template packs"""
        packs = {
            "customer_support": {
                "complaint": "We apologize for the inconvenience. Our team will contact you.",
                "exchange": "Item exchanges require original packaging.",
                "warranty": "The warranty covers defects for 1 year."
            },
            "education": {
                "homework": "Check the textbook Chapter {}.".format(random.randint(1,10)),
                "deadline": "Assignments are due by 11:59 PM on the due date."
            }
        }
        return packs.get(pack_name) if pack_name else None

    def generate(self, prompt: str) -> str:
        """Generate mock response with fuzzy matching"""
        if self.mode == "echo":
            return f"You said: {prompt}"
        
        elif self.mode == "random":
            responses = [
                "Let me think about that...",
                "Interesting question!",
                "Here's what I know about that topic...",
                "I need more information to help with that.",
                "Have you considered asking differently?"
            ]
            return random.choice(responses)
        
        elif self.mode == "template":
            # Fuzzy matching (checks for keywords)
            prompt_lower = prompt.lower()
            for trigger, response in self.templates.items():
                if trigger in prompt_lower:
                    if "{}" in response:  # Handle dynamic responses
                        return response.format(random.randint(1000,9999))
                    return response
            return "I'm not sure how to respond to that. Can you rephrase?"
        
        raise ValueError(f"Invalid mode: {self.mode}")

    def add_template(self, trigger: str, response: str):
        """Add/update a response template"""
        self.templates[trigger.lower()] = response

    def load_templates(self, file_path: str):
        """Load templates from JSON file"""
        try:
            with open(file_path) as f:
                self.templates.update(json.load(f))
        except Exception as e:
            print(f"Error loading templates: {e}")

    def save_templates(self, file_path: str):
        """Save templates to JSON file"""
        with open(file_path, 'w') as f:
            json.dump(self.templates, f, indent=2)