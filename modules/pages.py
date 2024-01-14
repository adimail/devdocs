import streamlit as st
from modules.texString import generateLatexCode
from modules.utils import get_file_language, open_in_overleaf


def home_page():

    st.title("Welcome to dev docs! 🌐")
    st.subheader(
        "A tool for transforming source code into professionally typeset PDF documents.")
    st.divider()

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.header('How to use the site:')
            st.markdown(
                """
                1. _Upload your source code files_
                1. _Modify header content_
                1. _Click on `Convert to PDF` button from the sidebar._
                1. _You will be redirected to Overleaf._
                1. _On the Overleaf site, you can preview your document._
                1. _Download the PDF file._
                """
            )
        with col2:
            st.image('assets/download_pdf.png',
                     caption='Sunrise by the mountains')

    st.divider()

    st.header("Sample Work:")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image('assets/sample1.jpg',
                     caption='Page 1')

        with col2:
            st.image('assets/sample2.jpg',
                     caption='Page 2')

    st.divider()
    st.header("Developers Note:")

    st.markdown("""
    ### _**An account on [Overleaf](https://www.overleaf.com/) is required to render your document.**_
    ---
    """)

    st.markdown("""
        Hiya Stranger! Thank you for visiting.
                    
        13 Jan 2024:
        - I've been searching for an online compiler for LaTeX documents to render code into PDF format, but unfortunately, I couldn't find one.
        - Overleaf was the closest I got. However, their API doesn't allow direct PDF downloads from my page; users are redirected to the Overleaf editor.
        - Initially, I built a CLI tool using Golang, but the dependencies (xelatex, minktex) couldn't be packed into a single binary executable.
        - I then wrote a simple script:
            1. Read the source code.
            1. Insert snippets into the existing LaTeX template.
            1. Create a tex file using `transform.String(unicode.UTF16(unicode.LittleEndian, unicode.UseBOM).NewEncoder(), unicodeContent)`.
            1. Compile the tex file using `xelatex -shell-escape file.tex`
                - Golang: `cmd := exec.Command("xelatex", "-shell-escape", "file.tex")`
        - Check out the Golang CLI code on [GitHub](https://github.com/adimail/GoLang-DevDoc).
        - If you're curious about LaTeX, check their documentation [here](https://www.latex-project.org/about/).
        - LaTeX compilers:
            - [Overleaf](https://www.overleaf.com/learn/latex/Choosing_a_LaTeX_Compiler)
            - **MiKTeX for Windows**
            - **TeX Live for Linux and other UNIX-like systems**
            - **MacTeX** - Redistribution of TeX Live for macOS
            - **teTeX** - For Linux and other UNIX-like systems; it is no longer actively maintained
            - **proTeXt** - Based on MiKTeX
    """)


