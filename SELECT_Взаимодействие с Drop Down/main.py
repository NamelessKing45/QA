from selenium.webdriver.support.ui import Select
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('--headless')

driver = selenium.webdriver.Chrome(options=chrome_options)
url = ('')
driver.get(url)


dropdown = Select(driver.find_element(By.XPATH, '////////////'))
dropdown.select_by_visible_text('drop-down') # Текст выпадающей кнопки