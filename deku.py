import os
import config
from urllib.parse import urlparse

print(f"Testing import config")
print(f"RUNTIME = {config.RUNTIME}")

chromeOptions = config.Options()
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--window-size=1920,1080')

current_dir = config.os.path.dirname(config.os.path.abspath(__file__))
driver_path = config.os.path.join(current_dir, 'bin', 'chromedriver.exe')

servicePath = config.Service(driver_path)
driver = config.webdriver.Chrome(service = servicePath, options = chromeOptions)

print(f"USERNAME = {config.USERNAME}")
print(f"PASSWORD = {config.PASSWORD}")

# Login to website
driver.get(config.SITE_UNDER_TEST)
driver.find_element(config.By.ID, "username").send_keys(config.USERNAME)
driver.find_element(config.By.ID, "password").send_keys(config.PASSWORD)
driver.find_element(config.By.CSS_SELECTOR, "button[type='submit']").click()

# Get page source HTML
html = driver.page_source

# Parse the URL to get the path
url_parsed = urlparse(driver.current_url)
path = url_parsed.path

# Extract the page file name (e.g., 'login' or 'login.html')
file_name_with_extension = os.path.basename(path)

# Remove the extension if it exists to get just the 'login' part
file_name = os.path.splitext(file_name_with_extension)[0]

print("The file name of the current page is:", file_name)

pageTitle = driver.title

print(f"pageTitle = {pageTitle}")

# Save HTML to file
filepath = config.os.path.join(config.PAGES_FOLDER, f"{file_name}.html")
with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML saved locally to", filepath)
print("Attempting to take a screenshot...")

# Get the current time and format it as a string
timestamp = config.getFormattedDateTime()

# Append the timestamp to the screenshot filename
screenshotFilename = f'screenshot_{timestamp}.png'

screenshotFilePath = config.os.path.join(config.PAGES_FOLDER, screenshotFilename)

driver.save_screenshot(screenshotFilePath)

print("Screenshot taken")

driver.quit()