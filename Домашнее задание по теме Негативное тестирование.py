from time import sleep
import selenium; from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--headless')

driver = selenium.webdriver.Chrome(options=chrome_options )
url = ('https://www.saucedemo.com/')
driver.get(url)

login_space = driver.find_element(By.XPATH, '//input[@id="user-name"]')
password_space = driver.find_element(By.XPATH, '//input[@id="password"]')
button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')


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
    login_space.send_keys(user_name)
    password_space.send_keys(user_password)
    button_login.click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
    write_log_file("Enter to site is success\n")



entry_site('standard_user', 'secret_sauce')
log_out()
