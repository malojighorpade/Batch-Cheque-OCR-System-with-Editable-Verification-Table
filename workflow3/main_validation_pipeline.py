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
            "cheque_id": validated_data.get("cheque_id"),
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

    sample_inputs = [
        {
            "cheque_id": "CHQ-TEST1234",
            "cheque_number": "123456",
            "date": "25/02/2026",
            "payee_name": "Rahul Sharma",
            "amount_number": "5000",
            "amount_words": "Five Thousand Only",
            "bank_name": "SBI"
        },
        {
            "cheque_id": "CHQ-TEST5678",
            "cheque_number": "99999",
            "date": "05/03/2026",
            "payee_name": "Amit Kumar",
            "amount_number": "abc",
            "amount_words": "Three Thousand Only",
            "bank_name": "HDFC"
        }
    ]

    result = process_cheques(sample_inputs)

    import json
    print(json.dumps(result, indent=4))