import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from locators.locators import Auth


base_url = 'https://www.saucedemo.com'

service = Service(
    executable_path=r'F:\Dev\selenium_python\chrome_driver\chromedriver.exe'
)

users_list = [
    'standard_user',
    'locked_out_user',
    'problem_user',
    'performance_glitch_user'
]

with webdriver.Chrome(service=service) as driver:

    try:
        driver.get(url=base_url)

        user_name = driver.find_element(Auth.user_name)
        user_name.send_keys(f'{random.choice(users_list)}')

        password = driver.find_element(Auth.password)
        password.send_keys('secret_sauce')

        login_button = driver.find_element(Auth.login_button)
        login_button.click()

        time.sleep(3)
    except Exception as exeption:
        print(exeption)
    finally:
        driver.close()
        driver.quit()
