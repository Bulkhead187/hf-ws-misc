from openai import OpenAI
from config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def query_nvidia_model(prompt: str, model: str = "nvidia/llama-3.1-nemotron-70b-instruct") -> None:
    try:
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=settings.NVIDIA_API_KEY
        )

        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            top_p=1,
            max_tokens=1024,
            stream=True
        )

        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    query_nvidia_model("How big is the NVIDIA training dataset?")
