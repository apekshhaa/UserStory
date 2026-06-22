import pandas as pd

REQUIRED_COLUMNS = [
    "EEID",
    "Full Name",
    "Job Title",
    "Department",
    "Hire Date"
]

def validate_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        print("Excel file loaded successfully")
        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}")

        missing_columns = []

        for column in REQUIRED_COLUMNS:
            if column not in df.columns:
                missing_columns.append(column)

        if missing_columns:
            print(f"Missing columns: {missing_columns}")
            return False

        print("All required columns exist")
        return True

    except Exception as e:
        print(f"Validation Error: {e}")
        return False