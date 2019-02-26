import os
import warnings
from selenium import webdriver

def handle(req):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--test-type')

        image_width = os.getenv('image_width', '1920')
        image_height = os.getenv('image_height', '1080')
        options.add_argument(f"window-size={image_width},{image_height}")

        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        options.binary_location = "/usr/bin/chromium-browser"
        driver = webdriver.Chrome(chrome_options=options)
 
        driver.get(req)
        driver.save_screenshot('/home/app/screenshot.png')
        driver.close()

        with open('/home/app/screenshot.png', 'rb') as f:
          return f.read()
