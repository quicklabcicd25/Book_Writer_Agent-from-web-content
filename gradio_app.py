import gradio as gr
from core.scraper import scrape_and_screenshot
import os

def extract_and_save_chapter(url):
    # Extract clean story text
    clean_text = scrape_and_screenshot(url)

    # Handle missing content
    if not clean_text or clean_text.startswith("⚠️"):
        return "❌ Failed to extract content from the URL.", None

    # Save to file
    os.makedirs("output", exist_ok=True)
    file_path = "output/clean_chapter.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(clean_text)

    # Show preview + downloadable file
    preview = clean_text[:1000] + "\n\n... (Full chapter saved below)"
    return preview, file_path

# Create the interface
demo = gr.Interface(
    fn=extract_and_save_chapter,
    inputs=gr.Textbox(label="📘 Wikisource Chapter URL", value="https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"),
    outputs=[
        gr.Textbox(label="🔍 Preview of Extracted Chapter (first 1000 characters)"),
        gr.File(label="📄 Download Clean Chapter Text")
    ],
    title="📚 Chapter Extractor Tool",
    description="Paste a Wikisource chapter URL to extract and download clean story text."
)

if __name__ == "__main__":
    demo.launch()
