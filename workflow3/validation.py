import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

REQUIRED_FIELDS = ["cheque_number","date","payee_name","amount_number","amount_words","bank_name"]

def validate_cheque_data(data: dict):
    error_flags = []
    warning_flags = []
    data_status = "Valid"

    
    for field in REQUIRED_FIELDS:
        if field not in data or not str(data[field]).strip():
            error_flags.append(f"missing_{field}")
    cheque_number=str(data.get("cheque_number", ""))
    if not re.fullmatch(r'^\d{6}$', cheque_number):
        error_flags.append("invalid_cheque_number")
    
    date_str = data.get("date", "")

    if re.fullmatch(r"\d{2}/\d{2}/\d{4}", date_str):
        try:
            cheque_date = datetime.strptime(date_str, "%d/%m/%Y")
            today = datetime.now()
            if cheque_date > today:
                warning_flags.append("post_dated_cheque")
                error_flags.append("future_date")
            elif cheque_date < today - relativedelta(months=3):
                warning_flags.append("cheque_expired")
                data_status = "Expired"
        except ValueError:
            error_flags.append("invalid_calendar_format")
    else:
        error_flags.append("invalid_date_format")
    
    amount_number= str(data.get("amount_number", "" )).replace(",", "")

    if not amount_number.isdigit():
        error_flags.append("invalid_amount_number")

    validated_output={
        
        "validated_data":data,
        "error_flags":error_flags,
        "warning_flags":warning_flags,
        "data_status":data_status
    }
    return validated_output
        
