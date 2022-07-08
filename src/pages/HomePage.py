from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory


class HomePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    locators = {
        'search_bar': ('CSS', "#search_form_input_homepage")
    }

    def search_query(self, query):
        self.search_bar.set_text(query)
        self.search_bar.send_keys(Keys.RETURN)
