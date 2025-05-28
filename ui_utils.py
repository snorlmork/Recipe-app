import streamlit as st

def hide_page_from_sidebar(page_title: str):
    st.markdown(f"""
        <script>
            const hideLink = () => {{
                const items = window.parent.document.querySelectorAll('section[data-testid="stSidebar"] ul li');
                items.forEach(item => {{
                    const text = item.innerText.trim();
                    if (text === "{page_title}") {{
                        item.style.display = "none";
                    }}
                }});
            }};
            const observer = new MutationObserver(hideLink);
            observer.observe(window.parent.document, {{ childList: true, subtree: true }});
            setTimeout(hideLink, 1000);
        </script>
    """, unsafe_allow_html=True)
