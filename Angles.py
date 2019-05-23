import serial
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
 A robotic rover arm is connected to an arduino which reads the angles of its joints.
 These angles are then outputted by the arduino which is then read by this program.
 The angles are then pasted on the online text editor
"""

ser = serial.Serial('COM4', 9600, timeout=1)    # Allows for serial communication with an arduino

time.sleep(3)

driver = webdriver.Chrome()

driver.get('https://www.protectedtext.com/')

site_search = driver.find_element_by_id("siteToVisit")
site_search.send_keys('ArduinoTest')
site_search.send_keys(Keys.ENTER)

password = driver.find_element_by_id("enterpassword")
password.send_keys('pass')
password.send_keys(Keys.ENTER)

text_area = driver.find_element_by_class_name("textarea-contents")
save = driver.find_element_by_id("button-save")

while True:

	# Reads serial output from arduino and sends it to the textfield

	for i in range(10):
		angles = str(ser.readline())
		angles = angles.split("b'")[1]
		angles_1 = angles.split("'")[0]
		angles_1 = angles_1.split("\\")[0]
		angles_2 = angles.split("'")[1]
		angles_2 = angles_2.split("\\")[0]
		text_area.send_keys(angles_1)
		text_area.send_keys(Keys.ENTER)
		text_area.send_keys(angles_2)

	save.click()    # Saves the current text so that it can be read from another device
	time.sleep(0.2)
	text_area.clear()   # Clears the text to make room for another batch of angle outputs
	time.sleep(0.5)




