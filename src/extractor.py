import zipfile
import os

def extract_zip(zip_path="employee_data.zip", extract_to="extracted_files"):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

        print("ZIP extraction successful")

        files = os.listdir(extract_to)
        print("Extracted files:", files)

        for file in files:
            if file.endswith(".xlsx") or file.endswith(".xls"):
                return os.path.join(extract_to, file)

        print("No Excel file found")
        return None

    except Exception as e:
        print(f"Extraction error: {e}")
        return None