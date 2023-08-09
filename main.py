from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()
pdf.output("output.pdf")

