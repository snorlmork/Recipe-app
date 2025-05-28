import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"] { display: none !important; }
        button[title="Open sidebar"] { display: none !important; }
        button[kind="icon"] { display: none !important; }
        header, div[data-testid="stToolbar"] { display: none !important; }
        section > div:first-child > button { display: none !important; }
        .block-container { padding-top: 1rem !important; }
    </style>
""", unsafe_allow_html=True)

st.write("✅ Sidebar and toggle button nuked.")
