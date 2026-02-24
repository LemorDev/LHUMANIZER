import requests
import re

def split_into_sentences(text):
    return re.split(r'(?<=[.!?]) +', text)

def analyze_text(text, api_key):
    url = "https://api.sapling.ai/api/v1/aidetect"
    payload = {
        "key": api_key,
        "text": text
    }
    
    response = requests.post(url, json=payload)
    data = response.json()
    
    # --- THE FIX: Catch the error so it doesn't default to 0% ---
    if "error" in data or "msg" in data:
        print(f"  [Sapling API Error / Rate Limit]: {data}")
        # Return 100% so the loop doesn't automatically exit
        return 1.0, [] 
    
    overall_score = data.get("score", 0) 
    sentence_scores = data.get("sentence_scores", [])
    
    return overall_score, sentence_scores

def get_flagged_sentences(sentence_scores, threshold=0.60):
    flagged = []
    # Enumerate through Sapling's list to grab the index of the bad sentences
    for index, item in enumerate(sentence_scores):
        if item.get('score', 0) > threshold:
            flagged.append(index)
    return flagged