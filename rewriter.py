import time
from groq import Groq

def humanize_text(full_text, api_key):
    # Initialize the Groq client
    client = Groq(api_key=api_key)
    
    prompt = f"""
    You are an expert humanizer rewriting a university capstone project draft to achieve a 0% AI detection score on all major platforms (ZeroGPT, Grammarly, Turnitin, justdone). 
    
    Your task is to rewrite the ENTIRE text provided. Do not just rewrite parts of it.
    
    EXECUTION ALGORITHM:
    1. CONVERSATIONAL SIMPLIFICATION: Replace highly formal academic nouns with clear, direct phrases. Use natural contractions (don't, won't) where appropriate.
    2. ACADEMIC COHESION (CRITICAL): The output MUST flow logically as well-structured paragraphs. You are strictly forbidden from outputting a list of choppy, fragmented sentences or adding unnecessary line breaks. Match the paragraph structure of the original text.
    3. STRATEGIC IMPERFECTION: Introduce very slight, natural grammatical variance so it doesn't look mathematically generated.
    4. CITATION LOCK: Keep all citations completely untouched and formatted exactly as they are (e.g., (Cho et al., 2025)).
    5. BAN LIST: delve, tapestry, testament, crucial, moreover, furthermore, beacon, landscape, multifaceted, comprehensive, robust, intricate, pivotal, dynamic, seamless, framework, utilize, facilitate, implement, wherein, thus, therefore, hence, rapid, vital.
    6. Write in a plain language/word

    FULL DRAFT TEXT TO HUMANIZE:
    {full_text}

    CRITICAL OUTPUT RULE: Return ONLY the raw, revised full text. No markdown formatting, no conversational prefixes, no explanations.
    """
    
    # Retry logic
    max_retries = 3
    for attempt in range(max_retries):
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.75,
                top_p=0.90,
            )
            
            # Success! Return the text
            return chat_completion.choices[0].message.content.strip()
            
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg:
                print(f"  [Groq Rate Limit. Waiting 10 seconds... (Attempt {attempt+1} of {max_retries})]")
                time.sleep(10) 
                continue
            else:
                print(f"  [Groq API Error]: {error_msg}")
                return full_text
                
    print("Max retries reached. Returning original text.")
    return full_text