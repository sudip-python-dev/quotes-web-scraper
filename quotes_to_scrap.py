import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"

print(f"Scraping started: {url}")

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

print("Page scraped successfully.")
print("Processing data...")

quotes_data = soup.find_all("div", class_="quote")

rows = []

for quote in quotes_data:
    
    text = quote.find("span", class_="text").text.strip()
    
    author = quote.find("small", class_="author").text.strip()
    
    tags = quote.find_all("a", class_="tag")
    tag_list = [tag.text for tag in tags]
    
    row = {
        "Quote": text,
        "Author": author,
        "Tags": ", ".join(tag_list)
    }
    
    rows.append(row)

print("Data processed. Writing to CSV...")

with open("quotes_to_scrape.csv", "w", newline="", encoding="utf-8") as f:
    
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "Quote",
            "Author",
            "Tags"
        ]
    )
    
    writer.writeheader()
    writer.writerows(rows)

print("All done!")