🛒 Amazon Product Scraper

📄 Overview

The Amazon Product Scraper is a Python-based tool designed to fetch product details like title and price from Amazon product pages. This project uses HTTP requests and BeautifulSoup for web scraping, making it lightweight and efficient.

⚠️ Note: This tool is for educational purposes only and should comply with Amazon’s Terms of Service.

🚀 Key Features


Retrieve Product Details: Extracts the product title and price from a given Amazon product URL.
Lightweight & Fast: No Selenium needed, making the script faster and simpler to use.
User-Friendly Input: Simply paste the URL, and the scraper handles the rest.


🛠️ Installation
1. Clone the Repository
bash
git clone https://github.com/yourusername/amazon-product-scraper.git
cd amazon-product-scraper

3. Install Dependencies
bash
pip install -r requirements.txt


📋 Usage
Run the Script:
bash
python scraper.py
Enter the Amazon Product URL when prompted.

Example:

plaintext
Copy code
Enter product URL: https://www.amazon.in/dp/B08N5W4NNB
View the Output: The script will return the product title, price, and URL.

🐛 Troubleshooting
Title or Price Not Found: If the scraper returns "Title not found" or "Price not found," it might be due to changes in Amazon's HTML structure. Check and update the BeautifulSoup parsing logic if necessary.