def document_uploader_page():
    st.title("Source Code to PDF converter")
    st.divider()

    h_top_left = ""
    h_center = ""
    h_top_right = ""
    Codelines = 52

    user_file_codes = []
    user_file_names = []
    user_file_languages = []

    uploaded_files = st.file_uploader(
        "Choose files", type=["py", "cpp", "js", "c", "ts", "go"], accept_multiple_files=True)

    unfilled_fields = []

    if uploaded_files:
        with st.expander("Customize your PDF", expanded=True):
            header = True
            if header:
                with st.container(border=True):
                    st.write(
                        "Header contents:")
                    with st.container():
                        col1, col2, col3 = st.columns(3)
                        tl_label = col1.checkbox("Top left", value=True)
                        tc_label = col2.checkbox("Center", value=True)
                        tr_label = col3.checkbox("Top right")

                    with st.container():
                        col1, col2, col3 = st.columns(3)

                        h_top_left = col1.text_input(
                            "Suggested: Name", disabled=not tl_label)
                        h_center = col2.text_input(
                            "Suggested: Subject", disabled=not tc_label)
                        h_top_right = col3.text_input(
                            "Suggested: Roll Number/date ", disabled=not tr_label)

                st.image('assets/info.png',
                         caption='Position of header contents')

            with st.container(border=True):
                st.write(
                    "Additional Features    :")
                with st.container():
                    col1, col2 = st.columns(2)
                    pagenumber = col1.checkbox(
                        "Page Numbers (Currently unavailable)")
                    col2.markdown(
                        "The page title is the file name by default. Change the title in [uploaded files](#uploaded-files) tab")

                with st.container():
                    col1, col2 = st.columns(2)

                    with col1:
                        with st.container(border=True):
                            pagenumberposition = st.radio(
                                "Position of page numbers",
                                ["Bottom Left", "Top Left", "Center",
                                    "Bottom right", "Disabled"],
                                index=1 if pagenumber else 4,
                                disabled=True
                            )

                    with col2:
                        with st.container(border=True):
                            Codelines = st.radio(
                                "Maximum number of lines of code on one page",
                                [52, 60, 69, 82, 110],
                                index=1,
                            )

        st.markdown(" --- ")

        if tl_label and not h_top_left:
            unfilled_fields.append("Top Left label")
        if tc_label and not h_center:
            unfilled_fields.append("Center label")
        if tr_label and not h_top_right:
            unfilled_fields.append("Top Right label")

        if unfilled_fields:
            st.sidebar.warning("Please fill in the following fields:")
            st.sidebar.markdown(
                "\n".join([f"- {field}" for field in unfilled_fields]), unsafe_allow_html=True)

        st.subheader("Uploaded Files")

        columns = st.columns(2)

        for i, file in enumerate(uploaded_files):
            with columns[i % 2].expander(f"{file.name}"):
                file_contents = file.read().decode("utf-8")

                edited_name = st.text_input(
                    f"Title of the program {i}", value=file.name)

                user_file_names.append(edited_name)

                language = get_file_language(file.name)
                st.code(file_contents, language=language, line_numbers=True)
                user_file_codes.append(file_contents)
                user_file_languages.append(language)

        latex_code = generateLatexCode(
            codes=user_file_codes,
            names=user_file_names,
            languages=user_file_languages,
            h_topleft=h_top_left,
            h_topright=h_top_right,
            h_center=h_center,
            fontsize=Codelines
        )

    if not unfilled_fields and uploaded_files:

        st.divider()

        with st.expander(label="View your Latex code", expanded=False):
            st.code(latex_code, language="latex", line_numbers=True)

        st.sidebar.success("Data is ready to be processed")
        btn = st.sidebar.button("Convert to PDF")
        if btn:
            open_in_overleaf(latex_code)

        st.sidebar.write(f"- Number of Files: {len(uploaded_files)}")

    else:
        st.sidebar.write(
            "Upload files and fill the details to proceed further")
        st.sidebar.button("Convert to PDF", disabled=True)


def about_page():
    st.title("About")
    st.divider()

    st.title("What is LaTeX")
    st.markdown(
        """
        LaTeX is a typesetting system widely used for the production of scientific and mathematical documents.
        It provides a high-level markup language for describing the structure and content of a document.
        LaTeX is particularly popular in academia for writing research papers, theses, and technical documents.

        ### Key Features:
        - **Professional Typesetting:** LaTeX produces high-quality documents with precise formatting and layout.
        - **Mathematical Typesetting:** It excels in rendering complex mathematical equations and symbols.
        - **Cross-Referencing:** LaTeX makes it easy to create cross-references within a document.
        - **Bibliography Management:** It has built-in support for managing bibliographies and citations.
        - **Template-Based:** LaTeX uses templates to maintain consistency and style in documents.
        """
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Resources')
        st.markdown(
            """
            - [LaTeX Project](https://www.latex-project.org/about/): Official LaTeX documentation and resources.
            - [Choosing a LaTeX Compiler](https://www.overleaf.com/learn/latex/Choosing_a_LaTeX_Compiler): Comparison of LaTeX compilers.
            - **MiKTeX:** LaTeX distribution for Windows.
            - **TeX Live:** LaTeX distribution for Linux and other UNIX-like systems.
            - **MacTeX:** Redistribution of TeX Live for macOS.
            - **teTeX:** Legacy LaTeX distribution (no longer actively maintained).
            - **proTeXt:** LaTeX distribution based on MiKTeX.
            """
        )

    with col2:
        st.subheader('How It Works')
        st.markdown(
            """
            1. **Markup Language:** Write your document using LaTeX markup language.
            2. **Compilation:** Compile the LaTeX source code using a LaTeX compiler (e.g., pdfLaTeX).
            3. **Output:** Obtain a professionally typeset document in PDF format.
            """
        )

    st.markdown(
        """
        LaTeX is a powerful tool for producing well-formatted and structured documents, especially in fields that require complex mathematical notations.
        """
    )
    st.divider()

    st.title("Developer")

    with st.container():
        col1, col2 = st.columns(2)
        col1.write('**Name:** [Aditya Godse](adimail.github.io)')
        col1.write(
            '**Contact:**    adimail2404@gmail.com')
