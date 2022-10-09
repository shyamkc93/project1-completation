from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#log in

driver = webdriver.Firefox(executable_path="c:\webdrivers\geckodriver.exe")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("//input[@class='oxd-input oxd-input--active']").send_keys("Admin")
driver.find_element_by_xpath("//input[@class='oxd-input oxd-input--active']").send_keys("admin123")
driver.find_element_by_xpath("//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()

#PIM

driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_xpath("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
driver.find_element_by_xpath("//input[@class='oxd-input oxd-input--active orangehrm-firstname']").send_keys("Shyam")
driver.find_element_by_xpath("//input[@class='oxd-input oxd-input--active orangehrm-lastname']").send_keys("Sundar")
#driver.find_element_by_xpath("//input[@class='oxd-input oxd-input--active']").send_keys("4222")
driver.implicitly_wait(50)
Save = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
Save.click()

#Admin

Admin = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
Admin.click()
Add = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
Add.click()
ess = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
driver.find_element(By.XPATH, ess).click()
driver.find_element(By.XPATH,ess).send_keys(Keys.DOWN,Keys.DOWN,Keys.ENTER)
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys("Shyam  Sundar")
Enabled ='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]'
driver.find_element(By.XPATH, Enabled).click()
driver.find_element(By.XPATH,Enabled).send_keys(Keys.DOWN,Keys.ENTER)

#Add user name

driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys("Shyamkc")
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("Shyam@123")
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("Shyam@123")
Save = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]')
Save.click()

#search for user name

Admin = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
Admin.click()
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Shyamkc")
ess = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
driver.find_element(By.XPATH, ess).click()
driver.find_element(By.XPATH,ess).send_keys(Keys.DOWN,Keys.DOWN,Keys.ENTER)
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input').send_keys("Shyam Sundar")
Enabled ='/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
driver.find_element(By.XPATH, Enabled).click()
driver.find_element(By.XPATH,Enabled).send_keys(Keys.DOWN,Keys.ENTER)
Search = driver.find_element_by_xpath("//div[@class='oxd-form-actions']")
Search.click()
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()

# Log out and Re-login

logout = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span'
logout1 = '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'
driver.find_element(By.XPATH, logout).click()
driver.find_element(By.XPATH,logout1).send_keys(Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.ENTER)
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Shyamkc")
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("Shyam@123")
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()














