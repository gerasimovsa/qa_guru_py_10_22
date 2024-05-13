import pytest
from allure import step
from appium import webdriver
from dotenv import load_dotenv
from selene import browser
from utils import path, attach


def pytest_addoption(parser):
    parser.addoption('--context', default='local_real')


def pytest_configure(config):
    context = config.getoption("--context")
    env_file = path.root_path(f'.env.{context}')
    load_dotenv(env_file)


@pytest.fixture(scope="function", autouse=True)
def mobile_management(request):
    with step("Setting up remote executor"):
        launch_context = request.config.getoption("--context")
        from config import setup_config
        driver_options = setup_config.setup_driver_options(context=launch_context)
        browser.config.driver = webdriver.Remote(setup_config.remote_url, options=driver_options)
    with step("Setting up timeout for browser"):
        browser.config.timeout = setup_config.timeout

    yield

    with step("Attaching screenshot, xml and video"):
        attach.add_xml(browser)
        attach.add_screenshot(browser)
        if launch_context == "bstack":
            attach.add_video_mobile(browser)

    with step("Browser teardown"):
        browser.quit()
