from time import sleep
import selenium; from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options; import datetime

open('log.txt', 'w').close()
chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--headless')

driver = selenium.webdriver.Chrome(options=chrome_options )
url = ('https://www.saucedemo.com/')
driver.get(url)

def write_log_file(text:str):
    with open('log.txt', 'a') as log:
        log.write(text)

def log_out():
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    assert driver.current_url == url
    write_log_file('Out to site is success\n')

def entry_site(user_name:str, user_password:str):
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys(user_name)
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(user_password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.save_screenshot(f'screenshots_entry_site\\'
                           f'{datetime.datetime.now().strftime('Time_%H.%M.%S_Data_%d.%m.%y')}.png')
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html',\
        write_log_file("Enter to site is FALSE\n")
    write_log_file("Enter to site is success\n")


def st_login_logout():
    entry_site('standard_user', 'secret_sauce')
    log_out()

st_login_logout()