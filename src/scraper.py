import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "http://books.toscrape.com/"

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def scrape_page(url, retries=3):
    books = []

    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)

            if response.status_code != 200:
                print(f"Failed to fetch page: {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all("article", class_="product_pod")

            for article in articles:
                try:
                    title = article.h3.a["title"]

                    price_text = article.find("p", class_="price_color").text.strip().replace("Â", "")
                    price = float(price_text.replace("£", ""))

                    availability = article.find("p", class_="instock availability").text.strip()

                    rating_classes = article.find("p")["class"]
                    rating = rating_map.get(rating_classes[1], 0)

                    product_url = article.h3.a["href"]

                    books.append({
                        "Title": title,
                        "Price": price,
                        "Rating": rating,
                        "Availability": availability,
                        "URL": BASE_URL + product_url
                    })

                except Exception as e:
                    print(f"Skipping book due to error: {e}")

            return books

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2)

    return books