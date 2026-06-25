import pandas as pd
from scraper import scrape_page

def main():
    all_books = []

    for page in range(1, 51):
        if page == 1:
            url = "http://books.toscrape.com/"
        else:
            url = f"http://books.toscrape.com/catalogue/page-{page}.html"

        

        books = scrape_page(url)
        all_books.extend(books)

    df = pd.DataFrame(all_books)

    print(df.head())
    print(f"Total books scraped: {len(df)}")

    df.to_csv("books_data.csv", index=False)

    print("CSV exported successfully!")


if __name__ == "__main__":
    main()