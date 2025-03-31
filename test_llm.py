from llm_tools import PromptEvaluator

eval = PromptEvaluator()
print(eval.evaluate("Write a poem about AI", task="creative"))
# Output: {'length': 0.22, 'clarity': 1.0, 'toxicity': 0.001, 'task_alignment': 0.33}

from llm_tools import MockLLM

llm = MockLLM(mode="template")
llm.add_template("price", "Our product costs $99")
print(llm.generate("What's the price?"))  # Output: "Our product costs $99"