from openai import OpenAI
from config import settings

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=settings.NVIDIA_API_KEY
)

completion = client.chat.completions.create(
    model="nvidia/llama-3.1-nemotron-70b-instruct",
    messages=[{
        "role": "user",
        "content": "How big is the NVIDIA training dataset?"
    }],
    temperature=0.5,
    top_p=1,
    max_tokens=1024,
    stream=True
)

# Print the response chunks
for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
