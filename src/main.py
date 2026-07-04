from downloader import download_file
from validator import validate_csv


def main():
    print("Starting Employee Data Pipeline...\n")

    if not download_file():
        print("Download failed")
        return

    if not validate_csv():
        print("Validation failed")
        return

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    main()
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
