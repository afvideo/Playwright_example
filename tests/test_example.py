from playwright.sync_api import Playwright
import allure
import datetime


@allure.epic('Example tests')
@allure.story('Tests todomvc')
@allure.testcase('https://playwright-todomvc.antonzimaiev.repl.co', 'playwright-todomvc')
@allure.link('https://playwright-todomvc.antonzimaiev.repl.co/#/', 'Just another link')
@allure.title('Simple test todomvc')
@allure.severity('CRITICAL')
def test_todomvc(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_role("link", name="petehunt").click()
    now = datetime.datetime.now().strftime('_%Y-%m-%d_%H-%M-%S')
    page.screenshot(path=f"results/test_todomvc01{now}.png")
    page.get_by_placeholder("Search").clear()
    page.get_by_placeholder("Search").fill("afvideo")
    page.get_by_placeholder("Search").press("Enter")
    now = datetime.datetime.now().strftime('_%Y-%m-%d_%H-%M-%S')
    page.screenshot(path=f"results/test_todomvc02{now}.png")
    page.get_by_role("link", name='Advanced search', exact=True).click()

    # ---------------------
    context.close()
    browser.close()


def test_todomvc_headless(page) -> None:
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_role("link", name="petehunt").click()
    now = datetime.datetime.now().strftime('_%Y-%m-%d_%H-%M-%S')
    page.screenshot(path=f"results/test_todomvc_headless01{now}.png")
    page.get_by_placeholder("Search").clear()
    page.get_by_placeholder("Search").fill("afvideo")
    page.get_by_placeholder("Search").press("Enter")
    now = datetime.datetime.now().strftime('_%Y-%m-%d_%H-%M-%S')
    page.screenshot(path=f"results/test_todomvc_headless02{now}.png")
    page.get_by_role("link", name='Advanced search', exact=True).click()
