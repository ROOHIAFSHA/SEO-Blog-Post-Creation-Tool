from scraper import get_best_selling_products
from keyword_research import get_seo_keywords
from script_generator import generate_blog_post
from post_publisher import post_to_wordpress, post_to_medium
import os

def seo_blog_post_creation_pipeline():
    print("Starting AI-based SEO Blog Post Creation Tool...")

    # Step 1: Scrape best-selling products
    products = get_best_selling_products()
    if not products:
        print("No best-selling products found. Exiting.")
        return

    # For demonstration, process the top product
    top_product = products[0]
    product_name = top_product['name']
    print(f"Processing product: {product_name}")

    # Step 2: Automate SEO keyword research
    keywords = get_seo_keywords(product_name)
    print(f"SEO keywords: {keywords}")

    # Step 3: Generate blog post content
    blog_post = generate_blog_post(product_name, keywords)
    print(f"Generated blog post:\n{blog_post}")

    # Step 4: Post the article (example for WordPress)
    wordpress_url = os.getenv('WORDPRESS_URL', 'https://yourwordpresssite.com')
    wordpress_user = os.getenv('WORDPRESS_USER', 'admin')
    wordpress_password = os.getenv('WORDPRESS_PASSWORD', 'password')

    post_response = post_to_wordpress(product_name, blog_post, wordpress_url, wordpress_user, wordpress_password)
    if post_response:
        print("Blog post published successfully.")
    else:
        print("Failed to publish blog post.")

if __name__ == "__main__":
    seo_blog_post_creation_pipeline()
