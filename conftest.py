import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture(scope="function")
def driver():
  download_dir = f"{os.path.dirname(__file__)}\\tests"
  options = Options()
  options.add_experimental_option("prefs", {"download.default_directory": download_dir, 
                                            "download.directory_upgrade": True, 
                                            "download.prompt_for_download": False, 
                                            "safebrowsing.enabled": True})
  options.add_argument("--safebrowsing-disable-download-protection")
  driver = webdriver.Chrome(options=options)
  
  yield driver
  driver.quit()
