import requests

URL = "https://api.slingacademy.com/v1/sample-data/files/employees.json"

def fetch_employee_data():
    response = requests.get(URL)

    if response.status_code == 200:
        return response.json()

    raise Exception(f"API Error: {response.status_code}")


if __name__ == "__main__":
    data = fetch_employee_data()
    print(type(data))