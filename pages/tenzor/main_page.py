from ..base_page import BasePage
from .about_page import AboutPage
from ..tenzor_locators import MainPageLocators

from selenium.webdriver import Remote as WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

  def __init__(self, driver: WebDriver):
    url = "https://tensor.ru"
    super().__init__(driver, url)

  def should_be_card(self, title):
    card_selector = f'//p[contains(@class, "tensor_ru-Index__card-title") and text()="{title}"]'
    assert self.is_element_present(By.XPATH, card_selector), \
      f"card with the title '{title}' is not on the page"
    
  def go_to_about_page(self):
    new_page = AboutPage(self.driver)

    # Need this to prevent preload overlay to stop obscuring the link
    WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(MainPageLocators.PRELOAD_OVERLAY), 
                                          message="Preload overlay is still on the main tenzor page")

    link = self.driver.find_element(*MainPageLocators.ABOUT_PAGE_LINK)
    link.location_once_scrolled_into_view
    link.click()
    
    self.switch_to_window(new_page.get_url())

    return new_page