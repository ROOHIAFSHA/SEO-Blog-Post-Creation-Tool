import requests

def post_to_wordpress(blog_title, blog_content, wordpress_url, username, password):
    """
    Post the blog article to a WordPress site using the REST API.
    """
    api_url = f"{wordpress_url}/wp-json/wp/v2/posts"
    data = {
        "title": blog_title,
        "content": blog_content,
        "status": "publish"
    }
    response = requests.post(api_url, json=data, auth=(username, password))
    if response.status_code == 201:
        print("Blog post published successfully on WordPress.")
        return response.json()
    else:
        print(f"Failed to publish blog post. Status code: {response.status_code}")
        print(response.text)
        return None

def post_to_medium(blog_title, blog_content, access_token, user_id):
    """
    Post the blog article to Medium using the Medium API.
    """
    api_url = f"https://api.medium.com/v1/users/{user_id}/posts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {
        "title": blog_title,
        "contentFormat": "html",
        "content": blog_content,
        "publishStatus": "public"
    }
    response = requests.post(api_url, json=data, headers=headers)
    if response.status_code == 201:
        print("Blog post published successfully on Medium.")
        return response.json()
    else:
        print(f"Failed to publish blog post. Status code: {response.status_code}")
        print(response.text)
        return None

if __name__ == "__main__":
    # Example usage (replace with real credentials and tokens)
    wp_url = "https://yourwordpresssite.com"
    wp_user = "admin"
    wp_pass = "password"
    medium_token = "your_medium_access_token"
    medium_user_id = "your_medium_user_id"

    title = "Sample Blog Post"
    content = "<p>This is a sample blog post content.</p>"

    # Uncomment to test WordPress posting
    # post_to_wordpress(title, content, wp_url, wp_user, wp_pass)

    # Uncomment to test Medium posting
    # post_to_medium(title, content, medium_token, medium_user_id)
