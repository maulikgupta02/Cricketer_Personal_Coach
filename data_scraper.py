from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# url="https://www.cricbuzz.com/live-cricket-scores/78138/ind-vs-pak-3rd-match-group-a-asia-cup-2023"
# url="https://www.cricbuzz.com/live-cricket-scores/78208/sl-vs-ind-final-asia-cup-2023"
# url="https://www.cricbuzz.com/live-cricket-scores/78201/ban-vs-ind-super-fours-6th-match-asia-cup-2023"
url="https://www.cricbuzz.com/live-cricket-scores/78187/ind-vs-sl-super-fours-4th-match-asia-cup-2023"
# url="https://www.cricbuzz.com/live-cricket-scores/78180/ind-vs-pak-super-fours-3rd-match-asia-cup-2023"

driver = webdriver.Chrome()
driver.get(url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1);")
time.sleep(2)
butt=driver.find_element(By.ID,"full_commentary_btn")
time.sleep(2)
butt.click()

while True:

    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    page_height=driver.execute_script("return document.body.scrollHeight")

    if last_height==page_height:
        break

elements = driver.find_elements(By.TAG_NAME, 'p')

with open("match_data//ind-vs-sl.txt","a+") as file:
    for i in elements:
        file.write(i.text+".")