import time
from openai import OpenAI

def humanize_text(full_text, api_key):
    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key)
    
    prompt = f"""
    You are an expert editor rewriting a capstone project draft. Your goal is to produce a text that reads primarily as human but retains enough, structured characteristics to achieve at least a 20% AI detection score on platforms like ZeroGPT, Turnitin, JustDone.

    EXECUTION ALGORITHM:
    1. Maintain the use of plain words.
    2. Tone: Formal
    3. CITATION LOCK: Keep all citations completely untouched and formatted exactly as they are (e.g., (Cho et al., 2025)).
    4. BAN LIST(Avoid Using this words): delve, tapestry, testament, crucial, moreover, furthermore, beacon, landscape, multifaceted, comprehensive, robust, intricate, pivotal, dynamic, seamless, framework, utilize, facilitate, implement, wherein, thus, therefore, hence, rapid, vital.
    FULL DRAFT TEXT TO REWRITE:
    {full_text}

    CRITICAL OUTPUT RULE: Return ONLY the raw, revised full text. No markdown formatting, no conversational prefixes, no explanations.
    """
    
    # Retry logic
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini", # The fastest and most cost-effective OpenAI model
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.75,
                top_p=0.90,
            )
            
            # Success! Return the text
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg or "rate limit" in error_msg.lower():
                print(f"  [OpenAI Rate Limit. Waiting 10 seconds... (Attempt {attempt+1} of {max_retries})]")
                time.sleep(10) 
                continue
            else:
                print(f"  [OpenAI API Error]: {error_msg}")
                return full_text
                
    print("Max retries reached. Returning original text.")
    return full_text