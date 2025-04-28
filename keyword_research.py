import requests

def get_seo_keywords(product_name):
    """
    Automate SEO keyword research for a given product name.
    This is a placeholder function. In a real scenario, this could call
    an API like Google Keyword Planner, Ubersuggest, or other SEO tools.
    For demonstration, it returns 3-4 sample keywords related to the product.
    """
    # Placeholder keywords - in real use, replace with API call results
    keywords = [
        f"buy {product_name}",
        f"{product_name} review",
        f"best price {product_name}",
        f"{product_name} features"
    ]
    return keywords

if __name__ == "__main__":
    sample_product = "wireless headphones"
    keywords = get_seo_keywords(sample_product)
    print(f"SEO keywords for '{sample_product}': {keywords}")
