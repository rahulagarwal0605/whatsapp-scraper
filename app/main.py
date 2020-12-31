from flask import Flask, render_template
from flask_qrcode import QRcode
from selenium import webdriver
import time

app = Flask(__name__)

qrcode = QRcode(app)

@app.route('/')
@app.route('/index')
def index():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(10)
    driver.get("https://web.whatsapp.com")
    time.sleep(1)
    element = None
    while element is None:
        element = driver.find_element_by_class_name('_1yHR2').get_attribute("data-ref")
        app.logger.info(element)
    return render_template('index.html', data = qrcode(element, box_size=4, error_correction='H'))
