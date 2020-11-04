from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from enum import Enum

#info needed from user
Language = Enum('Language', 'English Spanish')

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
	while not (selection.isnumeric() and int(selection) in range(optionList[0], optionList[-1])):
		print("Please enter a number from %s to %s" % (optionList[0], optionList[-1]))
		selection = input()
	return int(selection)

def sendUserInput(paths, data):
	if len(paths) != len(data):
		raise ValueError("Length of paths paraeter is not equal to length of data parameter")
	

getUsersInput(Language, "language")
"""
driver = webdriver.Chrome()

driver.get("https://public.txdpsscheduler.com/")
wait = WebDriverWait(driver, 10)

#language pick
button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/button[1]')))
button.click()

DLNumberField = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[1]/div/div[1]/div/input')))
firstNameField = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[2]/div/div[1]/div/input')
lastNameField = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[3]/div/div[1]/div/input')
DOBField = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[4]/div/div[1]/div[1]/input')
SSNField = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[5]/div/div[1]/div[1]/input')

firstNameField.send_keys('Firstname')
lastNameField.send_keys('Lastname')
DOBField.send_keys('05/12/1985')
SSNField.send_keys('1234')

logonButton = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[4]/button')
logonButton.click()

newAppointmentButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/div[2]/div/button')))
newAppointmentButton.click()

applyButton = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section/div/main/div/section/div[2]/div/main/div/div/div[1]/div[1]/button')))
applyButton.click()

emailField = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[1]/div/div[5]/div/div/div/div[1]/div/input')))
confirmEmailField = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[1]/div/div[6]/div/div/div/div[1]/div/input')
zipCodeField = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[2]/div[1]/div[4]/div[1]/div/div/div[1]/div/input')

emailField.send_keys('test@gmail.com')
confirmEmailField.send_keys('test@gmail.com')
zipCodeField.send_keys('78759')

nextButton = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[2]/div[2]/div/div[2]/button')
nextButton.click()

datePaths = []

datePaths.append('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div[3]/table/tbody/tr/td[2]/div/div[1]/div/div[2]')
datePaths.append('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div[3]/table/tbody/tr/td[2]/div/div[2]/div/div[2]')
datePaths.append('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div[3]/table/tbody/tr/td[2]/div/div[3]/div/div[2]')
datePaths.append('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div[3]/table/tbody/tr/td[2]/div/div[4]/div/div[2]')
datePaths.append('/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div[3]/table/tbody/tr/td[2]/div/div[5]/div/div[2]')

temp = wait.until(EC.presence_of_element_located((By.XPATH, datePaths[0])))
for path in datePaths:
	el = driver.find_element_by_xpath(path)
	print(el.text)

time.sleep(4)
driver.quit()
"""