from fpdf import FPDF
from lego import Lego_func

pdf = FPDF()
pdf.add_page()
pdf.set_line_width(1)
pdf.set_draw_color(r=0, g=0, b=0)
# pdf.set_fill_color(r=172, g=120, b=186)
R,G,B=Lego_func()[13].RGB
pdf.set_fill_color(r=R,g=G,b=B)
for i in range(16):
    pdf.ellipse(x=10+i*12, y=10, w=10, h=10, style="FD")
    pdf.set_font("helvetica", "B", 18)
    if i<10:
        pdf.text(13.5+i*12, 17, f"{i}")
    else:
        pdf.text(11+i*12, 17, f"{i}")
    # pdf.ellipse(x=22, y=10, w=10, h=10, style="FD")
    # pdf.set_font("helvetica", "B", 25)
    # pdf.text(24.5, 18, "1")

pdf.output("circle.pdf")
# 172,120,186