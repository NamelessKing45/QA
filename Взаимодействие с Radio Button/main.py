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
    assert driver.current_url == "https://demoqa.com/radio-button", write_log_file('to site IS FALSE\n')
    write_log_file('to site IS COOL\n')


def click_radio_button_and_it_inti_n():
    radio_button = driver.find_element(By.XPATH, '//div[2]/label[@class="custom-control-label"]')
    radio_button.click()
    if radio_button.is_selected():write_log_file('Radio button IS ON\n')
    else:write_log_file('Radio button IS OFF\n')

def sc_to_site_click_r_button_inti_n():
    to_site()
    click_radio_button_and_it_inti_n()\

sc_to_site_click_r_button_inti_n()