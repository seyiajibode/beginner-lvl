import requests
from bs4 import BeautifulSoup

def scrape_browser(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raise error for bad status
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Get page title and all links
        title = soup.title.string if soup.title else "No title found"
        links = [a['href'] for a in soup.find_all('a', href=True)]

        print(f"Page Title: {title}")
        print("\nLinks found on page:")
        for link in links:
            print(link)

        return {"title": title, "links": links}

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None


if __name__ == "__main__":
    url = input("Enter a website URL: ")
    scrape_browser(url)
