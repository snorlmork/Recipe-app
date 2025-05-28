import streamlit as st

def hide_sidebar_and_controls():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    st.markdown("""
        <style>
            /* Dölj sidopanelen */
            [data-testid="stSidebar"] {
                display: none !important;
            }

            /* Dölj pil/hamburgermenyn i vänstra hörnet */
            [data-testid="collapsedControl"] {
                display: none !important;
            }

            /* Dölj huvudmenyn (ex. File, Help etc.) */
            #MainMenu {
                display: none !important;
            }

            /* Dölj toolbar-rad överst */
            div[data-testid="stToolbar"] {
                display: none !important;
            }

            /* Dölj header helt (pilen visas där) */
            header {
                display: none !important;
            }
        </style>
    """, unsafe_allow_html=True)
