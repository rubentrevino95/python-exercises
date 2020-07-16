from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://memetees.store')

register = driver.find_element_by_xpath('//*[@id="navbarNav"]/ul[2]/li[2]/a')

register.click()

username = driver.find_element_by_xpath('//*[@id="username"]')

username.send_keys('bot')

email = driver.find_element_by_xpath('//*[@id="email"]')

email.send_keys('bot@bot.com')

password = driver.find_element_by_xpath('//*[@id="password"]')

password.send_keys('password')

submit_signup = driver.find_element_by_xpath('/html/body/div[1]/div/form/button')

submit_signup.click()

# searchBox.send_keys('pewdiepie')
#
# searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
#
# searchButton.click()