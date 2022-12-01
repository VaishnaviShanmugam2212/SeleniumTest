from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
print("sample test case started")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.trello.com/")
#LOG IN
l=driver.find_element("link text", "Log in")
l.click()
time.sleep(3)
driver.find_element("id", "user").send_keys("vaishnavishanmugam260@gmail.com")
driver.find_element("id", "login").click()
time.sleep(3)
driver.find_element("id", "password").send_keys("TestSelenium1234")
time.sleep(3)
s=driver.find_element("id", "login-submit")
s.click()
time.sleep(15)
e1=driver.find_element("xpath", '//div[@class="board-tile mod-add"]')
e1.click()
time.sleep(5)


# Adding the Project
e2=driver.find_element("xpath",'/html/body/div[3]/div/section/div/form/div[1]/label/input')
e2.send_keys("Project")
time.sleep(5)
e3 =driver.find_element("xpath",'//button[text()="Create"]')
e3.click()
time.sleep(5)

#Creating Lists
driver.find_element("name","name").send_keys("Not Started")
time.sleep(5)
e4=driver.find_element("xpath",'//input[@type="submit" and @value="Add list"]')
e4.click()
time.sleep(3)
e5=driver.find_element("xpath",'//*[@id="board"]/div[2]/form/a')
driver.find_element("name","name").send_keys("In Progress")
time.sleep(5)
e6=driver.find_element("xpath",'//input[@type="submit" and @value="Add list"]')
e6.click()
time.sleep(3)
e7=driver.find_element("xpath",'//*[@id="board"]/div[3]/form/input')
driver.find_element("name","name").send_keys("QA")
time.sleep(5)
e8=driver.find_element("xpath",'//input[@type="submit" and @value="Add list"]')
e8.click()
time.sleep(3)
e9=driver.find_element("xpath",'//*[@id="board"]/div[4]/form/input')
driver.find_element("name","name").send_keys("Done")
time.sleep(5)
element = driver.find_element("xpath",'//*[@id="board"]/div[4]/form/input')
element.send_keys(Keys.ENTER)
time.sleep(5)

#Adding Card
e10=driver.find_element("xpath",'//span[@class="js-add-a-card"]')
e10.click()
time.sleep(2)
e11=driver.find_element("xpath",'//*[@id="board"]/div[1]/div/div[2]/div/div[1]/div/textarea')
time.sleep(2)
e11.send_keys("Card1")
time.sleep(2)
e12=driver.find_element("xpath",'//input[@type="submit" and @value="Add card"]')
e12.click()
time.sleep(3)
c2=driver.find_element("xpath",'//*[@id="board"]/div[1]/div/div[2]/div/div[1]/div/textarea')
time.sleep(2)
c2.send_keys("Card2")
time.sleep(2)
c2a=driver.find_element("xpath",'//input[@type="submit" and @value="Add card"]')
c2a.click()
time.sleep(3)
c3=driver.find_element("xpath",'//*[@id="board"]/div[1]/div/div[2]/div/div[1]/div/textarea')
time.sleep(2)
c3.send_keys("Card3")
time.sleep(2)
c3a=driver.find_element("xpath",'//input[@type="submit" and @value="Add card"]')
c3a.click()
time.sleep(3)
c4=driver.find_element("xpath",'//*[@id="board"]/div[1]/div/div[2]/div/div[1]/div/textarea')
time.sleep(2)
c4.send_keys("Card4")
time.sleep(2)
c4a=driver.find_element("xpath",'//input[@type="submit" and @value="Add card"]')
c4a.click()
time.sleep(3)

#Moving Cards
source1=driver.find_element("link text","Card2")
source1.click()
time.sleep(2)
c2b=driver.find_element("xpath",'//*[@id="chrome-container"]/div[3]/div/div/div/div[5]/div[5]/div/a[1]/span[2]')
c2b.click()
time.sleep(2)

select_Add = driver.find_element("xpath",'//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/div/div[2]/div[1]/select').click()
time.sleep(3)
s2=driver.find_element("xpath",'//div//select/option[contains(text(),"In Progress")]')
s2.click()
time.sleep(3)



c2c=driver.find_element("xpath",'//input[@type="submit" and @value="Move"]')
c2c.click()
time.sleep(3)

m1=driver.find_element("xpath",'//*[@id="chrome-container"]/div[3]/div/div/a')
m1.click()

source2=driver.find_element("link text","Card3")
source2.click()
time.sleep(2)
c3b=driver.find_element("xpath",'//*[@id="chrome-container"]/div[3]/div/div/div/div[5]/div[5]/div/a[1]/span[2]')
c3b.click()
time.sleep(2)


select_Adder1 = driver.find_element("xpath",'//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/div/div[2]/div[1]/select').click()
time.sleep(3)
s3=driver.find_element("xpath",'//div//select/option[contains(text(),"QA")]')
s3.click()
time.sleep(3)

c3c=driver.find_element("xpath",'//input[@type="submit" and @value="Move"]')
c3c.click()
time.sleep(3)

m2=driver.find_element("xpath",'//*[@id="chrome-container"]/div[3]/div/div/a')
m2.click()

source3=driver.find_element("link text","Card2")
source3.click()
time.sleep(2)
c2qa=driver.find_element("xpath",'//*[@id="chrome-container"]/div[3]/div/div/div/div[5]/div[5]/div/a[1]/span[2]')
c2qa.click()
time.sleep(2)

select_Adding = driver.find_element("xpath",'//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/div/div[2]/div[1]/select').click()
time.sleep(3)
p1=driver.find_element("xpath",'//div//select/option[contains(text(),"QA")]')
p1.click()
time.sleep(3)


c2p=driver.find_element("xpath",'//input[@type="submit" and @value="Move"]')
c2p.click()
time.sleep(3)


m3=driver.find_element("xpath",'//*[@id="chrome-container"]/div[3]/div/div/a')
m3.click()

openc1=driver.find_element("link text","Card1")
openc1.click()
time.sleep(2)

member=driver.find_element("xpath",'//*[@id="chrome-container"]/div[3]/div/div/div/div[5]/div[2]/div/a[1]')
member.click()
time.sleep(3)

ms=driver.find_element("xpath",'//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/div[2]/ul/li/a/span[2]')
ms.click()
time.sleep(3)

m4=driver.find_element("xpath",'//*[@id="chrome-container"]/div[4]/div/div[1]/a')
m4.click()
time.sleep(3)

comment=driver.find_element("xpath",'//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[11]/div[2]/form/div/div/textarea')
comment.send_keys("I am done")
time.sleep(3)
#driver.find_element("xpath",'//input[@type="submit" and @value="Save"]').click()


time.sleep(3)

m5=driver.find_element("xpath",'//*[@id="chrome-container"]/div[3]/div/div/a')
m5.click()
time.sleep(5)


print("sample test case successfully completed")
