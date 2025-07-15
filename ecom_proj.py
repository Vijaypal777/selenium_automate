from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select





chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
wait=WebDriverWait(driver, 10)

phones=wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Phones & PDAs')]")))
phones.click()

iphones=wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'iPhone')]")))
iphones.click()
iphones_img=wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='thumbnail']//child::img")))
iphones_img.click()
time.sleep(2)


img_next=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='mfp-arrow mfp-arrow-right mfp-prevent-close']")))
# img_next.click()
# img_next.click()
# img_next.click()
# img_next.click()
# img_next.click()

for i in range(5):
    img_next.click()
    time.sleep(1)

# driver.save_screenshot("screenshots/screenshot_" + str(random.randint(1, 101)) + ".png")
driver.save_screenshot("screenshots/screenshot.png")

close_img=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Close (Esc)']//self::button")))
close_img.click()


input_quantity=wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='input-quantity']")))
input_quantity.clear()
input_quantity.send_keys("2")


click_to_add_to_Cart=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='button-cart']")))
click_to_add_to_Cart.click()

laptops=wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Laptops & Notebooks')]")))
actions= ActionChains(driver)
actions.move_to_element(laptops).perform()


laptops_2=wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Show AllLaptops & Notebooks")))
laptops_2.click()

select_laptop=wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='HP LP3065']")))
select_laptop.click()

select_date=wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='input-option225']")))
select_date.clear()
select_date.send_keys("2024-12-31")

select_calender=wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-calendar']")))
select_calender.click()

# Select the date from the calendar
# Assuming you want to select December 31, 2024
# Loop until the month-year is "December 2024"
while True:
    date_picker = wait.until(EC.presence_of_element_located((By.XPATH, "//th[@class='picker-switch']")))
    if date_picker.text.strip() == "December 2024":
        break
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//th[@class='next']")))
    next_button.click()

# Select the date "31"
date_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@class='day' and text()='31']")))
date_to_select.click()
time.sleep(3)

add_to_cart=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='button-cart']")))
add_to_cart.click()


select_cart=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-loading-text='Loading...']")))
select_cart.click()



checkout=wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='text-right']/a[2]")))
checkout.click()


click_on_guest=wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='guest']")))
click_on_guest.click()

click_continue=wait.until(EC.element_to_be_clickable((By.ID, "button-account")))
click_continue.click()  
first_name=wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='input-payment-firstname']")))
first_name.clear()
first_name.send_keys("aman")
last_name=wait.until(EC.element_to_be_clickable((By.ID, "input-payment-lastname")))
last_name.clear()
last_name.send_keys("kumar")
email_name=wait.until(EC.element_to_be_clickable((By.ID, "input-payment-email")))
email_name.clear()
email_name.send_keys("aman.kumar@example.com")
telephone_num=wait.until(EC.element_to_be_clickable((By.ID, "input-payment-telephone")))
telephone_num.clear()
telephone_num.send_keys("9876543210")


address_1=wait.until(EC.element_to_be_clickable((By.ID, "input-payment-address-1")))
address_1.clear()
address_1.send_keys("123 Main St")

input_city=wait.until(EC.element_to_be_clickable((By.ID, "input-payment-city")))
input_city.clear()
input_city.send_keys("New York")    

input_postcode=wait.until(EC.element_to_be_clickable((By.ID, "input-payment-postcode")))
input_postcode.clear()
input_postcode.send_keys("10001")

# Select country
country_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "input-payment-country")))
country_dropdown.click()
country_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='United Kingdom']")))
country_option.click()

# Wait for state list to be reloaded (optional: wait for specific state)
wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='input-payment-zone']/option[text()='Bristol']")))

# Re-fetch the state dropdown after country selection
state_dropdown = wait.until(EC.presence_of_element_located((By.ID, "input-payment-zone")))

# Now select state
Select(state_dropdown).select_by_visible_text("Bristol")




click_on_continue=wait.until(EC.element_to_be_clickable((By.ID, "button-guest")))
click_on_continue.click()


clicked_to_shipping=wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='button-shipping-method']")))
clicked_to_shipping.click()


# Click to agree Terms & Conditions
agree_checkbox = wait.until(EC.element_to_be_clickable((By.NAME, "agree")))
agree_checkbox.click()

# Click continue on shipping method
click_to_continue = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='button-payment-method']//self::input")))
click_to_continue.click()

# Confirm the order
confirm_order = wait.until(EC.element_to_be_clickable((By.ID, "button-confirm")))
confirm_order.click()



time.sleep(4)
driver.quit()