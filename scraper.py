import requests
from bs4 import BeautifulSoup

def get_trending_news():
    """
    Scrape trending news articles from a news website.
    Returns a list of trending news headlines and links.
    """
    url = "https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve news")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    trending_news = []

    for article in articles[:10]:  # Get top 10 trending articles
        headline = article.find('h3')
        if headline:
            title = headline.text
            link = headline.find('a')['href']
            if link.startswith('.'):
                link = 'https://news.google.com' + link[1:]
            trending_news.append({'title': title, 'link': link})

    return trending_news

def get_best_selling_products():
    """
    Scrape best-selling or trending products from an e-commerce site (e.g., Amazon).
    Returns a list of products with name, price, and link.
    Note: This is a simplified example and may require adjustments for real sites.
    """
    url = "https://www.amazon.com/Best-Sellers/zgbs"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve best-selling products")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    products = []

    product_elements = soup.select('div.zg-item-immersion')[:10]  # Top 10 products
    for product in product_elements:
        name_elem = product.select_one('div.p13n-sc-truncate')
        price_elem = product.select_one('span.p13n-sc-price')
        link_elem = product.select_one('a.a-link-normal')

        name = name_elem.text.strip() if name_elem else "No name"
        price = price_elem.text.strip() if price_elem else "No price"
        link = "https://www.amazon.com" + link_elem['href'] if link_elem else "No link"

        products.append({'name': name, 'price': price, 'link': link})

    return products

if __name__ == "__main__":
    news = get_trending_news()
    for item in news:
        print(f"Title: {item['title']}\nLink: {item['link']}\n")

    products = get_best_selling_products()
    for product in products:
        print(f"Product: {product['name']}\nPrice: {product['price']}\nLink: {product['link']}\n")
