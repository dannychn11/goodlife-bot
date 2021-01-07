from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime

hour = 18
minute = 0
day = 7
slot = 2

# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.goodlifefitness.com/content/goodlife/en/book-workout.html#no-redirect')

#Click login
browser.find_element_by_class_name('c-header__login-text').click();
time.sleep(1)

# Enter credentials
browser.find_elements_by_class_name('c-field__input')[0].send_keys('MEMBER ID')
browser.find_elements_by_class_name('c-field__input')[1].send_keys("PASSWORD")

#Logging in
browser.find_element_by_class_name('c-btn-cta').click()


# Waiting for time
'''
now = datetime.datetime.now()
alarm_time = datetime.datetime.combine(now.date(), datetime.time(hour, minute, 0))
time.sleep((alarm_time - now).total_seconds())
'''

# Refreshes and clicks to the desired day
#browser.refresh()
time.sleep(20)
next_butt = browser.find_elements_by_class_name('c-icon__wrapper')[2]
for i in range(day-1):
    next_butt.click()
    time.sleep(0.1)

time.sleep(1)

# Finds the slot and books
browser.find_element_by_xpath("//div[@id='day-number-{0}']/li[{1}]/div".format(day, slot)).click()
time.sleep(1)
browser.find_element_by_class_name('c-btn-cta--chevron').click()
browser.find_element_by_id('js-workout-booking-agreement-input').click()
browser.find_element_by_class_name('c-btn-cta--chevron').click()