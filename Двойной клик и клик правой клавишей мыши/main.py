import selenium; from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

open('log.txt', 'w').close()
chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--headless')

driver = selenium.webdriver.Chrome(options=chrome_options )
url = 'https://demoqa.com/buttons'
driver.get(url)

def write_log_file(text: str):
    with open('log.txt', 'a') as log:
        log.write(text)

def click_three_button():
    native_text = 'You have done a double click You have done a right click You have done a dynamic click'
    text_label = ''
    button_double_click = driver.find_element(By.XPATH, '//button[@Id="doubleClickBtn"]')
    button_right_click = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
    button_click = driver.find_element(By.XPATH, '//div[3]/button')
    action = ActionChains(driver)
    action.double_click(button_double_click).perform()
    action.context_click(button_right_click).perform()
    button_click.click()
    text_label += (f'{driver.find_element(By.XPATH, '//p[@id][1]').text} '
                   f'{driver.find_element(By.XPATH, '//p[@id][2]').text} '
                   f'{driver.find_element(By.XPATH, '//p[@id][3]').text}')
    assert native_text == text_label, write_log_file("click three button IS FALSE")
    write_log_file("click three button IS OK")

click_three_button()