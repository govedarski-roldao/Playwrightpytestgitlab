from playwright.sync_api import Playwright, sync_playwright, expect, Page
from pom.shop_woman_elements import ShopWoman


def test_about_us_section_verbiage(login_set_up):
    page = login_set_up
    shop_woman = ShopWoman(page)
    expect(shop_woman.celebrating_beauty_header).to_be_visible()
    expect(shop_woman.celebrating_beauty_body).to_be_visible()


def test_about_us_section_verbiage_2(set_up):
    page = set_up
    shop_woman = ShopWoman(page)
    expect(shop_woman.celebrating_beauty_header).to_be_visible()
    expect(shop_woman.celebrating_beauty_body).to_be_visible()

