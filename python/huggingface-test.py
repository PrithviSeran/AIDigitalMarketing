from huggingface_hub import login
import transformers
from transformers import pipeline
import torch


#login(token="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")
# Load model directly
#pipe = pipeline("text-generation", model="meta-llama/Meta-Llama-3-8B")

#pipe("Hi How Are you?")

"""
model_id = "meta-llama/Meta-Llama-3-70B"

#pipeline = transformers.pipeline(
#    "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
#)

# Use a pipeline as a high-level helper
pipe = pipeline("text-generation", model="meta-llama/Meta-Llama-3-70B")

"""

from huggingface_hub import InferenceClient

client = InferenceClient(
    "meta-llama/Meta-Llama-3-8B-Instruct",
    token="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",
)

for message in client.chat_completion(
	messages=[{"role": "user", "content": "What slang is this?:' Oi Bruv, its chtuesday innit?'"}],
	max_tokens=500,
	stream=True,
):
    print(message.choices[0].delta.content, end="")

# Use a pipeline as a high-level helper

#pipe = pipeline("text-generation", model="meta-llama/Meta-Llama-3.1-405B")

#pipe("How Are you")