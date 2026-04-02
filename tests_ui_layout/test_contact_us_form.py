import time
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.contact_us_page import ContactUsPage

@pytest.mark.integration
def test_submit_form(login_set_up) -> None:
    # browser = playwright.chromium.launch(headless=False)
    page = login_set_up

    contact_us_page = ContactUsPage(page)
    # page.pause()
    contact_us_page.navigate()
    contact_us_page.submit_form("Symon", '123 main street', "test@email.com", '123-432-5434', 'test subject',
                                'test message blah')


# with sync_playwright() as playwright:
#     test_page = ContactUsPage(playwright)
#     time.sleep(10)
