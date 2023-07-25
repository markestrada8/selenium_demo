from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# TO KEEP BROWSER OPEN
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

# WIKIPEDIA
# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# print(count.get_attribute('innerText'))
# count.click()

# featured_link = driver.find_element(By.LINK_TEXT, 'American logistics in the Normandy campaign')
# featured_link.click()

# search = driver.find_element(By.NAME, 'search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)

# NEWSLETTER
driver.get('http://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys('Test')
last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys('User')
email = driver.find_element(By.NAME, 'email')
email.send_keys('TestUser@email.com')
button = driver.find_element(By.CSS_SELECTOR, '.btn')
button.click()
# driver.quit()