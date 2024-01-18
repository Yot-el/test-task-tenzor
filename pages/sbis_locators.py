from selenium.webdriver.common.by import By

class MainPageLocators():
  CONTACTS_PAGE_LINK = (By.CSS_SELECTOR, 'a.sbisru-Header__menu-link[href="/contacts"]')
  DOWNLOAD_PAGE_LINK = (By.XPATH, '//a[@class="sbisru-Footer__link" and text()="Скачать СБИС"]')

class ContactsPageLocators():
  TENSOR_LINK_LOGO = (By.CSS_SELECTOR, 'a.sbisru-Contacts__logo-tensor')
  REGION_TITLE = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text')
  REGION_PANEL = (By.CSS_SELECTOR, '.sbis_ru-Region-Panel') 
  CONTACTS_ITEM = (By.CSS_SELECTOR, '.sbisru-Contacts-List__item')
  CONTACTS_NAME = (By.CSS_SELECTOR, '.sbisru-Contacts-List__name')

class DownloadPageLocators():
  ACTIVE_TAB = (By.CSS_SELECTOR, '.ws-SwitchableArea__item.ws-has-focus')
  DOWNLOAD_PLUGIN_LINK = (By.CSS_SELECTOR, 'a.sbis_ru-DownloadNew-loadLink__link[href*="sbisplugin-setup-web"]')