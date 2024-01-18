from ..base_page import BasePage
from ..tenzor_locators import AboutPageLocators

from selenium.webdriver import Remote as WebDriver

class AboutPage(BasePage):

  def __init__(self, driver: WebDriver):
    url = "https://tensor.ru/about"
    super().__init__(driver, url)

  def should_be_same_size_images(self):
    images = self.driver.find_elements(*AboutPageLocators.ABOUT_IMAGE)

    assert all(image.size == images[0].size for image in images), \
      "Images are not the same size on the tenzor about page in the block 'Работаем'"