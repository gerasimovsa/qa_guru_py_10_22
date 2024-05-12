import os

import allure
import requests
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_xml(browser):
    xml = browser.driver.page_source
    allure.attach(xml, 'XML', AttachmentType.XML, '.xml')


def add_video_mobile(browser):
    response = requests.get(f'https://api.browserstack.com/app-automate/sessions/{browser.driver.session_id}.json',
                            auth=(os.getenv("BSTACK_USER_NAME"), os.getenv("BSTACK_ACCESS_KEY")))
    video_url = response.json()['automation_session']['video_url']
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')
