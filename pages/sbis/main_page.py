from ..base_page import BasePage
from ..sbis_locators import MainPageLocators
from .contacts_page import ContactsPage
from .download_page import DownloadPage

from selenium.webdriver import Remote as WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

class MainPage(BasePage):

  def __init__(self, driver: WebDriver):
    url = "https://sbis.ru"
    super().__init__(driver, url)

  def go_to_contacts_page(self):
    new_page = ContactsPage(self.driver)

    try:
      self.driver.find_element(*MainPageLocators.CONTACTS_PAGE_LINK).click()
    except StaleElementReferenceException:
      self.driver.find_element(*MainPageLocators.CONTACTS_PAGE_LINK).click()

    self.switch_to_window(new_page.get_url())

    return new_page
  
  def go_to_download_page(self):
    new_page = DownloadPage(self.driver)

    download_link = self.driver.find_element(*MainPageLocators.DOWNLOAD_PAGE_LINK)

    try:
      download_link.location_once_scrolled_into_view
      download_link.click()
    except StaleElementReferenceException:
      download_link = self.driver.find_element(*MainPageLocators.DOWNLOAD_PAGE_LINK)
      download_link.location_once_scrolled_into_view
      download_link.click()

    self.switch_to_window(new_page.get_url())

    return new_page