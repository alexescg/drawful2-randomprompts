import codecs
import random
from selenium import webdriver

url = "http://jackbox.tv/"
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
driver.find_element_by_id('username').send_keys("script")
driver.find_element_by_id('roomcode').send_keys("IDQT")
driver.find_element_by_id('button-join').click()

with codecs.open("words.txt", "r", "utf-8") as f:
    content = f.read().splitlines()
    randomIndexes = random.sample(range(0, len(content)), 5)

    for i in range(0, len(randomIndexes)):
        driver.find_element_by_id("ugc-add-input").send_keys(content[randomIndexes[i]])
        driver.find_element_by_id("ugc-add-button").click()

# driver.close()
