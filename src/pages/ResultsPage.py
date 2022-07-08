from seleniumpagefactory.Pagefactory import PageFactory


class ResultsPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'more_results_button': ('CSS', ".result--more__btn"),
        'page_number_label': ('CSS', ".result__pagenum")
    }