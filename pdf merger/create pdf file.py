from PyPDF2 import PdfWriter

# Create a blank PDF with one page
writer = PdfWriter()
writer.add_blank_page(width=600, height=800)

# Save it as crazyones.pdf
with open("crazyones.pdf", "wb") as f:
    writer.write(f)

print("PDF created: crazyones.pdf")
