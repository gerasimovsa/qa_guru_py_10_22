from wikipedia_app.android_pages.onboarding_page import onboarding_page


def test_onboarding_screen():
    onboarding_page.should_have_screen_with_text("The Free Encyclopedia\n…in over 300 languages")
    onboarding_page.continue_to_next_screen()
    onboarding_page.should_have_screen_with_text("New ways to explore")
    onboarding_page.continue_to_next_screen()
    onboarding_page.should_have_screen_with_text("Reading lists with sync")
    onboarding_page.continue_to_next_screen()
    onboarding_page.should_have_screen_with_text("Data & Privacy")
    onboarding_page.click_onboarding_done()
    onboarding_page.should_not_have_onboarding_screen()


