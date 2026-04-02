# from playwright.sync_api import Playwright, expect
#
#
from playwright.sync_api import expect


def test_login(login_set_up) -> None:
    page = login_set_up
    expect(page.get_by_role("link", name="pomidor.png"))
#     page.goto("https://symonstorozhenko.wixsite.com/website-1")
#     # page.wait_for_load_state("networkidle")
#     page.set_default_timeout(10000)
#     login_issue = True
#     while login_issue:
#         if page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
#             page.click("button:has-text(\"Log in\")")
#         else:
#             login_issue = False
#     # page.get_by_role("button", name="Log In").click()
#     page.get_by_test_id("signUp.switchToSignUp").click()
#     expect(page.get_by_test_id("siteMembersDialogLayout")).to_be_visible()
#     page.get_by_role("button", name="Log in with Email").click()
#     page.set_default_timeout(10000)
#     page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
#     page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("test@testrodolfo.com")
#     page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("Tab")
#     page.get_by_role("textbox", name="Password").fill("test")
#     page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
#
#     context.close()
#     browser.close()
#
#     # page.get_by_test_id("signUp.switchToSignUp").click()
#     # page.get_by_role("button", name="Log in with Email").click()
#
#
#
#
