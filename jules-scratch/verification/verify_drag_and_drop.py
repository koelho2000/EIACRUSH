from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get the absolute path to the index.html file
        file_path = os.path.abspath("index.html")

        page.goto(f"file://{file_path}")

        # Wait for the main menu to be visible
        page.wait_for_selector('h1:has-text("EIA Crush")', state="visible")

        # Click the "Play as Guest" button
        page.click('button:has-text("Jogar como Convidado")')

        # Wait for the world map to be visible
        page.wait_for_selector('h2:has-text("Mapa de Mundos")', state="visible")

        # Disable the pulsing animation on the level nodes to prevent instability
        page.add_style_tag(content=".level-node.unlocked { animation: none !important; }")

        # Click the first level
        page.click('.level-node.unlocked')

        # Wait for the level start modal to be visible
        page.wait_for_selector("#level-start-modal", state="visible")

        # Click the "Play" button on the level start modal
        page.click('#level-start-modal button:has-text("Jogar")')

        # Wait for the game board to be visible
        page.wait_for_selector("#game-board", state="visible")

        # Drag and drop a gem
        page.drag_and_drop('.gem[data-r="0"][data-c="0"]', '.gem[data-r="0"][data-c="1"]', force=True)

        # Wait for the animations to complete
        page.wait_for_timeout(3000)

        page.screenshot(path="jules-scratch/verification/verification.png")
        browser.close()

if __name__ == "__main__":
    run()