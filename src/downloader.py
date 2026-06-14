import requests

URL = "https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download"

def download_file():
    try:
        response = requests.get(URL, timeout=10)

        if response.status_code == 200:
            with open("employee_data.csv", "wb") as file:
                file.write(response.content)

            print("Download successful")
            return True

        print(f"Download failed. Status code: {response.status_code}")
        return False

    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    download_file()