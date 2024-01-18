from selenium.webdriver import Remote as WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
  driver = None
  url = None

  def __init__(self, driver: WebDriver, url=''):
    self.driver = driver
    self.url = url
    self.set_wait()

  def open(self):
    self.driver.get(self.url)
    self.load_fully_page()

  def get_url(self):
    return self.url

  def switch_to_window(self, new_url):
    for handle in self.driver.window_handles:
      self.driver.switch_to.window(handle)
      current_url = self.driver.current_url
      if (new_url in current_url):
        self.load_fully_page()
        return
    
    raise Exception(f"No window with this url: {new_url}")

  def set_wait(self, timeout=5):
    self.driver.implicitly_wait(timeout)

  def should_be_current_page(self):
    assert self.url in self.driver.current_url, \
      f"Current page should be {self.url} instead of {self.driver.current_url}"
    
  def should_contain_url(self, url_part):
    WebDriverWait(self.driver, 3).until(EC.url_contains(url_part), 
                                        message=f"Current page url expected to contain {url_part}, got {self.driver.current_url}")
    
  def is_element_present(self, by, selector):
    try:
        self.driver.find_element(by, selector)
    except (NoSuchElementException):
        return False
    return True
  
  def should_contain_page_title(self, title_part):
    WebDriverWait(self.driver, 3).until(EC.title_contains(title_part), 
                                        message=f"Page title expected to contain {title_part}, got {self.driver.title}")

  ''' method to prevent lazy loading '''
  def load_fully_page(self):
  
    if not self.is_page_fully_loaded():
      self.scroll_page_to_end()

    self.scroll_page_to_top()

  def is_page_fully_loaded(self):
    return self.driver.execute_script("return document.readyState === 'complete';")

  def scroll_page_to_end(self):
    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  def scroll_page_to_top(self):
    self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")