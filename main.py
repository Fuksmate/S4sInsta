from selenium import webdriver
from time import sleep


#GLOBAL VARIABLRES

username = "filip@niepodam.pl"
password = "FILIP123"

#Open webdriver
browser = webdriver.Chrome("C:\chromedriver.exe")
browser.get("https://www.instagram.com/")

#Login to IG
sleep(2)
cookieAccept = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
cookieAccept.click()

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys(username)
password_input.send_keys(password)

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(3)
cancel = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div")
cancel.click()

cancel = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
cancel.click()

sleep(2)

#s4s
for column in range(250):
    for row in range(3):
        browser.get("https://www.instagram.com/explore/tags/girl/")
        browser.find_element_by_xpath("html/body/div[1]/section/main/article/div[2]/div/div[" + str(column + 1) + "]/div[" + str(row + 1) + "]/a/div").click()
        sleep(2)
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span").click()
        sleep(2)
        for columnUser in range(250):
            for rowUser in range(3):
                if browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div/div/div[" + str(columnUser + 1)+ "]/div[" + str(rowUser + 1) + "]/a/div/div[2]"):
                    browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div/div/div[" + str(columnUser + 1) + "]/div[" + str(rowUser + 1) + "]/a/div/div[2]").click()
                    sleep(2)
                    browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span").click()
                    sleep(2)
                    browser.find_element_by_xpath("/html/body/div[4]/div[3]").click()
                else:
                    columnUser = 250