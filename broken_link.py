import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://tutorialsninja.com/demo/")

# Collect all <a> tag links
all_links = driver.find_elements(By.TAG_NAME, "a")
broken_links = []

for link in all_links:
    url = link.get_attribute("href")
    if url is None or not url.startswith("http"):
        continue  # Skip empty or internal anchors like '#'

    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code >= 400:
            broken_links.append((url, response.status_code))
    except requests.exceptions.RequestException as e:
        broken_links.append((url, str(e)))

driver.quit()

# Print broken links
if broken_links:
    print("\nBroken links found:")
    for url, error in broken_links:
        print(f"{url} --> {error}")
else:
    print("✅ No broken links found.")
