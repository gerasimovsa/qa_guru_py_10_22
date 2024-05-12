from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
from allure import step


class WikipediaOnboardingPage:

    @staticmethod
    def continue_to_next_screen():
        with step("Clicking on 'continue' button"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

    @staticmethod
    def click_onboarding_done():
        with step("Clicking on 'Getting Started' button"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")).click()

    @staticmethod
    def should_have_screen_with_text(text: str):
        with step(f"Checking that screen with {text} is displayed"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text(text))

    @staticmethod
    def should_not_have_onboarding_screen():
        with step(f"Checking that onboarding screen is not present"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(be.not_.present)


onboarding_page = WikipediaOnboardingPage()
