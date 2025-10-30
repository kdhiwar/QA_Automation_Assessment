import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup():
    """Setup Chrome WebDriver."""
    options = Options()
    options.add_argument("--headless")  # remove this line if you want to see the browser
    driver = webdriver.Chrome(options=options)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    yield driver
    driver.quit()

def test_radio_buttons(setup):
    """Validate radio buttons are clickable."""
    radios = setup.find_elements(By.CSS_SELECTOR, "input[type='radio']")
    for radio in radios:
        radio.click()
        assert radio.is_selected()

def test_dropdown_selection(setup):
    """Validate dropdown selection works correctly."""
    dropdown = Select(setup.find_element(By.ID, "dropdown-class-example"))
    dropdown.select_by_visible_text("Option2")
    assert dropdown.first_selected_option.text == "Option2"
