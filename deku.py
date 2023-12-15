def setup_chrome_options(config):
    # Set up Chrome options for Selenium WebDriver
    chrome_options = config.Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    return chrome_options

def initialize_webdriver(config, chrome_options):
    # Initialize the Chrome WebDriver with specified options
    current_dir = config.os.path.dirname(config.os.path.abspath(__file__))
    driver_path = config.os.path.join(current_dir, 'bin', 'chromedriver.exe')
    service_path = config.Service(driver_path)
    driver = config.webdriver.Chrome(service=service_path, options=chrome_options)
    return driver

def navigate_to_site_under_test(driver):
    driver.get(config.SITE_UNDER_TEST)

def log_in_to_site_under_test(driver):
    driver.find_element(config.By.ID, "username").send_keys(config.USERNAME)
    driver.find_element(config.By.ID, "password").send_keys(config.PASSWORD)
    driver.find_element(config.By.CSS_SELECTOR, "button[type='submit']").click()

def get_current_page_title(driver):
    return driver.title

def get_site_under_test_dom(driver):
    return driver.page_source

def get_current_page_path(driver):
    return urlparse(driver.current_url).path

def getPageDetails(driver):
    pageTitle = get_current_page_title(driver)
    site_under_test_dom = get_site_under_test_dom(driver)
    current_page_path = get_current_page_path(driver)
    file_name_with_extension = os.path.basename(current_page_path)
    file_name = os.path.splitext(file_name_with_extension)[0]
    return pageTitle, site_under_test_dom, current_page_path, file_name_with_extension, file_name

def save_site_under_test_dom(config, site_under_test_dom, file_name):
    filepath = config.os.path.join(config.PAGES_FOLDER, f"{file_name}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(site_under_test_dom)

def screenshot_page(config, driver):
    screenshotFilename = f'screenshot_{config.getFormattedDateTime()}.png'
    screenshotFilePath = config.os.path.join(config.PAGES_FOLDER, screenshotFilename)
    driver.save_screenshot(screenshotFilePath)

import os
import config
from urllib.parse import urlparse

chrome_options = setup_chrome_options(config)
driver = initialize_webdriver(config, chrome_options)

navigate_to_site_under_test(driver)
log_in_to_site_under_test(driver)

pageTitle, site_under_test_dom, current_page_path, file_name_with_extension, file_name = getPageDetails(driver)

save_site_under_test_dom(config, site_under_test_dom, file_name)
screenshot_page(config, driver)

driver.quit()