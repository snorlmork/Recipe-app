import streamlit as st

def hide_page_from_sidebar(page_title: str):
    st.markdown(f"""
        <script>
            window.addEventListener("load", function() {{
                const links = window.parent.document.querySelectorAll("section[data-testid='stSidebar'] ul li a span");
                links.forEach(el => {{
                    if (el.innerText === "{page_title}") {{
                        el.parentElement.parentElement.style.display = "none";
                    }}
                }});
            }});
        </script>
    """, unsafe_allow_html=True)
