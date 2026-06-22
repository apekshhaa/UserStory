from downloader import download_zip
from extractor import extract_zip
from validator import validate_excel


def main():
    print("Starting Employee ZIP Pipeline...\n")

    if not download_zip():
        print("Download failed")
        return

    excel_file = extract_zip()

    if not excel_file:
        print("Extraction failed")
        return

    if not validate_excel(excel_file):
        print("Validation failed")
        return

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    main()