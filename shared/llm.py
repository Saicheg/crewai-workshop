from crewai import LLM

LMSTUDIO_DEEPSEEK_LLM = LLM(
    model="openai/deepseek-r1-distill-llama-8b",
    base_url="http://host.docker.internal:1234/v1",
)

LMSTUDIO_QWEN_2_5_7B_LLM = LLM(
    model="openai/qwen2.5-7b-instruct-1m",
    base_url="http://host.docker.internal:1234/v1",
)

__all__ = ["LMSTUDIO_DEEPSEEK_LLM", "LMSTUDIO_QWEN_2_5_7B_LLM"]
