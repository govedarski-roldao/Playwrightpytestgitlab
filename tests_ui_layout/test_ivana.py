from playwright.sync_api import Playwright, sync_playwright, expect

from playwright.sync_api import Playwright, sync_playwright, expect


#
#
def test_run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://ivanagovedarska.com/")
    page.wait_for_load_state("networkidle")
    expect(page.locator("text=“… her wonderful temperament")).to_be_visible()
    expect(page.locator("text=Philippe Cassard, concert")).to_be_visible()
    expect(page.locator("text=concert pianist and chamber")).to_be_visible()
    expect(page.locator("text=© Ivana Govedarska. All")).to_be_visible()

    page.get_by_role("link", name="About me").click()
    expect(page.get_by_role("link", name="Ivana Govedarska")).to_be_visible()

    # expect(page.locator("text=About me")).to_be_visible()
    expect(page.locator("text=Bulgarian born pianist Ivana")).to_be_visible()
    expect(page.locator("text=She started her piano")).to_be_visible()
    expect(page.locator("text=Throughout all these years,")).to_be_visible()
    expect(page.locator("text=Ivana is a prizewinner of")).to_be_visible()
    expect(page.locator("text=She has given various piano")).to_be_visible()
    expect(page.locator("text=Currently, Ivana is living in")).to_be_visible()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
