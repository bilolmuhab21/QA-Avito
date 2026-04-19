from playwright.sync_api import Page
import re

BASE_URL = "https://cerulean-praline-8e5aa6.netlify.app"


def parse_price(text):
    return int("".join(filter(str.isdigit, text)) or 0)


def test_open(page: Page):
    page.goto(BASE_URL)


def test_price_filter(page: Page):
    page.goto(BASE_URL)

    page.locator('input').nth(0).fill("1000")
    page.locator('input').nth(1).fill("30000")

    page.wait_for_timeout(2000)

    prices_elements = page.locator("text=₽")

    prices = []
    for i in range(prices_elements.count()):
        text = prices_elements.nth(i).inner_text()
        prices.append(parse_price(text))

    assert all(1000 <= p <= 30000 for p in prices)


def test_sort(page: Page):
    page.goto(BASE_URL)

    page.wait_for_timeout(2000)

    prices_elements = page.locator("text=₽")

    prices = []
    for i in range(prices_elements.count()):
        text = prices_elements.nth(i).inner_text()
        prices.append(parse_price(text))

    if len(prices) > 1:
        assert prices == sorted(prices) or prices == sorted(prices, reverse=True)


def test_mobile_theme(page: Page):
    page.set_viewport_size({"width": 390, "height": 844})
    page.goto(BASE_URL)

    html = page.locator("html")
    before = html.get_attribute("class") or ""

    page.locator("button").first.click()

    after = html.get_attribute("class") or ""

    assert before != after
