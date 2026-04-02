from playwright.sync_api import Playwright, sync_playwright, expect, Page
from pom.shop_woman_elements import ShopWoman


def test_about_us_section_verbiage(login_set_up):
    shop_woman = ShopWoman(login_set_up)
    expect(shop_woman.celebrating_beauty_header).to_be_visible()


def test_about_us_section_verbiage_2(login_set_up):
    page = login_set_up
    # page.goto("https://symonstorozhenko.wixsite.com/website-1")

    shop_woman = ShopWoman(page)
    expect(shop_woman.celebrating_beauty_header).to_be_visible()

