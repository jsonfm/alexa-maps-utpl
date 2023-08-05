import os
from dotenv import load_dotenv
import openai


load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY", "")


def fix_chatgpt_response(text: str):
    """Corrects the end of sentences with a final point."""
    split = text.split(".")[:-1]
    result = ".".join(split) + "."
    return result


def ask_to_chatgpt(
    prompt: str,
    engine: str = "text-davinci-003",
    max_tokens: int = 300,
    fixed: bool = True
):
    """Talk with chatGPT."""
    completion = openai.Completion.create(engine=engine,
                                          prompt=prompt,
                                          max_tokens=max_tokens)
    response = completion.choices[0].text
    if fixed:
        response = fix_chatgpt_response(response)
    return response


def ask_to_chatgpt_v2(
    prompt: str,
    model: str = "gpt-3.5-turbo",
    max_tokens: int = 300,
    fixed: bool = True
):
    """Talk with chatGPT."""
    messages = [{"role": "user", "content": prompt}]
    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        stream=False
    )
    response = completion.choices[0].message["content"]
    if fixed:
        response = fix_chatgpt_response(response)
    return response


if __name__ == "__main__":
    import time
    start = time.time()
    response = ask_to_chatgpt_v2("what is physics?", max_tokens=100)
    end = time.time()
    print(f"elapsed time: {end - start} secs.")
