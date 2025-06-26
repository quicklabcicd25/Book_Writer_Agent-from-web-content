def human_review_loop(initial_text: str) -> str:
    print("👤 Human Review Session")
    print("----- Preview Start -----\n")
    print(initial_text[:500])
    print("\n----- Preview End -----")
    print("\n(Leave input blank to keep content as is)")
    feedback = input("\n✏️ Enter edited content or press Enter to keep: ")
    return feedback if feedback.strip() else initial_text
