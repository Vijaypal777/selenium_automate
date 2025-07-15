from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# Hide logging
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Headless mode (invisible browser)
options.add_argument("--headless=new")  # Use `--headless` for Chrome < 109

# Optional: performance tweaks
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get("https://tutorialsninja.com/demo/")
print(driver.title)
driver.quit()
