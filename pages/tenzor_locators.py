from selenium.webdriver.common.by import By

class MainPageLocators():
  ABOUT_PAGE_LINK = (By.CSS_SELECTOR, 'a.tensor_ru-link[href="/about"]')
  PRELOAD_OVERLAY = (By.CSS_SELECTOR, 'div.preload-overlay')

class AboutPageLocators():
  ABOUT_IMAGE = (By.CSS_SELECTOR, '.tensor_ru-About__block3-image-wrapper')