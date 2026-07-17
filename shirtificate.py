from fpdf import FPDF


def main():
    name = input('Name: ')

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    pdf.set_font("helvetica", style="B", size=16)
    pdf.cell(0, 57, 'CS50 Shirtificate', align='C')

    pdf.image('shirtificate.png', x=10, y=70, w=190)

    pdf.set_font("Helvetica", style="B", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 160, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
