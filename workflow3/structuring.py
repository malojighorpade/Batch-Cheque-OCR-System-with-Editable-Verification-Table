import pandas as pd


# --------------------------------------------
# Convert Single Cheque Result to DataFrame Row
# --------------------------------------------

def structure_single_cheque(scoring_result: dict):

    validated_data = scoring_result.get("validated_data", {})

    row = {
        "cheque_id": scoring_result.get("cheque_id"),
        "cheque_number": validated_data.get("cheque_number"),
        "date": validated_data.get("date"),
        "payee_name": validated_data.get("payee_name"),
        "amount_number": validated_data.get("amount_number"),
        "amount_words": validated_data.get("amount_words"),
        "bank_name": validated_data.get("bank_name"),
        "date_status": scoring_result.get("date_status"),
        "confidence_score": scoring_result.get("confidence_score"),
        "confidence_level": scoring_result.get("confidence_level"),
        "error_flags": ", ".join(scoring_result.get("error_flags", [])),
        "warning_flags": ", ".join(scoring_result.get("warning_flags", []))
    }

    df = pd.DataFrame([row])

    return df


# --------------------------------------------
# Convert Multiple Cheques to DataFrame
# --------------------------------------------

def structure_multiple_cheques(scoring_results: list):

    rows = []

    for result in scoring_results:

        validated_data = result.get("validated_data", {})

        row = {
            "cheque_id": result.get("cheque_id"),
            "cheque_number": validated_data.get("cheque_number"),
            "date": validated_data.get("date"),
            "payee_name": validated_data.get("payee_name"),
            "amount_number": validated_data.get("amount_number"),
            "amount_words": validated_data.get("amount_words"),
            "bank_name": validated_data.get("bank_name"),
            "date_status": result.get("date_status"),
            "confidence_score": result.get("confidence_score"),
            "confidence_level": result.get("confidence_level"),
            "error_flags": ", ".join(result.get("error_flags", [])),
            "warning_flags": ", ".join(result.get("warning_flags", []))
        }

        rows.append(row)

    df = pd.DataFrame(rows)

    return df