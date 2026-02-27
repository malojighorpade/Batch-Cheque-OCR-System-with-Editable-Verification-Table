def format_for_frontend(scoring_result: dict):

    validated_data = scoring_result.get("validated_data", {})

    frontend_json = {
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
        "error_flags": scoring_result.get("error_flags"),
        "warning_flags": scoring_result.get("warning_flags")
    }

    return frontend_json