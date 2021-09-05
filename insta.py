from selenium import webdriver
from time import sleep
from secrets import username as un, password as pw, email
driver = webdriver.Chrome('/home/s0umyajit/Downloads/chromedriver')
driver.get('https://www.instagram.com/')

sleep(4)
username = driver.find_element_by_xpath('//input[@name="username"]')
username.send_keys(email)

password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys(pw)
sleep(2)

login = driver.find_element_by_xpath('//button[@type="submit"]')
login.click()
sleep(7)

not_now = driver.find_element_by_class_name("HoLwm")
not_now.click()
profile = driver.find_element_by_xpath('//a[@href="/{}/"]'.format(un))
profile.click()
sleep(4)

# Finding Followers
driver.find_element_by_xpath('//a[@href="/{}/followers/"]'.format(un)).click()
sleep(3)
scrollbar = driver.find_element_by_class_name("isgrP")
popup = driver.find_element_by_class_name("jSC57")
for i in range(15):
    driver.execute_script("arguments[0].scrollBy(0,2500)", scrollbar)
    sleep(2)

followers = []
links = popup.find_elements_by_tag_name('a')
for i in links:
    x = i.text
    if x != '':
        followers.append(x)
print(len(followers))
sleep(3)

driver.execute_script("window.location.reload()")
sleep(5)


# Finding Following
driver.find_element_by_xpath('//a[@href="/{}/following/"]'.format(un)).click()
sleep(5)
scrollbar = driver.find_element_by_class_name("isgrP")
popup = driver.find_element_by_class_name("jSC57")
for i in range(18):
    driver.execute_script("arguments[0].scrollBy(0,2500)", scrollbar)
    sleep(2)

following = []
links = popup.find_elements_by_tag_name('a')
for i in links:
    x = i.text
    if x != '':
        following.append(x)
print(len(following))
driver.close()

not_following = []
for i in following:
    if i in followers:
        continue
    else:
        not_following.append(i)
print(not_following)