import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


DELAY_DOWNLOAD = 5
DOWNLOAD_DIR = dir_path = os.path.dirname(os.path.realpath(__name__)) + "/bovespa"


logging.basicConfig(level=logging.INFO)

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": DOWNLOAD_DIR,
    "download.prompt_for_download": False,
})

driver = webdriver.Chrome(options=chrome_options)
logging.info("Running selenium chrome webdrive")
logging.info(f"Files will be saved in {DOWNLOAD_DIR}")

try:
    
    logging.info("Visting Bovespa")
    driver.get("https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br")
    
    time.sleep(DELAY_DOWNLOAD)

    logging.info("Clicking download button.")
    download_link = driver.find_element(By.LINK_TEXT, "Download")
    download_link.click()
    
    time.sleep(10)
    logging.info("The end =)")

finally:
    driver.quit()
