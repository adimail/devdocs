import os
import streamlit as st
import streamlit.components.v1 as components


def open_in_overleaf(latex_file):
    with st.sidebar.expander(label="open in overleaf", expanded=True):
        components.html(
            f"""
            <style>
                form {{
                    margin: 0;
                    padding: 0;
                    text-align: center; /* Center the button */
                }}
                input[type="submit"] {{
                    width: 100%;
                    background-color: #fff;
                    color: black;
                    padding: 10px 20px;
                    border: none;
                    cursor: pointer;
                }}
            </style>
            <script>
                document.addEventListener("DOMContentLoaded", function() {{
                    document.getElementById("overleaf-form").submit();
                }});
            </script>
            <form id="overleaf-form" action="https://www.overleaf.com/docs" method="post" target="_blank">
                <textarea rows="10" cols="60" name="snip" style="display: none;">
                {latex_file}
                </textarea>
                <input type="submit" value="Open in Overleaf">
            </form>
            """,
            height=50
        )


def get_file_language(file_name):
    file_extension = get_file_extension(file_name)

    language_mapping = {
        "py": "python",
        "cpp": "cpp",
        "js": "javascript",
        "c": "c",
        "ts": "typescript"
    }
    return language_mapping.get(file_extension, "plaintext")


def get_file_extension(file_name):
    _, file_extension = os.path.splitext(file_name)
    return file_extension.lstrip(".").lower()
