import os
from dotenv import load_dotenv
from rewriter import humanize_text # Assuming you renamed the file to humanizer.py

# Load your Groq key
load_dotenv()
LLM_KEY = os.getenv("GROQ_API_KEY")

if __name__ == "__main__":
    print("--- ONE-SHOT AI HUMANIZER TERMINAL ---")
    
    # The new infinite loop keeps the program running forever
    while True:
        print("\nPaste your draft text below.")
        print("When you are finished pasting, type 'D' on a new line and press Enter.")
        print("(Or type 'QUIT' to exit the program)\n")

        # Multi-line input loop
        input_lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            
            # Allow the user to easily exit the program
            if line.strip().upper() == 'QUIT':
                print("Exiting AI Humanizer. Goodbye!")
                exit()
                
            # Stop reading when the user types D
            if line.strip().upper() == 'D':
                break
                
            input_lines.append(line)

        # Stitch the lines back together into a single string
        draft_text = "\n".join(input_lines).strip()

        # Safety check
        if not draft_text:
            print("No text detected. Let's try again.")
            continue # Skips back to the top of the loop
            
        print("\n--- HUMANIZING TEXT (PLEASE WAIT) ---")
        
        # Call the API exactly once
        final_humanized_text = humanize_text(draft_text, LLM_KEY)

        print("\n--- FINAL RESULT ---")
        print(final_humanized_text)
        print("--------------------\n")