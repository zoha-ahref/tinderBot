from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


driver_path = "your/driver/path"
driver = webdriver.Chrome(executable_path=driver_path)

FB_EMAIL = "youremail@email.com"
FB_PASSWORD = "your_password"



driver.get("http://www.tinder.com")

time.sleep(5)
print(driver.title)

log_in = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span')

log_in.click()
time.sleep(5)
fb_login = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
fb_login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_name("email")
email.send_keys(FB_EMAIL)
password = driver.find_element_by_name("pass")
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)

click_allow_loc = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')

click_allow_loc.click()
time.sleep(2)
enable_not = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
enable_not.click()
time.sleep(2)
click_accept = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
click_accept.click()


for n in range(100):
    time.sleep(2)
    try:
        print("called")
        #can be changes to like by providing xpath for like button
        hit_dislike = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]')
        hit_dislike.click()


    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(3)
driver.quit()



