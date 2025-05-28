import streamlit as st

def hide_sidebar_and_controls():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    st.markdown("""
        <style>
            /* Dölj hela sidebar */
            [data-testid="stSidebar"] {
                display: none !important;
            }

            /* Dölj sidopanelens öppningsknapp i alla former */
            button[title="Open sidebar"] {
                display: none !important;
            }

            /* Dölj också nya UI-knappar (extra säkerhet) */
            button[kind="icon"] {
                display: none !important;
            }

            /* Dölj header och toolbar om pil sitter där */
            header, div[data-testid="stToolbar"] {
                display: none !important;
            }

            /* Dölj manuellt placerad toggle-knapp */
            section > div:first-child > button {
                display: none !important;
            }

            /* Dölj top-marginal ifall något sticker ut */
            .block-container {
                padding-top: 1rem !important;
            }
        </style>
    """, unsafe_allow_html=True)
