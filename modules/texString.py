def generateLatexCode(codes=[], names=[], languages=[], section_info=[], style="helvet",  h_topleft=None, h_center=None, h_topright=None, fontsize=None, pagenumbers=False):

    fontsize_dict = {
        52: '',
        69: '\\footnotesize',
        60: '\\small',
        82: '\\scriptsize',
        110: '\\tiny'
    }

    fontstyle_dict = {
        'Helvetica (Sans-serif)': 'helvet',
        'Times New Roman (Serif)': 'times',
    }

    style = fontstyle_dict[style]
    fontsize = fontsize_dict[fontsize]
    major_list = list(zip(codes, names, languages, section_info))

    comment = "\n"
    if style == "times":
        comment = "\n%"

    head = r'''
            
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%            ____               ____
%           |  _ \  _____   __ |  _ \  ___   ___
%           | | | |/ _ \ \ / / | | | |/ _ \ / __|
%           | |_| |  __/\ V /  | |_| | (_) | (__
%           |____/ \___| \_/   |____/ \___/ \___|
%  Made with love by your friendly neighborhood spider man
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\documentclass{article}
\usepackage[margin=0.68in]{geometry}
\usepackage{minted}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{graphicx}

\usepackage{''' + f'{style}' + r'''}'''
    head += comment
    head += r'''\renewcommand{\rmdefault}{\sfdefault}
% You can experiment with fonts by commenting out the above line

\usemintedstyle{colorful}
\pagestyle{fancy}
\fancyhf{}

% Header content goes here
\lhead{\vspace{8pt} ''' + f"{h_topleft}" + r'''}
\chead{\vspace{16pt}\fontsize{16}{18}\selectfont ''' + f"{h_center}" + r'''}
\rhead{\vspace{8pt} ''' + f"{h_topright}" + r'''}

\setlength{\headheight}{34.0pt}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\begin{document}

%   If you would like to give numbers to each section, 
%   remove the aestrick (*) after each section.
%   
%   For example: 
%      \section*{Title with number}
%      \section{Title without number}
'''

    template_string = ""

    for element in major_list:
        template_string += r'''\section*{''' + f"{element[1]}" + '}\n'
        template_string += element[3]
        template_string += '\n'
        template_string += r'''\begin{minted}[bgcolor=backcolour,linenos,frame=none,fontsize='''
        template_string += fontsize
        template_string += r''',breaklines]{''' + f"{element[2]}" + r'''}
''' + f"{element[0]}" + r'''
\end{minted}
\newpage
'''

    return head + template_string + r'\end{document}'
