import pandas as pd

REQUIRED_COLUMNS = [
    "User Id",
    "First Name",
    "Last Name",
    "Sex",
    "Email",
    "Phone",
    "Job Title"
]


def validate_csv(file_path="employee_data.csv"):
    try:
        df = pd.read_csv(file_path)

        print("CSV loaded successfully")
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


if __name__ == "__main__":
    validate_csv()