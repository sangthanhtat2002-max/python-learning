from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://aim.qa.spdigital.sg/")

wait = WebDriverWait(driver, 15)

# click login
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
).click()

# chờ input email xuất hiện
email = wait.until(
    EC.visibility_of_element_located((By.NAME, "email"))
)

email.send_keys("ironmonger-employee@singtel.com")

# password
password = wait.until(
    EC.visibility_of_element_located((By.NAME, "password"))
)

password.send_keys("Abcd1234")

wait.until(
    EC.element_to_be_clickable((By.ID,"1-submit"))
).click()