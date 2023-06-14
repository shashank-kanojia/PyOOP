import webbrowser

from fpdf import FPDF


class PDFReport:
    """
    Contains data about the flatmates, like their names, period of stay, and their contribution towards the total bill.
    """

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def pdf_generator(self, list_flatmates: list, bill):
        pdf = FPDF(orientation='p', unit='pt', format='A4')
        pdf.add_page()

        # Add a logo
        pdf.image(name='Images\\house.png', h=60, w=60)

        # Adding the title
        pdf.set_font(family='Arial', size=36, style='B')
        pdf.cell(w=0, h=66, txt='Flatmates\' share of the bill', border=1, align='C', ln=1)

        pdf.set_font(family='Arial', size=16)
        pdf.cell(w=120, h=66, txt=' Period: ', border=1)

        pdf.set_font(family='Arial', size=16, style='B')
        pdf.cell(w=150, h=66, txt=f' {bill.period}', border=1)

        pdf.set_font(family='Arial', size=16)
        pdf.cell(w=150, h=66, txt=' Bill Amount: ', border=1)

        pdf.set_font(family='Arial', size=16, style='B')
        pdf.cell(w=0, h=66, txt=f' INR {bill.amount}', border=1, ln=1)

        pdf.cell(w=0, h=30, txt='', border=0, ln=1)

        pdf.set_font(family='Arial', size=20, style='B')
        pdf.cell(w=0, h=66, txt=' Bill Summary:', border=0, ln=1)
        pdf.cell(w=150, h=66, txt=' Person', border=1)
        pdf.cell(w=200, h=66, txt=' Amount to be paid', border=1, ln=1)

        pdf.set_font(family='Arial', size=16)
        for flatmate_index in range(len(list_flatmates)):
            pdf.cell(w=150, h=66, txt=f' {list_flatmates[flatmate_index].name}', border=1)
            pdf.cell(w=200, h=66, txt=f' INR {list_flatmates[flatmate_index].pays(bill, [x for i, x in enumerate(list_flatmates) if i != flatmate_index])}', border=1, ln=1)

        pdf.output(f'{self.filename}')

        webbrowser.open(f'{self.filename}')
