import requests
from bs4 import BeautifulSoup


def fetch_webpage(url):
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        response.raise_for_status()
        return response
    except requests.exceptions.MissingSchema:
        print("Invalid URL: Make sure to include http:// or https://")
        return None
    except requests.exceptions.ConnectionError:
        print("Failed to fetch webpage: Connection error")
        return None
    except requests.exceptions.Timeout:
        print("Failed to fetch webpage: Request timed out")
        return None
    except requests.exceptions.HTTPError:
        print(f"Failed to fetch webpage: HTTP error ({response.status_code})")
        return None
    except requests.exceptions.RequestException:
        print("Failed to fetch webpage")
        return None


def extract_metadata(response):
    soup = BeautifulSoup(response.text, "html.parser")

    # Title
    title_tag = soup.find("title")
    title = title_tag.text.strip() if title_tag else "No title found"

    # Meta description
    meta_desc = soup.find("meta", attrs={"name": "description"})
    description = meta_desc["content"].strip() if meta_desc and meta_desc.get("content") else "No description available"

    # Open Graph metadata
    og_title_tag = soup.find("meta", attrs={"property": "og:title"})
    og_title = og_title_tag["content"].strip() if og_title_tag and og_title_tag.get("content") else None

    og_desc_tag = soup.find("meta", attrs={"property": "og:description"})
    og_description = og_desc_tag["content"].strip() if og_desc_tag and og_desc_tag.get("content") else None

    return title, description, og_title, og_description


def display_metadata(title, description, og_title, og_description):
    print("\n" + "=" * 50)
    print("          URL METADATA")
    print("=" * 50)
    print(f"  Title       : {title}")
    print(f"  Description : {description}")
    print("-" * 50)
    print("  Open Graph Metadata:")
    print(f"  og:title       : {og_title if og_title else 'Not available'}")
    print(f"  og:description : {og_description if og_description else 'Not available'}")
    print("=" * 50 + "\n")


def main():
    print("\n--- URL Metadata Scraper ---\n")
    url = input("Enter a website URL: ").strip()

    if not url:
        print("Invalid URL: No URL entered")
        return

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print(f"\nFetching: {url}\n")

    response = fetch_webpage(url)
    if response is None:
        return

    title, description, og_title, og_description = extract_metadata(response)
    display_metadata(title, description, og_title, og_description)

    if response.history:
        print(f"Note: Redirected to {response.url}")


if __name__ == "__main__":
    main()