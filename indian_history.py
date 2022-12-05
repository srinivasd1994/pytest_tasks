from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
print("Starting on the earth") 
driver = webdriver.Chrome()  
driver.maximize_window()  
driver.get("https://www.google.com/")  
time.sleep(2)
# driver.find_element(By.XPATH,"//button[@class = 'M6CB1c rr4y5c']").send_keys(Keys.ENTER)
# time.sleep(3)
driver.find_element(By.NAME,"q").send_keys("Indian history 1947")
time.sleep(3) 

driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element(By.XPATH,"//h3[contains(text(),'History of India (1947–present) - Wikipedia')]").click()
time.sleep(1) 
driver.find_element(By.XPATH,"//div[@id='siteSub']").click()

driver.close()  
print("landed on the moon ")  