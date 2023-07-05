from selenium.webdriver.common.by import By


class Auth:
    user_name = (By.XPATH, '//input[@id="user-name"]')
    password = (By.XPATH, '//input[@id="password"]')
    error_auth = (By.CSS_SELECTOR, '.error-message-container.error')
    login_button = (By.XPATH, '//input[@id="login-button"]')
