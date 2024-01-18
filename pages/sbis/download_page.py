from ..base_page import BasePage
from ..sbis_locators import DownloadPageLocators

from selenium.webdriver import Remote as WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import re
import time

class DownloadPage(BasePage):
  def __init__(self, driver: WebDriver):
    url = "https://sbis.ru/download"
    super().__init__(driver, url)

  def change_active_tab(self, tab_id):
    content = self.get_active_tab_content()
    tab_selector = f'.controls-TabButton[data-id="{tab_id}"]'

    tab_control = self.driver.find_element(By.CSS_SELECTOR, tab_selector)
    tab_control.click()

    WebDriverWait(self.driver, 5).until(EC.invisibility_of_element(content), 
                                        "Tab content on download page did not change after clicking tab control")

  def get_active_tab_content(self):
    tab_content = self.driver.find_element(*DownloadPageLocators.ACTIVE_TAB)
    return tab_content
  
  def download_web_plugin(self, timeout=5):
    link = self.driver.find_element(*DownloadPageLocators.DOWNLOAD_PLUGIN_LINK)
    link.click()

    time.sleep(timeout)

  def should_be_same_size_file(self, filename):
    link = self.driver.find_element(*DownloadPageLocators.DOWNLOAD_PLUGIN_LINK)
    size = float(re.findall(r'\d+\.\d+', link.text)[0])
    path = f'{os.getcwd()}\\tests'

    os.chdir(path)
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    for f in files:
      if f == filename:
        f_size = round(os.stat(f).st_size / 1024 ** 2, 2)
        os.remove(f)

        assert f_size == size, \
          f"Downloaded {filename} have wrong size, expected {size}, got {f_size}"

        return
    
    raise Exception(f"{filename} not found in tests directory")