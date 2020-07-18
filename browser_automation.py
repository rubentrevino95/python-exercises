from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://memetees.store')

# SIGN UP

# register = driver.find_element_by_xpath('//*[@id="navbarNav"]/ul[2]/li[2]/a')
#
# register.click()
#
# username = driver.find_element_by_xpath('//*[@id="username"]')
#
# username.send_keys('bot')
#
# email = driver.find_element_by_xpath('//*[@id="email"]')
#
# email.send_keys('bot@bot.com')
#
# password = driver.find_element_by_xpath('//*[@id="password"]')
#
# password.send_keys('password')
#
# submit_signup = driver.find_element_by_xpath('/html/body/div[1]/div/form/button')
#
# submit_signup.click()

product = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a')

product.click()

color = driver.find_element_by_xpath('//*[@id="productContainer"]/div[5]/form/div[1]/div/ul/li[2]/label/span')

color.click()

size = driver.find_element_by_xpath('//*[@id="sizeSelect"]/option[4]')

size.click()

quant = driver.find_element_by_xpath('//*[@id="amountOrdered"]')

quant.send_keys('3')

addToCart = driver.find_element_by_xpath('//*[@id="addProduct"]')

addToCart.click()

logIn_username = driver.find_element_by_xpath('//*[@id="username"]')

logIn_username.send_keys('bot2')

logIn_password = driver.find_element_by_xpath('//*[@id="password"]')

logIn_password.send_keys('password')

logIn = driver.find_element_by_xpath('/html/body/div[1]/div/form/button')

logIn.click()

cont_checkout = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/button')

cont_checkout.click()


# BILLING

bill_firstname = driver.find_element_by_xpath('//*[@id="Bfirst_name"]')

bill_firstname.clear()

bill_firstname.send_keys('bot')

bill_lastname = driver.find_element_by_xpath('//*[@id="Blast_name"]')

bill_lastname.clear()

bill_lastname.send_keys('doe')

bill_address = driver.find_element_by_xpath('//*[@id="Baddress1"]')

bill_address.clear()

bill_address.send_keys('1000 bot street')

bill_city = driver.find_element_by_xpath('//*[@id="Bcity"]')

bill_city.clear()

bill_city.send_keys('bot antonio')

bill_state = driver.find_element_by_xpath('//*[@id="Bstate"]')

bill_state.clear()

bill_state.send_keys('bot york')

bill_zip = driver.find_element_by_xpath('//*[@id="Bzip"]')

bill_zip.clear()

bill_zip.send_keys('1000')

# SHIPPING

ship_firstname = driver.find_element_by_xpath('//*[@id="Sfirst_name"]')

ship_firstname.clear()

ship_firstname.send_keys('bot')

ship_lastname = driver.find_element_by_xpath('//*[@id="Slast_name"]')

ship_lastname.clear()

ship_lastname.send_keys('doe')

ship_address = driver.find_element_by_xpath('//*[@id="Saddress1"]')

ship_address.clear()

ship_address.send_keys('1000 bot street')

ship_city = driver.find_element_by_xpath('//*[@id="Scity"]')

ship_city.clear()

ship_city.send_keys('bot antonio')

ship_state = driver.find_element_by_xpath('//*[@id="Sstate"]')

ship_state.clear()

ship_state.send_keys('bot york')

ship_zip = driver.find_element_by_xpath('//*[@id="Szip"]')

ship_zip.clear()

ship_zip.send_keys('1000')


checkout = driver.find_element_by_xpath('//*[@id="AddressSubmit"]')

checkout.click()

enter_pay = driver.find_element_by_xpath('//*[@id="checkout-btn"]')

enter_pay.click()

card_number = driver.find_element_by_xpath('//*[@id="card-element"]/div/iframe')

card_number.click()

card_number.send_keys('424242424242424242424242424')

pay = driver.find_element_by_xpath('//*[@id="submitButton"]')

pay.click()





