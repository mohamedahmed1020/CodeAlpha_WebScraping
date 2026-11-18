# CodeAlpha - Web Scraping Task

## 📌 Project Overview
This project is part of the **CodeAlpha Data Analytics Internship**. The goal is to extract structured data from an e-commerce website (`Books to Scrape`) using Python and save it into a clean CSV dataset ready for Exploratory Data Analysis (EDA).

## 🛠️ Tools & Libraries Used
- **Python 3**
- **Requests:** For sending HTTP requests to web pages.
- **BeautifulSoup4:** For parsing HTML content and extracting target elements.
- **Pandas:** For structuring the extracted data and exporting it to CSV.

## 📊 Extracted Features
- **Title:** Full name of the book.
- **Price_GBP:** Price in British Pounds (cleaned and converted to float).
- **Rating:** Star rating converted into numerical scale (1 to 5).
- **Availability:** Stock status of the item.

## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the script: `python scraper.py`
3. The output will be saved as `books_dataset.csv`.
