# LLM Quick Tools ⚡

![PyPI](https://img.shields.io/pypi/v/llm-quick-tools)
![Python](https://img.shields.io/pypi/pyversions/llm-quick-tools)
![License](https://img.shields.io/github/license/aryanator/llm-quick-tools)
[![PyPI Downloads](https://static.pepy.tech/badge/llm-quick-tools)](https://pepy.tech/projects/llm-quick-tools)

A lightweight dual-purpose library for:
1. **Prompt Evaluation** - Score and improve LLM inputs
2. **Mock LLM** - Simulate API responses during development

## Installation

```bash
pip install llm-quick-tools
```

---

## 1. Prompt Scoring 🔍

Evaluate prompt quality across multiple dimensions.

### Quick Start
```python
from llm_quick_tools import PromptEvaluator

evaluator = PromptEvaluator()
scores = evaluator.evaluate(
    "Explain quantum computing to a 5-year-old",
    task="education"
)

print(scores)
```
**Output:**
```python
{
    'length': 0.38,        # Optimal 20-100 chars
    'clarity': 0.9,        # Sentence structure
    'toxicity': 0.02,      # Harmful content risk
    'task_alignment': 0.8  # Relevance to education
}
```

### Scoring Metrics
| Metric | Range | Ideal | Description |
|--------|-------|-------|-------------|
| Length | 0-1 | 0.3-0.7 | Prompt character length |
| Clarity | 0-1 | >0.8 | Sentence complexity |
| Toxicity | 0-1 | <0.1 | Risk of harmful content |
| Task Alignment | 0-1 | >0.7 | Relevance to specified task |

---

## 2. Mock LLM 🤖

Simulate LLM responses without API calls.

### Response Modes
```python
from llm_quick_tools import MockLLM

# Initialize with different modes
echo_llm = MockLLM(mode="echo")
template_llm = MockLLM(mode="template")
```

#### Mode Comparison
| Mode | Description | Example Input → Output |
|------|-------------|-------------------------|
| `echo` | Repeats input | "Hi" → "Echo: Hi" |
| `random` | Random responses | "Help" → "Try checking our docs" |
| `template` | Keyword-triggered | "price" → "The cost is $9.99" |

### Template Management
```python
# Add custom templates
template_llm.add_template(
    "contact support",
    "Email us at help@company.com"
)

# Load from JSON
template_llm.load_templates("path/to/templates.json")

# Generate responses
print(template_llm.generate("How to contact support?"))
# Output: "Email us at help@company.com"
```

#### Pre-Loaded Templates
```python
{
    "hello": "Hi! How can I help?",
    "goodbye": "Have a nice day!",
    "pricing": "Our plans start at $9.99/mo",
    "refund": "Refunds take 5-7 business days",
    "tech support": "Try restarting your device"
}
```

---

## Advanced Usage

### Combined Workflow
```python
# 1. Evaluate prompt
scores = evaluator.evaluate("Tell me a joke about AI")

# 2. Generate mock response
if scores['toxicity'] < 0.1:
    response = template_llm.generate("Tell me a joke about AI")
else:
    response = "I can't comply with that request"
```

### Custom Template JSON
```json
// custom_templates.json
{
    "feature request": "Added to our roadmap",
    "bug report": "We'll investigate this issue",
    "order {} status": "Order #{} ships in 2 days"
}
```

---

## Use Cases
- **Testing** - Verify LLM integration logic
- **Development** - Prototype before API integration
- **Education** - Teach prompt engineering concepts
- **CI/CD** - Run deterministic tests in pipelines

---

## Contributing
1. Fork the [repository](https://github.com/aryanator/llm-quick-tools)
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License
MIT © [Aryan](https://github.com/aryanator)
