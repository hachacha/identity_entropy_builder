#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver 
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import cred as c
import random
from time import sleep

# profile is so you don't have to duo login every time
profile = FirefoxProfile(c.firefox_profile_path)

# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("--set-binary /usr/bin/chromedriver");
# driver = webdriver.Chrome(chrome_options=chrome_options)



driver = webdriver.Firefox(profile)

start_link = "https://trends.google.com/trends/trendingsearches/daily?geo=US"
region_dropdown = '//*[@id="select_1"]'
region_rand = random.randint(1,48)
countries = '/html/body/div[7]/md-select-menu/md-content/md-option['+str(region_rand)+']'
# start_link = "https://babel.hathitrust.org/cgi/ssd?id=uc1.31822037856036;page=ssd;view=plaintext;seq=2"
# next_butt = "/html/body/div[1]/div[2]/div[2]/div/p[3]/a[2]"
# alt_next_butt = "/html/body/div[1]/div[2]/div[2]/div/p/a[2]"
# text_xpath = "/html/body/div[1]/div[2]/div[2]/div/p[1]"
# title_xpath = "/html/body/div[1]/div[2]/div[2]/h2"

driver.get(start_link)
sleep(3) # it opens

# click a link on the page 
link = driver.execute_script(open("eval_list.js").read(), "arg1")
driver.get(link)
sleep(5) # page loads with ads.
# driver.execute_script(open("clickpos.js").read(), "arg1")
#click a bunch until we find something...
action = ActionChains(driver)
window_size = driver.get_window_size() #window_size.get('width')
print(window_size.get('width'))
body_width = random.randint(1,window_size.get('width'))
body_height = random.randint(1,window_size.get('height'))
print([body_width,body_height])
# start at the dang top!
action.move_to_element(driver.find_element_by_tag_name('body'))
# 60 by 60 in is a safe bet.
x_pos=60
y_pos=60
# keep moving one over and then ten down
for x in range(10):
	x_pos = x_pos+10
	try:
		action.move_by_offset(x_pos, y_pos)
	except MoveTargetOutOfBoundsException as e:
		print(e)
		x_pos = 0
		continue
	for y in range(10):
		y_pos = y_pos+10
		try:
			action.move_by_offset(x_pos, y_pos)
		except MoveTargetOutOfBoundsException as e:
			print(e)
			y_pos=0
			continue
		
		action.click().perform()
		action.send_keys(Keys.ESCAPE).perform()
		print("ok")
exit()


# action.move_to_element(driver.find_element_by_tag_name('body')).move_by_offset(body_width, body_height).click().perform()

# action.move_to_element_with_offset(el, body_width, body_height)
# action.click()
# action.perform()
# link = '/html/body/div[2]/div[2]/div/div[2]/div/div[1]/ng-include/div/div/div/div['+str(div_days)+']/md-list['+str(story_rand)+']/feed-item/ng-include/div/div/div[2]/div/a'
# driver.find_element_by_xpath(link).click()
# the_book=""
# f = open("buck.txt","a")
# first = True
# while(1):
# 	the_book += driver.find_element_by_xpath(title_xpath).text.encode(encoding='UTF-8') + "\n"
# 	the_book += driver.find_element_by_xpath(text_xpath).text.encode(encoding='UTF-8') + "\n\n"
# 	if first is True:
# 		driver.find_element_by_xpath(next_butt).click()
# 		first = False
# 	else:
# 		driver.find_element_by_xpath(alt_next_butt).click()
# 	sleep(1)
# 	f.write(the_book)
# 	the_book=""



# f.close()

