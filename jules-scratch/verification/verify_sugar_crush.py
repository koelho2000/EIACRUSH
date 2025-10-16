import asyncio
from playwright.async_api import async_playwright, expect
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # 1. Load the page from the local web server
        await page.goto('http://localhost:8080/index.html')

        # Wait for Firebase auth to resolve and render the main menu
        await page.wait_for_selector("#auth-buttons, #user-info", timeout=20000)

        # 2. Start as a guest
        await page.get_by_role("button", name="Jogar como Convidado").click()

        # 3. Unlock all levels
        await page.get_by_role("button", name="Desbloquear").click()
        await page.get_by_placeholder("CÓDIGO SECRETO").fill("K2000_EIA_CRACK")
        await page.get_by_role("button", name="Confirmar").click()
        await page.wait_for_selector('.popup:text("Todos os níveis desbloqueados!")')

        # 4. Go to a level (e.g., level 1)
        await page.get_by_role("button", name="Nível 1", exact=True).click()

        # 5. Start the level
        await page.get_by_role("button", name="Jogar").click()

        # Wait for the game board to be ready
        await expect(page.locator("#game-board .gem")).to_have_count(49)

        # 6. Trigger the auto-win patch
        # The patch is on the bottom-right gem (6, 6)
        bottom_right_gem = page.locator('.gem[data-r="6"][data-c="6"]')
        for _ in range(5):
            await bottom_right_gem.click()
            await page.wait_for_timeout(50) # Small delay between clicks

        # 7. Wait for the "Sabia Que?" modal and trigger Sugar Crush
        await expect(page.locator("#sabia-que-modal")).to_be_visible(timeout=10000)
        await page.get_by_role("button", name="Continuar").click()

        # 8. Wait for Sugar Crush to start and take a screenshot
        await expect(page.locator(".sugar-crush-active")).to_be_visible(timeout=5000)
        await page.wait_for_timeout(1500) # Let some animations play

        await page.screenshot(path="jules-scratch/verification/verification.png")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())