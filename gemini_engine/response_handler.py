import json
import re


def clean_response_text(text: str) -> str:
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)
    return text.strip()


def safe_json_parse(text: str) -> dict:
    cleaned_text = clean_response_text(text)

    try:
        return json.loads(cleaned_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON returned from Gemini: {e}")


def with_retry(extract_function, *args, max_retries=2):
    """
    Flexible retry wrapper.
    Works with any number of arguments.
    """
    attempt = 0

    while attempt <= max_retries:
        try:
            raw_response = extract_function(*args)
            return safe_json_parse(raw_response)

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            attempt += 1

            if attempt > max_retries:
                raise RuntimeError("Extraction failed after retries")