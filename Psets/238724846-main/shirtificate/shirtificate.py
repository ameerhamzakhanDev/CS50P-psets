from fpdf import FPDF
from PIL import Image


class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 70, 100, 450)
        self.set_font("helvetica", "B", 100)
        self.cell(0, 30, "CS50 Shitificate", ln=True, align="C")



def main():
    name = input("Enter thine name: ")
    create_pdf(name)


def create_pdf(name):
    img = Image.open("shirtificate.png")

    pdf = PDF("P", "mm", img.size)

    pdf.add_page()
    pdf.set_font("helvetica", "", 60)
    pdf.set_text_color(255, 255, 255)

    pdf.cell(0, 500, f'{name} took CS50', align='C')

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
