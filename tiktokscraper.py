from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

browser_driver = Service(executable_path="chromedriver.exe")
page = webdriver.Chrome(service=browser_driver)
page.get("https://www.tiktok.com/@khaby.lame?lang=en")
time.sleep(1)

username = page.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/h1").text
name = page.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/h2").text

following_amount = page.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[1]/strong").text

followers_amount = page.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[2]/strong").text

total_likes_amount = page.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[3]/strong").text

time.sleep(5)

latest_video_views_amount = page.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/a/div/div[2]/strong").text
page.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/a/div/div[2]").click()
latest_video_likes_amount = page.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/button[1]/strong").text
#latest_video_comments_amount = page.find_element(By.NAME, "browse-comment-count")

print(f"Username: {username}")
print(f"Name: {name}")
print(f"@{username} is following {following_amount} people")
print(f"@{username} has {followers_amount} followers")
print(f"@{username} has {total_likes_amount} likes on his account")
print("")

print(f"@{username} has {latest_video_views_amount} views, {latest_video_likes_amount} likes, and  on their last video")

#username = page.find_element(By.ID, "username")
#password = page.find_element(By.ID, "password")
#username.send_keys("admin")
#password.send_keys("1234")
#IMPORTANT, CONSIDER THIS
#page.find_element(By.CSS_SELECTOR, "input.btn-primary").click()


#quotes = page.find_elements(By.CLASS_NAME, "text")
#authors = page.find_elements(By.CLASS_NAME, "author")

#file = open("scraped_quotes2.csv", "w")
#writer = csv.writer(file)

#writer.writerow(["QUOTES", "AUTHORS"])

#for quote, author in zip(quotes, authors):
    #print(quote.text + " - " + author.text)
    #writer.writerow([quote.text, author.text])
#file.close()