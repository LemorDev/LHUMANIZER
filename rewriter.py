import time
import logging
from typing import Optional
from groq import Groq

# Set up basic logging to replace print statements
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def humanize_text(
    full_text: str, 
    api_key: str, 
    model: str = "llama-3.3-70b-versatile",
    temperature: float = 0.75,
    max_retries: int = 3
) -> str:
    """
    Rewrites a text using the Groq API to achieve a polished, academic tone
    that retains around 20% AI detection characteristics.

    Args:
        full_text (str): The draft text to be rewritten.
        api_key (str): The Groq API key.
        model (str): The model to use for completion.
        temperature (float): The temperature for generation.
        max_retries (int): Maximum number of retries for API rate limits.

    Returns:
        str: The rewritten text, or the original text if all retries fail.
    """
    # Initialize the Groq client
    client = Groq(api_key=api_key)

    # The prompt is updated to target ~20% AI detection by maintaining 
    # AI-typical structures, perfect grammar, and formal vocabulary.
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

    for attempt in range(max_retries):
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=model,
                temperature=temperature,
                top_p=0.90,
            )

            # Success! Return the safely extracted text
            content = chat_completion.choices[0].message.content
            return content.strip() if content else full_text

        except Exception as e:
            error_msg = str(e)
            # Check for rate limit status code or keywords
            if "429" in error_msg or "rate limit" in error_msg.lower():
                # Exponential backoff: 10s, 20s, 40s
                wait_time = 10 * (2 ** attempt)  
                logging.warning(f"Groq Rate Limit encountered. Waiting {wait_time} seconds... (Attempt {attempt + 1} of {max_retries})")
                time.sleep(wait_time)
                continue
            else:
                # Catch-all for authentication errors, bad requests, etc.
                logging.error(f"Groq API Error: {error_msg}")
                return full_text

    logging.warning("Max retries reached. Returning original text.")
    return full_text
