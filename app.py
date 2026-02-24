import os
import streamlit as st
from dotenv import load_dotenv
from rewriter import humanize_text # Imports your existing Groq logic

# Load your Groq key
load_dotenv()
LLM_KEY = os.getenv("GROQ_API_KEY")

# --- WEB PAGE CONFIGURATION ---
st.set_page_config(page_title="AI Humanizer", page_icon="📝", layout="centered")

st.title("Academic AI Humanizer")
st.markdown("Bypass AI detectors by transforming robotic drafts into natural, human-written academic prose. Perfect for capstone and thesis documentation.")
st.markdown("Made by: Lemor")
# --- USER INPUT AREA ---
draft_text = st.text_area("Paste your draft text below:", height=250, placeholder="Enter the text you want to humanize here...")

# --- ACTION BUTTON ---
if st.button("Humanize Text 🚀"):
    if not draft_text.strip():
        st.warning("⚠️ Please paste some text first!")
    elif not LLM_KEY:
        st.error("❌ Groq API key not found. Please check your .env file.")
    else:
        # Show a loading spinner while the API works
        with st.spinner("Humanizing your text... please wait..."):
            
            # Call your one-shot function
            humanized_result = humanize_text(draft_text, LLM_KEY)
            
            st.success("✅ Humanization Complete!")
            
            # --- OUTPUT AREA ---
            st.subheader("Final Humanized Text:")
            st.info(humanized_result)