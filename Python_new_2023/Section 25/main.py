from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("files(.txt)/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    name = filename.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=name)

pdf.output("output.pdf")
