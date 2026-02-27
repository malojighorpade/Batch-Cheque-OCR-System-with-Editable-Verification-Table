# --------------------------------------------
# Scoring Configuration
# --------------------------------------------

ERROR_DEDUCTION = {
   
    "invalid_cheque_number": 15,
    "invalid_date_format": 15,
    "invalid_calendar_date": 15,
    "cheque_expired": 30,
    "invalid_amount_number": 15
}

WARNING_DEDUCTION = {
    "post_dated_cheque": 5
}


# --------------------------------------------
# Confidence Classification
# --------------------------------------------

def classify_confidence(score: int):

    if score >= 85:
        return "High"
    elif score >= 60:
        return "Medium"
    else:
        return "Low"


# --------------------------------------------
# Main Scoring Function
# --------------------------------------------

def calculate_confidence(validation_result: dict):

   
    error_flags = validation_result.get("error_flags", [])
    warning_flags = validation_result.get("warning_flags", [])

    score = 100

    # Deduct for Errors
    for error in error_flags:
        deduction = ERROR_DEDUCTION.get(error, 10)  # default deduction
        score -= deduction

    # Deduct for Warnings
    for warning in warning_flags:
        deduction = WARNING_DEDUCTION.get(warning, 2)
        score -= deduction

    # Ensure score is within 0–100
    score = max(0, min(100, score))

    confidence_level = classify_confidence(score)

    # Final structured scoring output
    scoring_output = {
        
        "validated_data": validation_result.get("validated_data"),
        "error_flags": error_flags,
        "warning_flags": warning_flags,
        "date_status": validation_result.get("date_status"),
        "confidence_score": score,
        "confidence_level": confidence_level
    }

    return scoring_output