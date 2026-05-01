import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

# Page config (hides default clutter)
st.set_page_config(
    page_title="Bio Chapter 3",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit menu/footer + file style UI
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# Load HTML file
html_file = Path("bio_ch_3.html")

if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")

    # Render HTML as full webpage inside Streamlit
    components.html(html_content, height=1000, scrolling=True)
else:
    st.error("HTML file not found. Make sure 'bio_ch_3.html' is in the same repo folder as app.py.")
