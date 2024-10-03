import logging
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from pipeline_util import process_csv_files


DELAY_DOWNLOAD = 5
DELAY_SELECT = 3
DELAY_END = 2

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

    consulta_por = Select(driver.find_element(By.ID, "segment"))
    consulta_por.select_by_value("2")

    time.sleep(DELAY_SELECT)

    logging.info("Clicking download button.")
    download_link = driver.find_element(By.LINK_TEXT, "Download")
    download_link.click()
    
    time.sleep(DELAY_END)
    
    logging.info("Formatting date field")
    process_csv_files(DOWNLOAD_DIR)

    logging.info("The end =)")

finally:
    driver.quit()
