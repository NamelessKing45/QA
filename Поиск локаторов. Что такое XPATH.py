from selenium import webdriver; from time import sleep; from selenium.webdriver.common.by import By

#1 Задание
driver = webdriver.Chrome()
driver.get('https://www.lambdatest.com/selenium-playground/simple-form-demo')

box_text = driver.find_element(By.XPATH, '//*[@id="user-message"]')
box_text.send_keys("1263")

#2 Задание
driver.execute_script("window.open('about:blank','second_link')\
"); driver.switch_to.window("second_link");driver.get('https://www.lambdatest.com/selenium-playground/checkbox-demo')

button_answer = driver.find_element(By.XPATH, '//*[@value="Check All"]')
button_answer.click()

#3 Задание
driver.execute_script("window.open('about:blank','third_link')\
"); driver.switch_to.window("third_link"); driver.get('https://www.lambdatest.com/selenium-playground/checkbox-demo')

div_answer = driver.find_element(By.XPATH, '//div[@class="mt-50 rounded w-full"][2]')

#4 Задание
driver.execute_script("window.open('about:blank', 'four_link')\
"); driver.switch_to.window('four_link')
driver.get('https://www.lambdatest.com/selenium-playground/table-data-download-demo')

button_copy = driver.find_element(By.XPATH, '//*[@id="example_wrapper"]/div[1]/a[1]')
button_copy.click()

sleep(15)
