from fpdf import FPDF
import pandas as pd

# Main doc
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

# Read .cvs file
df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    # Header
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=24, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 27, 200, 27)
    # Multiple lines
    for line in range(34, 270, 7):
        pdf.set_draw_color(100, 100, 100)
        pdf.line(10, line, 200, line)

    # Footer
    pdf.ln(250)
    pdf.set_font(family='Times', style='I', size=10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        # Footer
        pdf.ln(270)
        pdf.set_font(family='Times', style='I', size=10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')
        # Multiple lines
        for line in range(27, 270, 7):
            pdf.set_draw_color(100, 100, 100)
            pdf.line(10, line, 200, line)


pdf.output('output.pdf')
