from playwright.sync_api import Playwright, sync_playwright, expect, Page


def test_run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.wait_for_load_state("networkidle")
    page.set_default_timeout(3000)
    # page.pause()
    expect(page.get_by_role("navigation", name="Site")).to_be_visible()

    page.get_by_test_id("handle-button").click()
    expect(page.get_by_test_id("siteMembersDialogLayout")).to_be_visible()

    page.get_by_test_id("signUp.switchToSignUp").click()
    expect(page.get_by_test_id("siteMembersDialogLayout")).to_be_visible()

    page.get_by_role("button", name="Log in with Email").click()
    expect(page.get_by_test_id("emailAuth")).to_be_visible()

    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("test@test.pt")
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("Tab")
    page.get_by_role("textbox", name="Password").fill("test123")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
