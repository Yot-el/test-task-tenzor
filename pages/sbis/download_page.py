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
  
  def download_web_plugin(self, filename, timeout=5):
    link = self.driver.find_element(*DownloadPageLocators.DOWNLOAD_PLUGIN_LINK)
    link.click()

    time_step = 1
    while timeout > 0:
      if not (self.is_file_downloaded(filename)):
        timeout -= time_step
        time.sleep(time_step)

    if (self.is_file_downloaded(self, filename)):
      return
    
    raise Exception(f"File {filename} failed to load in {timeout} seconds")

  def is_file_downloaded(self, filename):
    path = f'{os.getcwd()}\\tests\\{filename}'

    return (os.path.exists(path))

  def should_be_same_size_file(self, filename):
    link = self.driver.find_element(*DownloadPageLocators.DOWNLOAD_PLUGIN_LINK)
    path = f'{os.getcwd()}\\tests\\{filename}'

    size = float(re.findall(r'\d+\.\d+', link.text)[0])
    file_size = round(os.path.getsize(path) / 1024 ** 2, 2)

    os.remove(path)

    assert size == file_size, \
      f"Size of {filename} expected to be {size}, got {file_size}"