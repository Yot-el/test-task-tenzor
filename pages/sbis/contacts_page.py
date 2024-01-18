from ..base_page import BasePage
from ..tenzor.main_page import MainPage
from ..sbis_locators import ContactsPageLocators

from selenium.webdriver import Remote as WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ContactsPage(BasePage):
  def __init__(self, driver: WebDriver):
    url = "https://sbis.ru/contacts"
    super().__init__(driver, url)

  def go_to_tensor_main_page(self):
    new_page = MainPage(self.driver)
    self.driver.find_element(*ContactsPageLocators.TENSOR_LINK_LOGO).click()
    self.switch_to_window(new_page.get_url())

    return new_page
  
  def go_to_region(self, region_title):
    region_selector = f'//span[contains(@class, "sbis_ru-link") and contains(text(), "{region_title}")]'
    self.driver.find_element(*ContactsPageLocators.REGION_TITLE).click()

    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ContactsPageLocators.REGION_PANEL),
                                        "Region choose panel on contacts didn't appear in 10 seconds")

    self.driver.find_element(By.XPATH, region_selector).click()
  
  def get_contacts_names(self):
    contacts_names = self.driver.find_elements(*ContactsPageLocators.CONTACTS_NAME)

    return list(map(lambda name: name.text, contacts_names))
  
  def should_have_contacts(self):
    contacts_items = self.driver.find_elements(*ContactsPageLocators.CONTACTS_ITEM)

    assert len(contacts_items) != 0, \
      "Contacts list expected to contain items, got 0"
    
  def should_change_contacts(self, previous_contacts_names):
    contacts_names = self.get_contacts_names()

    assert len(set(contacts_names) - set(previous_contacts_names)) > 0, \
      "Contacts on contacts page have not been changed"
  
  def should_be_region(self, title, url=''):
    self.should_contain_page_title(title)
    self.should_be_region_title(title)
    self.should_contain_url(url)

  def should_be_region_title(self, title):
    region_title = self.driver.find_element(*ContactsPageLocators.REGION_TITLE)
    assert title in region_title.text, \
      f"Region title on contacts page expected to contain {title}, got {region_title.text}"