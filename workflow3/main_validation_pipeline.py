from validation import validate_cheque_data

# ---------------------------------------------------
# Universal Processing Function (Validation Only)
# ---------------------------------------------------

def process_cheques(input_data):

    # Convert single cheque to list
    if isinstance(input_data, dict):
        input_data = [input_data]

    frontend_list = []

    for cheque in input_data:

        validation_result = validate_cheque_data(cheque)

        validated_data = validation_result.get("validated_data", {})
        error_flags = validation_result.get("error_flags", [])
        warning_flags = validation_result.get("warning_flags", [])

        frontend_list.append({
            
            "cheque_number": validated_data.get("cheque_number"),
            "date": validated_data.get("date"),
            "payee_name": validated_data.get("payee_name"),
            "amount_number": validated_data.get("amount_number"),
            "amount_words": validated_data.get("amount_words"),
            "bank_name": validated_data.get("bank_name"),
            "error_flags": error_flags,
            "warning_flags": warning_flags
        })

    return {
        "total_processed": len(frontend_list),
        "cheques": frontend_list
    }


# ---------------------------------------------------
# Testing Block
# ---------------------------------------------------

if __name__ == "__main__":
    import os
    import json

    BATCH_PATH = "output.json"

    if not os.path.exists(BATCH_PATH):
        raise FileNotFoundError("Extracted batch file not found.")

    with open(BATCH_PATH, "r", encoding="utf-8") as f:
        extracted_data = json.load(f)

    for cheque in extracted_data:
        result = process_cheques(cheque)
        


  

    import json
    print(json.dumps(result, indent=4))