from crewai import LLM

LMSTUDIO_DEEPSEEK_LLM = LLM(
    model="openai/deepseek-r1-distill-llama-8b",
    base_url="http://host.docker.internal:1234/v1",
)

__all__ = ["LMSTUDIO_DEEPSEEK_LLM"]
