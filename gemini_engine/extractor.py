from google.genai import types
from gemini_engine.config import client
from gemini_engine.prompt import build_prompt
import mimetypes


def extract_cheque_data(original_image_path, cropped_image_path=None):
    """
    Supports:
    - Single image mode (PDF page)
    - Two image mode (original + cropped)
    """

    prompt = build_prompt()

    mime_original, _ = mimetypes.guess_type(original_image_path)

    if not mime_original:
        raise ValueError("Could not detect MIME type")

    with open(original_image_path, "rb") as f:
        original_bytes = f.read()

    contents = [
        prompt,
        types.Part.from_bytes(
            data=original_bytes,
            mime_type=mime_original,
        )
    ]

    # Add cropped image only if provided
    if cropped_image_path:
        mime_cropped, _ = mimetypes.guess_type(cropped_image_path)

        if not mime_cropped:
            raise ValueError("Could not detect MIME type for cropped image")

        with open(cropped_image_path, "rb") as f:
            cropped_bytes = f.read()

        contents.append(
            types.Part.from_bytes(
                data=cropped_bytes,
                mime_type=mime_cropped,
            )
        )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
    )

    return response.text