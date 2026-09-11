import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """Initializes Chrome WebDriver with automated path setups."""
    options = webdriver.ChromeOptions()
    # Optional: Disables automation extensions and banners
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    yield driver

    driver.quit()
