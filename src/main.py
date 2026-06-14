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