# from playwright.sync_api import Playwright, sync_playwright, expect
# import time
# #
# #
# def test_run(set_up) -> None:
#     page = set_up
#     locator = page.get_by_test_id("handle-button")
#     login_issue = True
#     while login_issue:
#         if not locator.is_visible():
#             locator.click()
#         else:
#             login_issue = False
#         time.sleep(0.1)
#     page.get_by_test_id("handle-button").click()
#     page.get_by_test_id("signUp.switchToSignUp").click()
#     page.get_by_role("button", name="Log in with Email").click()
#     page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
#     page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("test@testrodolfo.com")
#     page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("Tab")
#     page.get_by_role("textbox", name="Password").fill("test")
#     page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
#     # page.get_by_role("link", name="Shop Women", exact=True).click()
#     # page.get_by_label("Shoes gallery").get_by_role("link", name="Quick View").click()
#     page.wait_for_load_state("networkidle")
#     page.pause()
#     expect(page.get_by_test_id("handle-button")).to_be_visible()
#     page.get_by_role("link", name="Shop Women", exact=True).click()
#     all_links = page.get_by_role("link").all()
#     for link in all_links:
#         if link.text_content() == "$85":
#             assert 'socks' not in link.text_content().lower() and 'notpad' not in link.text_content().lower()
#     product = page.get_by_text("$85").first.locator("xpath=../../../../..").text_content()
#     assert product != "Socks"
#     print("yay")
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     test_run(playwright)
