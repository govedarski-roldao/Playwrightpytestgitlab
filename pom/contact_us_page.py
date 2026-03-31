from playwright.sync_api import Playwright, sync_playwright, expect

class ContactUsPage:
    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")

    def submit_form(self,name, address, email, phone, subject, message):
        self.page.get_by_role("textbox", name="Name *").click()
        self.page.get_by_role("textbox", name="Name *").fill(name)
        self.page.get_by_role("textbox", name="Address").click()
        self.page.get_by_role("textbox", name="Address").fill(address)
        self.page.get_by_role("textbox", name="Email *").click()
        self.page.get_by_role("textbox", name="Email *").fill(email)
        self.page.get_by_role("textbox", name="Phone").click()
        self.page.get_by_role("textbox", name="Phone").fill(phone)
        self.page.get_by_role("textbox", name="Subject").click()
        self.page.get_by_role("textbox", name="Subject").fill(subject)
        self.page.get_by_role("textbox", name="Message").click()
        self.page.get_by_role("textbox", name="Message").fill(message)
        self.page.get_by_test_id("buttonElement").click()

