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
container = []
container_2 = []

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

def letters(text):
    return ''.join([c for c in text if c.isalpha()])

def add_recycle_bin():
    for i in range(1,1000):
        try:
            driver.find_element(By.XPATH, f'//div[{i}]/div[2]/div[2]/button').click()
            container.append(letters(driver.find_element(
                By.XPATH, f'//div[{i}]/div[2]/div[@class="inventory_item_label"]').text))
        except:
            assert len(container) == i-1, write_log_file("Add elements to bin IS FALSE\n")
            write_log_file("Add elements to bin IS COOL\n")
            break

def open_bin_site_and_url_verification():
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    assert driver.current_url == 'https://www.saucedemo.com/cart.html', (
        write_log_file("Enter to site(RECYCLE BIN) is FALSE\n"))
    write_log_file("Enter to site(RECYCLE BIN) is success\n")

def remove_recycle_bin():
    text_div = letters(driver.find_element(By.XPATH, f'//div[1]/div[{3}]/div[2]/a').text +
                                           driver.find_element(By.XPATH, f'//div[1]/div[{3}]/div[2]/div[1]').text)
    container.remove(text_div)
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
    driver.refresh()
    for i in range(3,1000):
        try:
            container_2.append(letters(driver.find_element(By.XPATH, f'//div[1]/div[{i}]/div[2]/a').text +
                                       driver.find_element(By.XPATH, f'//div[1]/div[{i}]/div[2]/div[1]').text))
        except:break;pass
    assert container_2 == container, write_log_file("Remove elements to bin IS FALSE\n")
    write_log_file("Remove elements to bin IS COOL\n")

def open_your_information_and_url_verification():
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    assert driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html', (
        write_log_file("Enter to site(YOUR INFORMATION STEP ONE) is FALSE\n"))
    write_log_file("Enter to site(YOUR INFORMATION STEP ONE) is success\n")

def swag_labs_and_url_verification(first_name:str, last_name:str, zip_pst_code:str):
    driver.find_element(By.XPATH, '//div/div[1]/input').send_keys(first_name)
    driver.find_element(By.XPATH, '//div/div[2]/input').send_keys(last_name)
    driver.find_element(By.XPATH, '//div/div[3]/input').send_keys(zip_pst_code)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    assert driver.current_url == 'https://www.saucedemo.com/checkout-step-two.html', (
        write_log_file("Enter to site(YOUR INFORMATION STEP TWO) is FALSE\n"))
    write_log_file("Enter to site(YOUR INFORMATION STEP TWO) is success\n")
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()

def final_tabs_and_url_verification_text_verification():
    assert driver.current_url == 'https://www.saucedemo.com/checkout-complete.html', (
        write_log_file("Enter to site(FINAL TABS) is FALSE\n"))
    write_log_file("Enter to site(FINAL TABS) is success\n")
    assert (driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2').text ==
            'Thank you for your order!'), (
        write_log_file("Text to site(FINAL TABS) is FALSE\n"))
    write_log_file("Text to site(FINAL TABS) is success\n")

def sc_login_logout():
    entry_site('standard_user', 'secret_sauce')
    log_out()

def sc_login_add_rem_bin_logout():
    entry_site('standard_user', 'secret_sauce')
    add_recycle_bin()
    open_bin_site_and_url_verification()
    remove_recycle_bin()
    open_your_information_and_url_verification()
    swag_labs_and_url_verification('111', '111', '111')
    final_tabs_and_url_verification_text_verification()
    log_out()

sc_login_add_rem_bin_logout()