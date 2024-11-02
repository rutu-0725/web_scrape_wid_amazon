import requests
from bs4 import BeautifulSoup

# Set headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5'
}

def get_product_details(product_url: str) -> dict:
    # Create an empty product details dictionary
    product_details = {}
    
    try:
        # Get the product page content and create a soup
        page = requests.get(product_url, headers=headers)
        page.raise_for_status()  # Raise an exception for bad requests
        soup = BeautifulSoup(page.content, 'lxml')
        
        # Attempt to find the product title and price with alternative tags and classes
        title = soup.find('span', attrs={'id': 'productTitle'})
        if not title:
            title = soup.find('span', attrs={'data-automation-id': 'title'})
        
        price_whole = soup.find('span', class_='a-price-whole')
        price_fraction = soup.find('span', class_='a-price-fraction')
        
        # Combine the price parts if they are found separately
        if price_whole and price_fraction:
            price = f"{price_whole.get_text().strip()}.{price_fraction.get_text().strip()}"
        elif price_whole:
            price = price_whole.get_text().strip()
        else:
            price = 'Price not found'
        
        # Add title and price to product details
        product_details['title'] = title.get_text().strip() if title else 'Title not found'
        product_details['price'] = price
        product_details['product_url'] = product_url
        
        return product_details

    except requests.exceptions.RequestException as e:
        print('Could not fetch product details')
        print(f'Failed with exception: {e}')
        return None
    except AttributeError as e:
        print('Could not fetch product details')
        print(f'Failed with exception: {e}')
        return None

# Get URL from user
product_url = input('Enter product URL: ')
product_details = get_product_details(product_url)

print(product_details)
