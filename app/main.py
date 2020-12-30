from flask import Flask, render_template
from flask_qrcode import QRcode
from selenium import webdriver

app = Flask(__name__)

qrcode = QRcode(app)

@app.route('/')
@app.route('/index')
def index():
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com")
    content = driver.find_element_by_class_name('_1yHR2').get_attribute("data-ref")
    app.logger.info(content)
    return render_template('index.html', data = qrcode(content, box_size=5, error_correction='H'))
