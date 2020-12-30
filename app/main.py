from flask import Flask, render_template
from flask_qrcode import QRcode
from selenium import webdriver

app = Flask(__name__)

qrcode = QRcode(app)

@app.route('/')
@app.route('/index')
def index():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("enable-automation")
    chrome_options.add_argument("--window-size=1360,765");
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-browser-side-navigation")
    chrome_options.add_argument("--disable-gpu");
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver.implicitly_wait(10)
    driver.get("https://web.whatsapp.com")
    return driver.page_source
    # element = None
    # while element==None:
    #     element = driver.find_element_by_class_name('_1yHR2').get_attribute("data-ref")
    # app.logger.info(element)
    # return render_template('index.html', data = qrcode(element, box_size=4, error_correction='H'))
