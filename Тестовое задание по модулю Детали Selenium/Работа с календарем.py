import selenium
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime

open('log.txt', 'w').close()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('--headless')

driver = selenium.webdriver.Chrome(options=chrome_options)
url = ('https://demoqa.com/date-picker')
driver.get(url)

date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
date_time = driver.find_element(By.XPATH, '//input[@id="dateAndTimePickerInput"]')

def write_log_file(text: str):
    with open('log.txt', 'a') as log:
        log.write(text)

def input_calendar():
    time_date = datetime.datetime.strptime(f'{datetime.datetime.now().strftime("%m/%d/%y_%H:%M")}',
                                           '%m/%d/%y_%H:%M')
    date_plus = (time_date + datetime.timedelta(days=10)).strftime("%m/%d/%y")
    date_plus_time = (time_date + datetime.timedelta(days=10)).strftime("%m/%d/%y %H:%M")
    date.send_keys(keys.Keys.CONTROL + 'a')
    date.send_keys(date_plus)
    date.send_keys(keys.Keys.ENTER)
    date_time.send_keys(keys.Keys.CONTROL + 'a')
    date_time.send_keys(date_plus_time)
    date_time.send_keys(keys.Keys.ENTER)

def input_validation():
    pass

def sc_input_validation_calendar():
    input_calendar()
    input_validation()

sc_input_validation_calendar()