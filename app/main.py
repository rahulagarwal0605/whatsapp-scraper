from flask import Flask, render_template
from flask_qrcode import QRcode
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time

app = Flask(__name__)

qrcode = QRcode(app)

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    driver.get("https://web.whatsapp.com")
    time.sleep(1)
    element = None
    while element is None:
        element = driver.find_element_by_class_name('_1yHR2').get_attribute("data-ref")
        app.logger.info(element)
    return qrcode(element, box_size=4, error_correction='H')

@app.route('/receive', methods=['GET', 'POST'])
def receive():
    wait = WebDriverWait(driver, 600)
    target = '"LNMIIT Param Parikh"'
    # string = "Wasted!!!"
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    app.logger.info(group_title.text)
    group_title.click()
    # eula = driver.find_elements_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]')[0]
    # for my_xpath in eula:
    #     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', my_xpath)
    #     time.sleep(1)
    # message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    # message.send_keys(string)
    # sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    # sendbutton.click()
    # message = driver.find_elements_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]')[0]
    # recentList = driver.find_elements_by_xpath("//div[@class='_1wlJG']")
    # while True:
    #     driver.execute_script("arguments[0].scrollIntoView();", recentList[0] )
    # for x in range(len(recentList)):
    #      app.logger.info(recentList[x])
    # app.logger.info(type(recentList))
    # for list in recentList :
    #     driver.execute_script("arguments[0].scrollIntoView();", list )
    # app.logger.info(list.text)
    # driver.close()
    element = driver.find_elements_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]')[0]
    element.click()
    element = driver.find_elements_by_xpath('//*[@id="main"]/div[3]/div/div/div[1]')[0]
    while True:
        try:
            driver.find_elements_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]')[0]
            driver.execute_script("arguments[0].scrollIntoView();", element)
        except IndexError:
            break
    # while True:
    #     element.send_keys(Keys.PAGE_UP);
    element = driver.find_elements_by_xpath('//*[@id="main"]/div[3]/div/div/div[2]')[0]
    message_in = element.find_elements_by_xpath("./div[contains(@class, 'message-in')]")
    message_out = element.find_elements_by_xpath("./div[contains(@class, 'message-out')]")
    app.logger.info(target + " " + str(len(message_in)))
    app.logger.info("You" + " " + str(len(message_out)))
    for x in element.find_elements_by_xpath("./div"):
        if 'message-in' in x.get_attribute('class').split():
            app.logger.warning(target)
            app.logger.info(x.text)
        elif 'message-out' in x.get_attribute('class').split():
            app.logger.warning("You")
            app.logger.info(x.text)
    return "sent"

# def scroll_until_loaded(driver):
#         check_height = driver.execute_script("return document.body.scrollHeight;")
#         while True:
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             try:
#                 wait.until(lambda driver: driver.execute_script("return document.body.scrollHeight;") > check_height)
#                 check_height = driver.execute_script("return document.body.scrollHeight;")
#             except TimeoutException:
#                 break
