def front_nametags(inside_tex_string):
    tex_string = f'''{chr(92)}documentclass[a4paper,12pt]{{article}}
{chr(92)}usepackage[T1,T2A]{{fontenc}}

{chr(92)}usepackage[utf8]{{inputenc}}
{chr(92)}usepackage[english, russian]{{babel}}
{chr(92)}usepackage{{CJKutf8}}
{chr(92)}usepackage{{tgpagella}} % Default fonts
{chr(92)}usepackage{{cmbright}} % sans serif everywhere
{chr(92)}usepackage{{helvet}}
{chr(92)}usepackage{{FiraSans}}

{chr(92)}usepackage{{tipa}}
{chr(92)}usepackage{{newunicodechar}}
{chr(92)}newunicodechar{{ə}}{{{chr(92)}textschwa}}

{chr(92)}usepackage[dvipsnames]{{xcolor}}
{chr(92)}usepackage[newdimens]{{labels}}
{chr(92)}usepackage{{xpatch}}

{chr(92)}makeatletter
{chr(92)}xpatchcmd{{{chr(92)}BuildB@x}}{{{chr(92)}vss}}{{}}{{}}{{}}
{chr(92)}makeatother
{chr(92)}LabelGridtrue
{chr(92)}LabelCols=2
{chr(92)}LabelRows=5
{chr(92)}LeftPageMargin=12mm
{chr(92)}RightPageMargin=12mm
{chr(92)}TopPageMargin=2mm
{chr(92)}BottomPageMargin=2mm
{chr(92)}InterLabelRow=0mm
{chr(92)}LeftLabelBorder=0mm
{chr(92)}RightLabelBorder=0mm
{chr(92)}TopLabelBorder=1mm
{chr(92)}BottomLabelBorder=1mm
% Create an empty label; for if the label has already been used
{chr(92)}newcommand{{{chr(92)}emptylabel}}{{{chr(92)}rule{{0mm}}{{22mm}}}}

{chr(92)}usepackage{{adjustbox}}

{chr(92)}begin{{document}}
% This is where your labels go

{inside_tex_string}

{chr(92)}end{{document}}
'''
    return tex_string

def back_nametags(inside_tex_string):
    tex_string = f'''{chr(92)}documentclass[a4paper,9pt]{{scrarticle}}
{chr(92)}usepackage[T1,T2A]{{fontenc}}

{chr(92)}usepackage[utf8]{{inputenc}}
{chr(92)}usepackage[english, russian]{{babel}}
{chr(92)}usepackage{{CJKutf8}}
{chr(92)}usepackage{{tgpagella}} % Default fonts
{chr(92)}usepackage{{cmbright}} % sans serif everywhere
{chr(92)}usepackage{{helvet}}
{chr(92)}usepackage{{FiraSans}}

{chr(92)}usepackage[table,xcdraw,dvipsnames]{{xcolor}}
{chr(92)}usepackage[newdimens]{{labels}}
{chr(92)}usepackage{{xpatch}}

{chr(92)}makeatletter
{chr(92)}xpatchcmd{{{chr(92)}BuildB@x}}{{{chr(92)}vss}}{{}}{{}}{{}}
{chr(92)}makeatother
{chr(92)}LabelGridtrue
{chr(92)}LabelCols=2
{chr(92)}LabelRows=5
{chr(92)}LeftPageMargin=12mm
{chr(92)}RightPageMargin=12mm
{chr(92)}TopPageMargin=2mm
{chr(92)}BottomPageMargin=2mm
{chr(92)}InterLabelRow=0mm
{chr(92)}LeftLabelBorder=0mm
{chr(92)}RightLabelBorder=0mm
{chr(92)}TopLabelBorder=1mm
{chr(92)}BottomLabelBorder=1mm
% Create an empty label; for if the label has already been used
{chr(92)}newcommand{{{chr(92)}emptylabel}}{{{chr(92)}rule{{0mm}}{{22mm}}}}

{chr(92)}usepackage{{adjustbox}}
{chr(92)}usepackage{{float}}
{chr(92)}usepackage{{multirow}}
{chr(92)}usepackage{{graphicx}}
{chr(92)}usepackage{{svg}}

{chr(92)}begin{{document}}
% This is where your labels go

{inside_tex_string}

{chr(92)}end{{document}}
'''
    return tex_string

def merged_nametags(inside_tex_string):
    tex_string = f'''{chr(92)}documentclass[11pt,a4paper,oneside,DIV=12,BCOR=5mm,pdftex]{{scrreprt}}
{chr(92)}usepackage{{pdfpages}}
{chr(92)}begin{{document}}
% put the output of labelsPDFmerger.py here

{inside_tex_string}

{chr(92)}end{{document}}
'''
    return tex_string
