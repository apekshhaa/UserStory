import requests
import time

URL = "https://www.thespreadsheetguru.com/wp-content/uploads/2022/12/EmployeeSampleData.zip"

def download_zip(retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(URL, timeout=10)

            if response.status_code == 200:
                with open("employee_data.zip", "wb") as file:
                    file.write(response.content)

                print("ZIP download successful")
                return True

            print(f"Attempt {attempt + 1} failed with status code: {response.status_code}")

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")

        time.sleep(2)

    print("ZIP download failed after retries")
    return False


if __name__ == "__main__":
    download_zip()