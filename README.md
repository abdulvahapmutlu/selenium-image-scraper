# Selenium Image Scraper for JavaScript-Driven Websites

This project is a Python script that uses Selenium to scrape images from websites that load content dynamically with JavaScript. It handles loading more images by scrolling and clicking through multiple pages, and saves high-resolution images locally.

## Features

- **Web Automation**: Utilizes Selenium to automate browser interactions and handle dynamic content loading.
- **Image Scraping**: Extracts high-resolution images from web pages.
- **Pagination Handling**: Automatically navigates through multiple pages to scrape more images.
- **Image Saving**: Saves the scraped images to a local directory with proper naming.

## Requirements

- Selenium
- Webdriver_manager
- Requests
- Pillow

## Setup

1. **Clone the repository**:
    ```
    git clone https://github.com/yourusername/selenium-image-scraper.git
    cd selenium-image-scraper
    ```

2. **Install the required packages**:
    ```
    pip install -r requirements.txt
    ```

3. **Update the script**:
    - Set the `driver.get("site_link")` to the URL of the website you want to scrape.
    - Update the XPaths: `image_row_xpath`, `image_xpath`, and `next_page_button_xpath` with the correct values from the target website.

4. **Run the script**:
    ```
    python scrape_images.py
    ```

## Usage

The script is designed to scrape up to 2000 images from a website by navigating through multiple pages and saving the images to a directory called `scripted_images`.

1. **Specify the website**:
    Update the `driver.get("site_link")` line in the script with the URL of the target website.

2. **Set the XPaths**:
    Update the XPaths for image rows, images, and the next page button:
    ```
    image_row_xpath = "your_image_row_xpath"
    image_xpath = "your_image_xpath"
    next_page_button_xpath = "your_next_page_button_xpath"
    ```

3. **Run the script**:
    Execute the script to start scraping images:
    ```
    python scrape_images.py
    ```

4. **Find your images**:
    The images will be saved in a directory named `scripted_images` with filenames in the format `image_1.jpg`, `image_2.jpg`, etc.

## Example

Here's an example of how to set up and run the script:

1. **Update the script with the target website and XPaths**:
    ```python
    driver.get("https://example.com")

    image_row_xpath = "//div[@class='image-row']"
    image_xpath = ".//img"
    next_page_button_xpath = "//button[@id='next-page']"
    ```

2. **Run the script**:
    ```bash
    python scrape_images.py
    ```

3. **Output**:
    The script will save the images in the `scripted_images` directory.

## Troubleshooting

- **Element Not Found**: Ensure the XPaths are correct and match the structure of the target website.
- **Timeouts**: Increase the sleep time in the `load_more_images` and `click_next_page` functions if the website is slow to load.

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the Apache 2.0 License.

## Acknowledgements

- Selenium for web automation
- WebDriver Manager for managing ChromeDriver
- Pillow for image processing

---

Happy Scraping! 🚀
