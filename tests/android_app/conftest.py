import pytest
from allure import step
from appium import webdriver
from dotenv import load_dotenv
from selene import browser
from utils import path, attach

CONTEXT = "bstack"  # local_real,local_emulator


@pytest.fixture()
def load_env():
    dotenv_file = path.root_path(f".env.{CONTEXT}")
    load_dotenv(dotenv_file)


@pytest.fixture(scope="function", autouse=True)
def mobile_management(load_env):
    with step("Setting up remote executor"):
        from config import setup_config
        driver_options = setup_config.setup_driver_options(context=CONTEXT)
        browser.config.driver = webdriver.Remote(setup_config.remote_url, options=driver_options)
    with step("Setting up timeout for browser"):
        browser.config.timeout = setup_config.timeout

    yield

    with step("Attaching screenshot, xml and video"):
        attach.add_xml(browser)
        attach.add_screenshot(browser)
        if CONTEXT == "bstack":
            attach.add_video_mobile(browser)

    with step("Browser teardown"):
        browser.quit()
