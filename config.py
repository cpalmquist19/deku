import os
import datetime
from datetime import date
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load environment variables from .env file
load_dotenv()

SITE_UNDER_TEST = os.getenv("DEKU_SITE_UNDER_TEST")

TODAY = date.today().strftime("%Y%m%d")
NOW = datetime.datetime.now()

# Get environment variables
USERNAME = os.getenv("DEKU_USERNAME")
PASSWORD = os.getenv("DEKU_PASSWORD")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

RUNS_FOLDER = os.path.join(ROOT_DIR, "runs")
if not os.path.exists(RUNS_FOLDER):
    os.makedirs(RUNS_FOLDER)

TODAY_FOLDER = os.path.join(RUNS_FOLDER, TODAY)
if not os.path.exists(TODAY_FOLDER):
    os.makedirs(TODAY_FOLDER)

NOW = datetime.datetime.now()
RUNTIME = NOW.strftime("%Y%m%d%H%M%S")

RUN_FOLDER = os.path.join(TODAY_FOLDER, RUNTIME)
if not os.path.exists(RUN_FOLDER):
    os.makedirs(RUN_FOLDER)

PAGES_FOLDER = os.path.join(RUN_FOLDER, "pages")
if not os.path.exists(PAGES_FOLDER):
    os.makedirs(PAGES_FOLDER)

print(f"TODAY is {TODAY}")
print(f"RUNTIME is {RUNTIME}")
print(f"RUN_FOLDER is {RUN_FOLDER}")
print(f"PAGES_FOLDER is {PAGES_FOLDER}")

def getDateTime():
    return datetime.datetime.now()

def getFormattedDateTime():
    return getDateTime().strftime('%Y%m%d_%H%M%S')