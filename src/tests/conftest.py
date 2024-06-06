from datetime import datetime
from pathlib import Path

import pytest
from playwright.sync_api import expect
from slugify import slugify


@pytest.fixture(scope="function")
def set_up_tear_down(page) -> None:
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://www.saucedemo.com")
    expect(page).to_have_url('https://www.saucedemo.com/')
    yield page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if report.failed or xfail and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
            page.screenshot(path=screen_file)

        if (report.skipped and xfail) or (report.failed and not xfail):
            # add the screenshots to the html report
            extra.append(pytest_html.extras.png(screen_file))
        report.extra = extra

