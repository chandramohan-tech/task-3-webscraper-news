import requests
from bs4 import BeautifulSoup


url = "https://www.bbc.com/news"


response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to retrieve page: {response.status_code}")
    exit()


soup = BeautifulSoup(response.text, "html.parser")


headlines = soup.find_all("h3")


headlines_list = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, title in enumerate(headlines_list, start=1):
        f.write(f"{i}. {title}\n")

print(f"✅ {len(headlines_list)} headlines saved to headlines.txt")
