import asyncio
from pyppeteer import launch


async def anchor_connect():
    print("Launching pyppeteer")
    browser = await launch(args=["--no-sandbox"], headless=headless_mode)
    page = await browser.newPage()

    navigationPromise = asyncio.ensure_future(page.waitForNavigation())

    await page.goto("https://anchor.fm/dashboard/episode/new")

    await page.setViewport({"width": 1600, "height": 789})
    await navigationPromise

    print("Trying to log in")
    await page.type("#email", email)
    await page.type("#password", password)
    await page.click("button[type=submit]")
    await navigationPromise
    print("Logged in")
