from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://kanye2020.country/')

first = driver.find_element_by_xpath('//*[@id="firstname"]')

first.send_keys('bot')

last = driver.find_element_by_xpath('//*[@id="lastname"]')

last.send_keys('botter')

addy = driver.find_element_by_xpath('//*[@id="address"]')

addy.send_keys('1000 bot lane')

city = driver.find_element_by_xpath('//*[@id="city"]')

city.send_keys('south carolina')

zip = driver.find_element_by_xpath('//*[@id="zip"]')

zip.send_keys('30000')

county = driver.find_element_by_xpath('//*[@id="county"]')

county.click()

count_option = driver.find_element_by_xpath('//*[@id="county"]/option[2]')

count_option.click()

birth = driver.find_element_by_xpath('//*[@id="dob"]')

birth.send_keys('07221995')

email = driver.find_element_by_xpath('//*[@id="email"]')

email.send_keys('bot@yahoo.com')

phone = driver.find_element_by_xpath('//*[@id="phone"]')

phone.send_keys('3030000000')

sign = driver.find_element_by_xpath('/html/body/form/div/div[11]/button')

sign.click()
