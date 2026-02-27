import json

from gemini_engine.pdf_processor import pdf_to_images
from gemini_engine.extractor import extract_cheque_data
from gemini_engine.response_handler import with_retry
from gemini_engine.data_store import EXTRACTED_CHEQUE_DATA


def process_pdf(pdf_path):
    pages = pdf_to_images(pdf_path)

    for page_image in pages:
        print(f"\nProcessing: {page_image}")

        # Correct extraction call
        result = with_retry(
            extract_cheque_data,
            page_image
        )

        # Store in shared variable
        EXTRACTED_CHEQUE_DATA.append(result)

    return EXTRACTED_CHEQUE_DATA


if __name__ == "__main__":
    data = process_pdf("samples/cheques.pdf")

    # Optional backup save
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("\nExtraction completed.")
    print("\n==== CURRENT DATA IN MEMORY ====\n")
    print(json.dumps(EXTRACTED_CHEQUE_DATA, indent=4))
    print("\nTotal Cheques Processed:", len(EXTRACTED_CHEQUE_DATA))