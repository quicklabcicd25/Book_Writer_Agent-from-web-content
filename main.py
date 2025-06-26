from core.scraper import scrape_and_screenshot
from agents.ai_writer import ai_writer_spin
from agents.ai_reviewer import ai_reviewer_feedback
from agents.human_review import human_review_loop
from core.chromadb_utils import store_version
import os

def main():
    # Step 1: Define the URL
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    
    # Step 2: Scrape content
    print("🌐 Scraping content...")
    content = scrape_and_screenshot(url)
    
    # Debugging preview
    if not content or content.strip() == "":
        print("❌ Scraper returned empty content.")
        return
    else:
        print("🔍 Scraped content preview:\n", content[:500], "\n")

    # Step 3: AI Writer Simulation
    print("✍️ AI Writer (Simulated)...")
    spun = ai_writer_spin(content)

    # Step 4: AI Reviewer Simulation
    print("🧠 AI Reviewer (Simulated)...")
    reviewed = ai_reviewer_feedback(spun)

    # Step 5: Human-in-the-loop Editing
    print("👤 Human-in-the-loop Editing...")
    final_content = human_review_loop(reviewed)

    # Step 6: Store in ChromaDB
    version_id = "chapter_1"
    store_version(version_id, final_content)

    # Step 7: Save to .txt file
    save_dir = "output"
    os.makedirs(save_dir, exist_ok=True)
    chapter_path = os.path.join(save_dir, f"{version_id}.txt")
    with open(chapter_path, "w", encoding="utf-8") as f:
        f.write(final_content)

    # Final preview
    print(f"\n✅ Final content saved to: {chapter_path}")
    print("\n📄 Final Content Preview:\n")
    print(final_content[:500], "...")

if __name__ == "__main__":
    main()


