import pytest
from pages.sbis.main_page import MainPage as SbisMainPage

def test_first(driver):
  page = SbisMainPage(driver)
  page.open()

  page = page.go_to_contacts_page()

  page = page.go_to_tensor_main_page()
  page.should_be_current_page()
  page.should_be_card('Сила в людях')

  page = page.go_to_about_page()
  page.should_be_current_page()
  page.should_be_same_size_images()

def test_second(driver):
  default_region_title = 'Калининградская обл'

  page = SbisMainPage(driver)
  page.open()

  page = page.go_to_contacts_page()
  page.should_be_current_page()
  page.should_be_region(default_region_title)
  page.should_have_contacts()

  previous_contacts_names = page.get_contacts_names()

  new_region_title = 'Камчатский край'
  new_region_url = '41-kamchatskij-kraj'

  page.go_to_region(new_region_title)
  page.should_be_region(new_region_title, new_region_url)
  
  page.should_change_contacts(previous_contacts_names)

def test_third(driver):
  page = SbisMainPage(driver)
  page.open()

  page = page.go_to_download_page()
  page.should_be_current_page()

  filename = 'sbisplugin-setup-web.exe'
  page.change_active_tab('plugin')
  page.download_web_plugin()
  page.should_be_same_size_file(filename)