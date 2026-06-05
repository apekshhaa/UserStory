import requests
import logging
import time

URL = "https://api.slingacademy.com/v1/sample-data/files/employees.json"

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def fetch_employee_data(retries=3):

    for attempt in range(retries):

        try:
            response = requests.get(URL, timeout=5)

            if response.status_code == 200:
                return response.json()

            logging.error(
                f"API returned status code {response.status_code}"
            )

        except requests.exceptions.Timeout:
            logging.error("Request timed out")

        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")

        time.sleep(2)

    raise Exception("Failed after multiple retries")


if __name__ == "__main__":
    data = fetch_employee_data()
    print(type(data))