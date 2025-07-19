from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder

pdf_path = r"C:\Users\ADARSH\OneDrive\Desktop\Python course\pdf merger\crazyones.pdf"

reader = PdfReader(pdf_path)
page = reader.pages[0]

writer = PdfWriter()
writer.add_page(page)

annotation = AnnotationBuilder.free_text(
    "Hello World\nThis is the second line!",
    rect=(50, 550, 200, 650),
    font="Arial",
    bold=True,
    italic=True,
    font_size="20pt",
    font_color="00ff00",
    border_color="0000ff",
    background_color="cdcdcd",
)

writer.add_annotation(page_number=0, annotation=annotation)

with open("annotated-pdf.pdf", "wb") as fp:
    writer.write(fp)

print("Annotated PDF saved as annotated-pdf.pdf")
