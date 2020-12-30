from flask import Flask, render_template
from flask_qrcode import QRcode
from selenium import webdriver

app = Flask(__name__)

qrcode = QRcode(app)

@app.route('/')
@app.route('/index')
def index():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://google.com")
    return driver.page_source
    # element = None
    # while element==None:
    #     element = driver.find_element_by_class_name('_1yHR2').get_attribute("data-ref")
    # app.logger.info(element)
    # return render_template('index.html', data = qrcode(element, box_size=4, error_correction='H'))
