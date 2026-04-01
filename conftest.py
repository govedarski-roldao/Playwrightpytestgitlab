import time

import pytest

import utils.secret_config


@pytest.fixture(scope="session")
def set_up(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.wait_for_load_state("networkidle")
    page.set_default_timeout(3000)
    yield page


@pytest.fixture(scope="session")
def login_set_up(set_up):
    page = set_up
    login_issue = True
    # while login_issue:
    #     if page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
    #         page.click("button:has-text(\"Log in\")")
    #     else:
    #         login_issue = False
    #     time.sleep(0.1)
    #     get_by_test_id("handle-button")
    # page.pause()
    # try:
    #     page.click("[data-testid=\"signIn\"]")
    # except:
    page.get_by_test_id("handle-button").click()
    # page.click("[data-testid=\"signUp.switchToSignUp\"]", timeout=2000)
    # page.click("[data-testid='signUp.switchToSignUp'] >> [data-testid='buttonElement']")
    # page.fill('input:below(:text("Email"))', "symon.storozhenko@gmail.com")
    # page.press("[data-testid='siteMembers.container'] >> input[type='email']", "Tab")
    # page.fill("input[type='password']", utils.secret_config.PASSWORD)
    # page.click("[data-testid='submit'] >> [data-testid='buttonElement']")

    yield page
    page.close()

@pytest.fixture()
def go_to_new_collection(set_up):
    page = set_up
    page.goto("/new-collection")
    page.set_default_timeout(3000)

    yield page


@pytest.fixture
def home_page(page):
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    return page