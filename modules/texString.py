def generateLatexCode(codes=[], names=[], languages=[], h_topleft=None, h_center=None, h_topright=None, fontsize=None, pagenumbers=False):

    if fontsize == 52:
        fontsize = ''
    elif fontsize == 69:
        fontsize = '\\footnotesize'
    elif fontsize == 60:
        fontsize = '\\small'
    elif fontsize == 82:
        fontsize = '\\scriptsize'
    elif fontsize == 110:
        fontsize = '\\tiny'
    else:
        fontsize = ''

    major_list = list(zip(codes, names, languages))

    head = r'''
\documentclass{article}
\usepackage[margin=0.68in]{geometry}
\usepackage{minted}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{graphicx}

\usemintedstyle{colorful}
\pagestyle{fancy}
\fancyhf{}
\lhead{\vspace{8pt} ''' + f"{h_topleft}" + r'''}
\chead{\vspace{16pt}\fontsize{16}{18}\selectfont ''' + f"{h_center}" + r'''}
\rhead{\vspace{8pt} ''' + f"{h_topright}" + r'''}

\setlength{\headheight}{34.0pt}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\begin{document}
'''

    template_string = ""

    for element in major_list:
        template_string += r'''
\section*{''' + f"{element[1]}" + r'''}
\begin{minted}[bgcolor=backcolour,linenos,frame=none,fontsize=''' + fontsize + r''']{''' + f"{element[2]}" + r'''}
''' + f"{element[0]}" + r'''
\end{minted}
\newpage
'''

    return head + template_string + r'\end{document}'
