from selenium import webdriver
from selenium.webdriver.common.by import By
import time

seconds_to_run = 300


def run_game_bot(time_amount):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    driver.get('https://orteil.dashnet.org/experiments/cookie/')

    cookie = driver.find_element(By.CSS_SELECTOR, '#cookie')

    time_to_stop = time.time() + time_amount

    check_time = time.time() + 5

    interval = 6

    items = driver.find_elements(By.CSS_SELECTOR, '#store div')
    item_ids = [item.get_attribute('id') for item in items]

    # GAME LOOP
    while time_to_stop >= time.time():
        cookie.click()

        if time.time() >= check_time:
            all_prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
            item_prices = []

            for price in all_prices:
                element_text = price.get_attribute('innerText')
                if element_text != '':
                    cost = int(element_text.split('-')[1].strip().replace(',', ''))
                    item_prices.append(cost)

            cookie_upgrades = {}
            for n in range(len(item_prices)):
                cookie_upgrades[item_prices[n]] = item_ids[n]

            money_element = driver.find_element(By.CSS_SELECTOR, '#money').get_attribute('innerText')
            if ',' in money_element:
                money_element = money_element.replace(',', '')
            money = int(money_element)

            affordable_upgrades = {}
            for cost, id in cookie_upgrades.items():
                if money > cost:
                    affordable_upgrades[cost] = id

            max_affordable_upgrade = max(affordable_upgrades)
            print(max_affordable_upgrade)
            to_purchase_id = affordable_upgrades[max_affordable_upgrade]

            driver.find_element(By.ID, to_purchase_id).click()

            check_time += interval
            if interval == 6:
                interval = 2
            else:
                interval = 6
    print(driver.find_element(By.CSS_SELECTOR, '#cps').get_attribute('innerText'))
    driver.quit()


run_game_bot(seconds_to_run)

