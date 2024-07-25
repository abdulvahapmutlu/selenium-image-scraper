from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import requests
from PIL import Image
from io import BytesIO
import os
import time

# Setup Chrome driver using webdriver_manager
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("site_link")

# XPaths
image_row_xpath = "xpath"
image_xpath = "xpath"
next_page_button_xpath = "xpath"

# Function to scroll and load more images
def load_more_images():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)  # Increased wait time to ensure all images load

# Function to click the 'Next page' button using JavaScript
def click_next_page():
    try:
        next_page_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, next_page_button_xpath))
        )
        driver.execute_script("arguments[0].click();", next_page_button)
    except Exception as e:
        print("Failed to click 'Next page' button: ", e)

# Scrape image URLs
image_urls = set()
page_count = 0

while len(image_urls) < 2000 and page_count < 20:  # Limited to 20 pages
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, image_row_xpath)))
    image_rows = driver.find_elements(By.XPATH, image_row_xpath)
    
    for row in image_rows:
        image_elements = row.find_elements(By.XPATH, image_xpath)
        for img in image_elements:
            srcset = img.get_attribute('srcset')
            if srcset:
                img_url = srcset.split(', ')[-1].split(' ')[0]  # Get the highest resolution image
                image_urls.add(img_url)
                if len(image_urls) >= 2000:
                    break
    
    if len(image_urls) < 2000:
        click_next_page()
        page_count += 1
        time.sleep(10)  # Wait for the next page to load

# Save images to local directory
output_dir = "scripted_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i, url in enumerate(image_urls):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.save(os.path.join(output_dir, f"image_{i+1}.jpg"))
    except Exception as e:
        print(f"Failed to save image {i+1}: {e}")

driver.quit()
