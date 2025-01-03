import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

open('log.txt', 'w').close()
chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--headless')

driver = selenium.webdriver.Chrome(options=chrome_options)
url = ('http://demoqa.com/')
driver.get(url)


def write_log_file(text: str):
    with open('log.txt', 'a') as log:
        log.write(text)


def to_site_back_forward():
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[1]').click()
    driver.back();
    driver.forward()
    driver.find_element(By.XPATH, '//*[@id="item-1"]/span').click()
    driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button').click()
    assert driver.current_url == "https://demoqa.com/checkbox", write_log_file('to site back forward IS FALSE\n')
    write_log_file('to site back forward IS COOL\n')


def click_all_labels():
    [(driver.find_element(By.XPATH, f'//div[@id="tree-node"]/ol/li/ol/li[{i}]/span/label').click(),
      driver.find_element(By.XPATH, f'//*[@id="tree-node"]/ol/li/ol/li[{i}]/span/button').click())
     for i in range(1, 4)]
    ''''''''''''''''''''''''''''''
    lst = [f'{driver.find_element(By.XPATH, f'//div[@id="tree-node"]/ol/li/ol/li[{i}]/span/label').text} '
           f'{driver.find_element(By.XPATH, f'//div[@id="tree-node"]/ol/li/ol/li[{i}]/ol/li[1]/span/label')
           .text} {driver.find_element(By.XPATH, f'//div[@id="tree-node"]/ol/li/ol/li[{i}]/ol/li[2]/span/label')
           .text}' for i in range(1, 4)]
    string = ''
    for el in lst:
        string += el.lower().replace(".doc", "")
    print(string)
    ''''''''''''''''''''''''''''''


#Name_check_box.is_selected() -- Для проверки чек бокса и т. п.

def cs_to_site_b_f_click_labels():
    to_site_back_forward()
    click_all_labels()


cs_to_site_b_f_click_labels()
