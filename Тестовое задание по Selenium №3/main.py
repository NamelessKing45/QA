import selenium; from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options; import datetime


chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--headless')

driver = selenium.webdriver.Chrome(options=chrome_options )
url = ('https://www.saucedemo.com/')
driver.get(url)

num_rs = []
conte_r = []

def entry_site(user_name:str, user_password:str):
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys(user_name)
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(user_password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.save_screenshot(f'screenshots_entry_site\\'
                           f'{datetime.datetime.now().strftime('Time_%H.%M.%S_Data_%d.%m.%y')}.png')

def print_text_product():
    for i in range(1,1000):
        num_rs.append(i)
        try:
            print(f'{i}) {driver.find_element(
                By.XPATH, f'//div[{i}]/div[2]/div[@class="inventory_item_label"]').text}\n')
        except:break

def add_bin(i):
    product_text = driver.find_element(By.XPATH, f'//div[{i}]/div[2]/div[@class="inventory_item_label"]')
    product_button = driver.find_element(By.XPATH, f'//div[{i}]/div[2]/div[2]/button')
    product_button.click()
    conte_r.append(f'{i}) {product_text.text}')

def open_bin_site():
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

def swag_labs(first_name:str, last_name:str, zip_pst_code:str):
    driver.find_element(By.XPATH, '//div/div[1]/input').send_keys(first_name)
    driver.find_element(By.XPATH, '//div/div[2]/input').send_keys(last_name)
    driver.find_element(By.XPATH, '//div/div[3]/input').send_keys(zip_pst_code)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    print(f'Информация по заказу:\n\n{driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]').text}\n')
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    print(driver.find_element(By.XPATH,'//*[@id="checkout_complete_container"]').
          text.replace("Back Home", ""))

def console():
    if input("Вы хотите войти в систему?   ") in 'ДАдаДадАYESyeYEPyepyes':
        entry_site('standard_user', 'secret_sauce')
        print("Вы вошли в аккаунт!\n")
        print("Какие товары вы хотите купить?\n")
        print_text_product()
        print(1 in num_rs)
        save_input = []
        while True:
            integer = int(input('выберите соответствующую цифру товара, что бы добавить его в корзину.\n'
                             'Если вы выбрали все товары введите цифру 0!\n'))
            if integer not in save_input:
                if integer in num_rs:
                    add_bin(integer);print(f"Товар {integer} успешно добавлен!\n")
                    save_input.append(integer)
                if integer == 0:
                    open_bin_site()
                    print('Вы добавили в корзину:')
                    for i in conte_r:
                        print(f'{i}\n')
                    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
                    first_name = input("Для завершения заказа введите свои контактные данные\n"
                                       "1) Имя   ")
                    last_name = input("2) Фамилия   ")
                    zip_pst_code = str(input("ZIP CODE   "))
                    swag_labs(first_name,last_name,zip_pst_code)
                    break
                if integer not in num_rs:print('Невозможно выбрать данный товар!\n')
            else:print("Данный товар уже добавлен в корзину!\n")
    else:print("Gog Bye!")

console()

