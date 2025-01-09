import selenium
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


open('log.txt', 'w').close()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('--headless')

driver = selenium.webdriver.Chrome(options=chrome_options)
url = ('https://html5css.ru/howto/howto_js_rangeslider.php')
driver.get(url)
action = ActionChains(driver)

def write_log_file(text: str):
    with open('log.txt', 'a') as log:
        log.write(text)

def sliders():
    slider = driver.find_element(By.XPATH, '//input[@id="id2"]')
    sleep(1)
    action.click_and_hold(slider).move_by_offset(-300, 10).perform()

sliders()