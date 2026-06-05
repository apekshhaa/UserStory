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


def normalize_data(data):
    df = pd.DataFrame(data)

    # Full Name
    df["Full Name"] = df["first_name"] + " " + df["last_name"]

    # Designation
    df["designation"] = df["years_of_experience"].apply(get_designation)

    # Phone validation
    df["phone"] = df["phone"].apply(
        lambda x: "Invalid Number"
        if "x" in str(x)
        else x
    )

    # Data type conversions
    df["age"] = df["age"].astype(int)
    df["years_of_experience"] = df["years_of_experience"].astype(int)
    df["salary"] = df["salary"].astype(int)

    return df