from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def scrape_and_screenshot(url: str, screenshot_path: str = "screenshot.png") -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=screenshot_path, full_page=True)
        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "html.parser")

    # Debug: Save raw HTML to file to inspect it manually
    with open("debug_page.html", "w", encoding="utf-8") as f:
        f.write(html)

    # Try to locate the main content
    content_div = soup.find("div", class_="mw-parser-output")

    if not content_div:
        print("❌ Could not find .mw-parser-output div.")
        return "⚠️ No chapter content found."

    # Print what was found
    print("✅ Found content div.")
    elements = content_div.find_all(["h1", "h2", "h3", "p", "li"])
    clean_text = "\n\n".join(el.get_text(strip=True) for el in elements if el.get_text(strip=True))

    return clean_text

