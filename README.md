# AI-based SEO Blog Post Creation Tool

## Overview
This project is an AI-powered tool designed to automate the creation of SEO-optimized blog posts. The tool scrapes best-selling or trending products from an e-commerce site, automates SEO keyword research, generates blog post content incorporating those keywords, and posts the articles to platforms like WordPress or Medium.

## Features
- Scrapes best-selling products from Amazon (or other e-commerce sites).
- Automates SEO keyword research using placeholder logic (can be extended to use real SEO tools APIs).
- Generates 150-200 word blog posts highlighting the product and naturally incorporating SEO keywords.
- Posts articles to WordPress or Medium using their respective APIs.

## File Structure
- `scraper.py`: Contains functions to scrape trending news and best-selling products.
- `keyword_research.py`: Automates SEO keyword research (placeholder implementation).
- `script_generator.py`: Generates blog post content based on product and keywords.
- `post_publisher.py`: Handles posting blog articles to WordPress and Medium.
- `main.py`: Orchestrates the entire SEO blog post creation pipeline.

## Setup and Usage
1. Install required Python packages:
   ```
   pip install requests beautifulsoup4
   ```

2. Configure environment variables for WordPress posting (optional):
   - `WORDPRESS_URL`: Your WordPress site URL.
   - `WORDPRESS_USER`: WordPress username.
   - `WORDPRESS_PASSWORD`: WordPress password.

3. Run the tool:
   ```
   python3 main.py
   ```

## Notes
- The product scraping function currently targets Amazon's Best Sellers page. Due to Amazon's anti-scraping measures, this may not always work reliably. Consider using official APIs or other data sources for production use.
- The SEO keyword research function uses placeholder keywords. Integrate with real SEO tools APIs like Google Keyword Planner or Ubersuggest for better results.
- The blog post generation uses a simple template. Integrate with AI content generation APIs like OpenAI GPT for more natural and varied content.
- Posting functions support WordPress and Medium. Update credentials and tokens accordingly.

## License
This project is provided as-is for demonstration purposes.
