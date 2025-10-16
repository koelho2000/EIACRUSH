import asyncio
from playwright.async_api import async_playwright, expect
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Load the page in debug mode to get enough coins
        await page.goto('http://localhost:8080/index.html?debug=true')

        # Wait for the main menu to render
        await expect(page.get_by_role("button", name="Jogar como Convidado")).to_be_visible(timeout=10000)
        await page.get_by_role("button", name="Jogar como Convidado").click()

        # Navigate to a level
        await page.get_by_role("button", name="Nível 1", exact=True).click()

        # The pre-level modal should now be visible
        await expect(page.locator("#level-start-modal")).to_be_visible(timeout=5000)

        # Assert that the booster buttons are enabled
        gem_hammer_booster = page.locator('#booster-selection button', has_text='Martelo de Gema')
        await expect(gem_hammer_booster).to_be_enabled()

        extra_striped_booster = page.locator('#booster-selection button', has_text='+1 Peça Listada')
        await expect(extra_striped_booster).to_be_enabled()

        # Take a screenshot for verification
        await page.screenshot(path="jules-scratch/verification/boosters_enabled.png")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())