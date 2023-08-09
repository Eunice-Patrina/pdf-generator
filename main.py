from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

topics = pd.read_csv("topics.csv")

for index, topic in topics.iterrows():
    pdf.add_page()

    # adds Header
    pdf.set_font(family="Times", style='B', size=24)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=0, h=12, txt=topic["Topic"], ln=1)
    pdf.line(10, 21, 200, 21)

pdf.output("output.pdf")

