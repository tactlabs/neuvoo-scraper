from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json




PATH = "/home/aswin/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)


def startpy():
    driver.get("https://neuvoo.co.in/jobs/?k=machine+learning&l=&p=1&date=&field=&company=&source_type=&radius=&from=&test=&iam=&is_category=no")

    # print all details inside the card
    details = driver.find_elements_by_class_name("card__job-c")
    for detail in details:
        print(detail.text)
        print()

    driver.quit()
if __name__ == '__main__':
    startpy()