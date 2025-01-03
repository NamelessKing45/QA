import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

open('log.txt', 'w').close()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('--headless')

driver = selenium.webdriver.Chrome(options=chrome_options)
url = ('http://demoqa.com/')
driver.get(url)


def write_log_file(text: str):
    with open('log.txt', 'a') as log:
        log.write(text)


def to_site():
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[1]').click()
    driver.find_element(By.XPATH, '//*[@id="item-1"]/span').click()
    driver.find_element(By.XPATH, '//*[@id="item-2"]').click()
    assert driver.current_url == "https://demoqa.com/checkbox", write_log_file('to site IS FALSE\n')
    write_log_file('to site IS COOL\n')


to_site()