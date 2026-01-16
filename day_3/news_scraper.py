import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    books = soup.find_all("h3")
    
    print(f"we find {len(books)} books")
    
    for index, book in enumerate(books, 1):
        title = book.get_text()
        print(f"{index}. {title}")

except Exception as e:
    print(f"erorr{e}")