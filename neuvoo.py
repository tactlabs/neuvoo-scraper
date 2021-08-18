from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

PATH = "/home/aswin/Downloads/chromedriver_linux64/chromedriver"

def startpy():
    user_agent ="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(PATH,options=options)

    driver.get("https://neuvoo.co.in/jobs/?k=machine+learning&l=&p=1&date=&field=&company=&source_type=&radius=&from=&test=&iam=&is_category=no")

    # print all details inside the card
    details = driver.find_elements_by_class_name("card__job-c")
    for detail in details:
        print(detail.text)
        print()

    driver.quit()
if __name__ == '__main__':
    startpy()