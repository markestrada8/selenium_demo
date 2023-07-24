from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# AMAZON
# PRODUCT_URL = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
# driver.get(PRODUCT_URL)
# price = driver.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen")
# print("price: ", price.get_attribute('innerText'))

# PYTHON.ORG
PYTHON_URL = "https://www.python.org"
driver.get(PYTHON_URL)
# docs_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
# print(docs_link.get_attribute('href'))
#
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute('innerText'))

# EXERCISE
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul a')
# times = [item.get_attribute('innerText') for item in event_times]
# names = [item.get_attribute('innerText') for item in event_names]
# for i in range(len(names)):
#     event_data[i] = {'time': times[i], 'name': names[i]}

event_data = {
    i: {
        'time': event_times[i].get_attribute('innerText'),
        'name': event_names[i].get_attribute('innerText')
    }
    for i in range(len(event_names))
}

print(event_data)

driver.quit()
