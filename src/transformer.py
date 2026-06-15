import pandas as pd

def get_designation(exp):
    if exp < 3:
        return "System Engineer"
    elif exp <= 5:
        return "Data Engineer"
    elif exp <= 10:
        return "Senior Data Engineer"
    else:
        return "Lead"


def convert_inr_to_usd(salary):
    exchange_rate = 83.5
    return round(salary / exchange_rate, 2)


def normalize_data(data):
    df = pd.DataFrame(data)

    df["Full Name"] = df["first_name"] + " " + df["last_name"]

    df["designation"] = df["years_of_experience"].apply(get_designation)

    df["phone"] = df["phone"].apply(
        lambda x: "Invalid Number"
        if "x" in str(x)
        else x
    )

    df["age"] = df["age"].astype(int)
    df["years_of_experience"] = df["years_of_experience"].astype(int)
    df["salary"] = df["salary"].astype(int)

    # NEW COLUMN
    df["salary_usd"] = df["salary"].apply(convert_inr_to_usd)

    return df