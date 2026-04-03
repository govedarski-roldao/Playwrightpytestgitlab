from pom.shop_woman_elements import ShopWoman
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def test_visual_landing(page, assert_snapshot):
    # access given
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    time.sleep(10)
    homepage = ShopWoman(page)

    expect(homepage.celebrating_beauty_header).to_be_visible()
    assert_snapshot(page.screenshot())
