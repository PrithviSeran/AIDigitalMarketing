import math
import transformers
import torch
import time

ts = time.time()
lt = time.localtime()

print(f"Loading Model {lt.tm_hour}:{lt.tm_min}:{lt.tm_sec}")

device = "cpu"

model_id = "meta-llama/Meta-Llama-3-8B"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"low_cpu_mem_usage": True}
#    device_map="auto",
)

pipeline("how are you?")

