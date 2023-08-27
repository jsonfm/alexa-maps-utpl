import os
from dotenv import load_dotenv
import openai
import json

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

# Utils for queries
def take_json_from_string(string: str):
    """Returns a dict contained by a string message."""
    start_index = string.find("{")
    final_index = string.find("}")
    if start_index == -1 or final_index == -1:
        return None
    json_string = string[start_index:final_index + 1]
    data = json.loads(json_string)
    return data

def sort_countries_by_continent(countries: list, to_json: bool = True):
    query = f"""
    Sort the following countries list by continent:  {str(countries)}
    Return something like this: `{{
        "america": [...],
        "europa": [...],
        "africa": [...],
        "oceania": [...],
        "asia": [...]
        "antartida": [...]
    }}`
    """
    response = ask_to_chatgpt(query, max_tokens=500, fixed=False)
    if to_json:
        response = take_json_from_string(response)
    return response


if __name__ == "__main__":
    import time
    start = time.time()
    query = "What's astrophysics? Give me a short response."
    response = ask_to_chatgpt(query, max_tokens=500, fixed=False)
    end = time.time()
    print("response: ", response)
    print(f"elapsed time: {end - start} secs.")
