import time
import pytest
import os

PASSWORD = os.environ["PASSWORD"]
HEADLESS = os.getenv("CI") is not None


# try:
#     PASSWORD = os.environ["PASSWORD"]
# except KeyError:
#     import utils.secret_config
#     PASSWORD = utils.secret_config.PASSWORD

@pytest.fixture(scope="session")
def set_up(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.wait_for_load_state("networkidle")
    page.set_default_timeout(3000)
    yield page


@pytest.fixture(scope="session")
def context_creation(playwright):
    browser = playwright.chromium.launch(
        headless=HEADLESS,
        slow_mo=300 if not HEADLESS else 0)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.wait_for_load_state("networkidle")
    page.set_default_timeout(3000)
    login_issue = True
    # page.pause()
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.click("button:has-text(\"Log in\")")
        else:
            login_issue = False
        time.sleep(0.1)
        # get_by_test_id("handle-button")
    # page.pause()
    # try:
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.fill('input:below(:text("Email"))', "symon.storozhenko@gmail.com")
    page.press("[data-testid='siteMembers.container'] >> input[type='email']", "Tab")
    page.fill("input[type='password']", PASSWORD)
    page.click("[data-testid='submit'] >> [data-testid='buttonElement']")
    page.wait_for_load_state(timeout=1000)
    time.sleep(5)
    context.storage_state(path="state.json")

    yield context
    time.sleep(5)


@pytest.fixture()
def login_set_up(context_creation, playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.wait_for_load_state("networkidle")
    # page.pause()
    page.set_default_timeout(3000)
    assert not page.is_visible("text=Log In")
    yield page
    time.sleep(5)
    browser.close()


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
