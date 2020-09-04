from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from enum import Enum

#info needed from user
Language = Enum('Language', 'English Spanish')
#language = input('Pick a language: ')

#function to get user's selection for different data
#returns the selection as integer
def getUsersInput(dataEnum, enumName):
	#display header and options options
	print("Select a %s by entering a number:" % enumName)
	for case in dataEnum:
		print("%s. %s " % (case.value, case.name))
	#get user's selection
	optionList = [case.value for case in dataEnum]
	selection = input()
	while not selection.isnumeric():
		print("Please enter a number from %s to %s" % (optionList[0], optionList[-1]))
		selection = input()
		print(int(selection))



getUsersInput(Language, "language")

#driver = webdriver.Chrome()

#driver.get("https://public.txdpsscheduler.com/")
#driver.quit()