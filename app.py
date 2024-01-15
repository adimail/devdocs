import streamlit as st
from modules.pages import home_page
from modules.pages import about_page
from modules.pages import document_uploader_page
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Dev Docs",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    if 'uploaded_files' not in st.session_state:
        st.session_state.uploaded_files = []
    if 'include_name' not in st.session_state:
        st.session_state.include_name = False
    if 'include_subject' not in st.session_state:
        st.session_state.include_subject = False
    if 'include_roll_number' not in st.session_state:
        st.session_state.include_roll_number = False
    if 'user_name' not in st.session_state:
        st.session_state.user_name = ""
    if 'subject' not in st.session_state:
        st.session_state.subject = ""
    if 'roll_number' not in st.session_state:
        st.session_state.roll_number = ""

    with st.sidebar:
        page = option_menu(
            "Dev Docs", ["Home", "Converter", "About"],
            icons=["house-door-fill", "tools", "info-circle-fill"],
            menu_icon="file-earmark-code-fill",
            default_index=1
        )
        overleaf_registration_page = "https://www.overleaf.com/register"

        st.markdown(
            f'''<a href="{overleaf_registration_page}" target="_blank">
                <button
                    style="
                        width: 100%;
                        background-color: #475caa;
                        color: white;
                        padding: 8px 16px;
                        border-radius: 15px;
                        border: none;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 16px;
                        margin: 4px 2px;
                        cursor: pointer;
                    ">Create Overleaf account</button>
            </a>''',
            unsafe_allow_html=True
        )
        st.divider()

    if page == "Home":
        home_page()
    elif page == "Converter":
        document_uploader_page()
    elif page == "About":
        about_page()


if __name__ == "__main__":
    main()
