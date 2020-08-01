from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.supremenewyork.com/shop/all')

product = driver.find_element_by_xpath('//*[@id="container"]/li[73]/div/a')

product.click()

size = driver.find_element_by_xpath('//*[@id="s"]')

size.click()

size_choice = driver.find_element_by_xpath('//*[@id="s"]/option[3]')

size_choice.click()

add_cart = driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input')

add_cart.click()

checkout_now = driver.find_element_by_xpath('//*[@id="cart"]/a[2]')

checkout_now.click()

# billing
b_name = driver.find_element_by_xpath('//*[@id="order_billing_name"]')

b_name.send_keys('First Last')

b_email = driver.find_element_by_xpath('//*[@id="order_email"]')

b_email.send_keys('name@gmail.com')

b_tele = driver.find_element_by_xpath('//*[@id="order_tel"]')

b_tele.send_keys('2100000000')

b_address = driver.find_element_by_xpath('//*[@id="bo"]')

b_address.send_keys('1000 bot lane')

b_zip = driver.find_element_by_xpath('//*[@id="order_billing_zip"]')

b_zip.send_keys('10000')


# card

c_num = driver.find_element_by_xpath('//*[@id="rnsnckrn"]')

c_num.send_keys('2424242424242424')

c_month = driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[8]')

c_month.click()

c_year = driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[3]')

c_year.click()

terms = driver.find_element_by_xpath('//*[@id="order_terms"]')

terms.click()

process_pay = driver.find_element_by_xpath('//*[@id="pay"]/input')

process_pay.click()