from selenium import webdriver
from bs4 import BeautifulSoup
import time

def get_instagram_posts(username):
    # Set up the Chrome webdriver (you need to have chromedriver installed)
    driver = webdriver.Chrome()

    # Open Instagram profile page
    driver.get(f'https://www.instagram.com/{username}/')
    time.sleep(2)  # Let the page load (you may need to adjust this time)

    # Get the page source after initial load
    page_source = driver.page_source

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the element containing the number of posts
    post_count_element = soup.find('span', {'class': 'g47SY'})

    if post_count_element:
        # Extract the text with the number of posts
        posts_count = post_count_element.text.replace(',', '').strip()
        print(f"{username} has {posts_count} posts on Instagram.")
    else:
        print(f"Couldn't find post count for {username}.")

    # Close the webdriver
    driver.quit()

# Example usage
get_instagram_posts('example_username')
