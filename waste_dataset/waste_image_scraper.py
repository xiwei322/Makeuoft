import os
import requests
from bs4 import BeautifulSoup

def fetch_images(query, save_dir, num_images=50):
    print(f"Starting image download for category: {query}")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)

    search_url = f"https://www.google.com/search?q={query}+waste&tbm=isch"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to connect: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    image_tags = soup.find_all("img")

    print(f"Found {len(image_tags)} images for {query}")

    count = 0
    for img in image_tags:
        try:
            img_url = img.get("src")
            if img_url and img_url.startswith('http'):
                img_data = requests.get(img_url, headers=headers).content
                with open(os.path.join(save_dir, f"{query}_{count+1}.jpg"), 'wb') as f:
                    f.write(img_data)
                count += 1
                print(f"Downloaded {query}_{count}.jpg")
            if count >= num_images:
                break
        except Exception as e:
            print(f"Could not download image {count+1}: {e}")
    print(f"Completed downloading {count} images for {query}")

if __name__ == "__main__":
    base_dir = os.path.expanduser("~/Desktop/Makeuoft/waste_dataset")

    categories = ["recycle", "trash"]  # Removed 'plastic'
    for category in categories:
        fetch_images(category, os.path.join(base_dir, category), num_images=100)
