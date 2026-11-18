import time
from bs4 import BeautifulSoup # type: ignore
import pandas as pd # type: ignore
import requests # type: ignore

# List to store extracted book data
books_data = []

# Dictionary to convert text ratings into numerical values for easier analysis
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

# Loop through pages (1 to 5 as a sample; can be increased up to 50)
for page in range(1, 6):
    url = f'http://books.toscrape.com/catalogue/page-{page}.html'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f'Failed to load page {page}')
        continue

    soup = BeautifulSoup(response.content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        # 1. Extract book title
        title = book.h3.a['title']

        # 2. Extract price and clean the currency symbol (£)
        price_text = book.find('p', class_='price_color').text
        price = float(price_text.replace('£', '').strip())

        # 3. Extract star rating and map it to a number
        rating_class = book.find('p', class_='star-rating')['class']
        rating_word = rating_class[
            1
        ]  # The second class represents the rating (e.g., 'Three')
        rating = rating_map.get(rating_word, 0)

        # 4. Extract stock availability status
        availability = book.find('p', class_='instock availability').text.strip()

        books_data.append({
            'Title': title,
            'Price_GBP': price,
            'Rating': rating,
            'Availability': availability,
        })

    print(f'Page {page} scraped successfully...')
    time.sleep(1)  # Polite delay to avoid overwhelming the server

# Convert the list of dictionaries to a DataFrame and save to CSV
df = pd.DataFrame(books_data)
df.to_csv('books_dataset.csv', index=False, encoding='utf-8-sig')

print('\nScraping completed! Data saved to books_dataset.csv')
print(df.head())