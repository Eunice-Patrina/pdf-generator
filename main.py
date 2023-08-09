from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

topics = pd.read_csv("topics.csv")

for index, topic in topics.iterrows():

    # add multiple pages
    for page in range(topic["Pages"]):
        pdf.add_page()

        # first page of topic
        if(not page):
            # adds Header
            pdf.set_font(family="Times", style='B', size=24)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(w=0, h=12, txt=topic["Topic"])

        # add ruling lines to pages
        for i in range(21, 290, 12):
            pdf.line(10, i, 200, i)

        # add footer
        pdf.ln(277)
        pdf.set_font(family="Times", style='I', size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=topic["Topic"], align="R")

pdf.output("output.pdf")

