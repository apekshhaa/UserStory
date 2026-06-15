import requests
import time

URL = "https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download"


def download_file(retries=3):

    for attempt in range(retries):

        try:
            response = requests.get(URL, timeout=10)

            if response.status_code == 200:

                with open("employee_data.csv", "wb") as file:
                    file.write(response.content)

                print("Download successful")
                return True

            print(f"Attempt {attempt + 1} failed")

        except Exception as e:
            print(f"Attempt {attempt + 1}: {e}")

        time.sleep(2)

    print("Download failed after retries")
    return False


if __name__ == "__main__":
    download_file()