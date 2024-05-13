import os

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from pydantic import BaseModel

from utils import path


class Config(BaseModel):
    timeout: float = float(os.getenv("TIMEOUT"))
    remote_url: str = os.getenv("REMOTE_URL")
    platform_version: str = os.getenv("PLATFORM_VERSION")
    platform_name: str = os.getenv("PLATFORM_NAME")
    device_name: str = os.getenv("DEVICE_NAME")
    app_wait: str = os.getenv("APP_WAIT")
    app: str = os.getenv("APP")
    if app.startswith("bs:"):
        load_dotenv(path.root_path(".env.credentials"))
        user_name: str = os.getenv("BSTACK_USER_NAME", default="")
        access_key: str = os.getenv("BSTACK_ACCESS_KEY", default="")

    def setup_driver_options(self, context):
        driver_options = UiAutomator2Options()
        if context == "bstack":
            driver_options.set_capability("remote_url", self.remote_url)
            driver_options.set_capability("platformName", self.platform_name)
            driver_options.set_capability("deviceName", self.device_name)
            driver_options.set_capability("platformVersion", self.platform_version)
            driver_options.set_capability("app", self.app)
            driver_options.set_capability(
                "bstack:options", {
                    "projectName": "Bstack_SergeyG_android_test",
                    "buildName": "android_browserstack-test-build",
                    "sessionName": "Android Browserstack test session",
                    "userName": self.user_name,
                    "accessKey": self.access_key,
                },
            )
        if context == "local_emulator":
            driver_options.set_capability("remote_url", self.remote_url)
            driver_options.set_capability("app", path.apk_path(self.app))
            driver_options.set_capability("appWaitActivity", self.app_wait)
        if context == "real_local":
            driver_options.set_capability("remote_url", self.remote_url)
            driver_options.set_capability("app", path.apk_path(self.app))
            driver_options.set_capability("appWaitActivity", self.app_wait)
        return driver_options


setup_config = Config()
