from scraper import fetch_employee_data
from transformer import normalize_data

data = fetch_employee_data()

df = normalize_data(data)

print(df[["Full Name", "phone", "designation","salary","salary_usd"]].head(10))
df.to_csv(
    "output/employees_cleaned.csv",
    index=False
)

print("CSV exported successfully!")