import os
from datetime import datetime


# --------------------------------------------
# Ensure Export Folder Exists
# --------------------------------------------

def ensure_export_folder(folder_name="exports"):

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    return folder_name


# --------------------------------------------
# Generate Unique Filename
# --------------------------------------------

def generate_filename(prefix="validated_cheques"):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{timestamp}.xlsx"

    return filename


# --------------------------------------------
# Export DataFrame to Excel
# --------------------------------------------

def export_to_excel(df, folder_name="exports"):

    # Ensure folder exists
    folder_path = ensure_export_folder(folder_name)

    # Generate filename
    filename = generate_filename()

    file_path = os.path.join(folder_path, filename)

    try:
        df.to_excel(file_path, index=False)

        return {
            "status": "success",
            "file_path": file_path
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e)
        }