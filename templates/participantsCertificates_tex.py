def participant(name_string = 'Vorname Nachname', compName = 'Test Comp', highestRank_string = 'Place Event Test', backgroundImg_path = '/Users/annikastein/Documents/Speedcubing/Competitions/RLP25/Urkunden/certificate_RLP25.pdf'):
    tex_string = f'''{chr(92)}documentclass[a4paper,14pt,landscape]{{scrarticle}}
{chr(92)}usepackage[top=2cm, bottom=2cm, outer=0cm, inner=0cm]{{geometry}}
{chr(92)}pagestyle{{empty}}
{chr(92)}usepackage[T1,T2A]{{fontenc}}
{chr(92)}usepackage[utf8]{{inputenc}}
{chr(92)}usepackage[english, russian]{{babel}}
{chr(92)}usepackage{{CJKutf8}}
{chr(92)}usepackage{{tgpagella}} % Default fonts
{chr(92)}usepackage{{cmbright}} % sans serif everywhere
{chr(92)}usepackage{{helvet}}
{chr(92)}usepackage{{FiraSans}}
{chr(92)}usepackage{{xcolor}}

{chr(92)}usepackage{{graphicx}}
{chr(92)}AddToHook{{shipout/background}}{{%
	{chr(92)}put(0,-{chr(92)}paperheight){{{chr(92)}includegraphics[width={chr(92)}paperwidth]{{ {backgroundImg_path} }}}}}}

{chr(92)}begin{{document}}
{chr(92)}centering{{
{chr(92)}selectlanguage{{english}}
{chr(92)} {chr(92)}{chr(92)} {chr(92)} {chr(92)}vspace{{7cm}} {chr(92)}{chr(92)}
    This is to certify that{chr(92)} {chr(92)}vspace{{1.7cm}} {chr(92)}{chr(92)}{{
    {chr(92)}Huge {{
        {chr(92)}textbf{{{name_string}}}}}}}{chr(92)}vspace{{1.7cm}} {chr(92)}{chr(92)}
        has successfully participated in the WCA Competition {compName}.{chr(92)}{chr(92)} {chr(92)} {chr(92)}{chr(92)}
        Highest rank achieved at this competition: {highestRank_string}.{chr(92)}{chr(92)} {chr(92)} {chr(92)}{chr(92)}
        {chr(92)}color{{orange}}Congratulations!}}
{chr(92)}end{{document}}
'''
    return tex_string

def participant_outdated(name_string = 'Vorname Nachname', compName = 'Test Comp', highestRank_string = 'Place Event Test', backgroundImg_path = '/Users/annikastein/Documents/Speedcubing/Competitions/RLP25/Urkunden/certificate_RLP25.pdf'):
    tex_string = f'''{chr(92)}documentclass[a4paper,14pt,landscape]{{scrarticle}}
{chr(92)}usepackage[top=2cm, bottom=2cm, outer=0cm, inner=0cm]{{geometry}}
{chr(92)}usepackage[pages=some,placement=top]{{background}}
{chr(92)}pagestyle{{empty}}
{chr(92)}usepackage[T1,T2A]{{fontenc}}
{chr(92)}usepackage[utf8]{{inputenc}}
{chr(92)}usepackage[english, russian]{{babel}}
{chr(92)}usepackage{{CJKutf8}}
{chr(92)}usepackage{{tgpagella}} % Default fonts
{chr(92)}usepackage{{cmbright}} % sans serif everywhere
{chr(92)}usepackage{{helvet}}
{chr(92)}usepackage{{FiraSans}}
{chr(92)}usepackage{{xcolor}}

{chr(92)}backgroundsetup{{
scale=1,
color=black,
opacity=1,
angle=0,
contents={{{chr(92)}includegraphics[width={chr(92)}paperwidth,height={chr(92)}paperheight]{{{backgroundImg_path}}}}}
}}

{chr(92)}begin{{document}}

{chr(92)}BgThispage
{chr(92)}centering{{
{chr(92)}selectlanguage{{english}}
{chr(92)} {chr(92)}{chr(92)} {chr(92)} {chr(92)}vspace{{7cm}} {chr(92)}{chr(92)}
    This is to certify that{chr(92)} {chr(92)}vspace{{1.7cm}} {chr(92)}{chr(92)}{{
    {chr(92)}Huge {{
        {chr(92)}textbf{{{name_string}}}}}}}{chr(92)}vspace{{1.7cm}} {chr(92)}{chr(92)}
        has successfully participated in the WCA Competition {compName}.{chr(92)}{chr(92)} {chr(92)} {chr(92)}{chr(92)}
        Highest rank achieved at this competition: {highestRank_string}.{chr(92)}{chr(92)} {chr(92)} {chr(92)}{chr(92)}
        {chr(92)}color{{orange}}Congratulations!}}
{chr(92)}clearpage
{chr(92)}end{{document}}
'''
    return tex_string
