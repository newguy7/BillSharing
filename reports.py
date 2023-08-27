#to generate pdf
from fpdf import FPDF
#to automatically open pdf file generated
import webbrowser
#to perform action with files and directories
import os

class PdfReport:
    """
    Creates a pdf file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Add icon
        pdf.image("App-2-Flatmates-Bill/files/house.png", w=30, h=30)
        #pdf.image("files/house.png", w=30, h=30)

        #Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Utility Bill', border=0, align="C", ln=1)

        #Insert Period Label and Value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:",border=0)
        #adding another cell in the same row using ln=1
        pdf.cell(w=150, h=40, txt=bill.period, border=0, align="C", ln=1)

        #Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name,border=0)
        pdf.cell(w=150, h=25, txt="$" + flatmate1_pay, border=0, align="C", ln=1)

        #Insert name and due amount of the second flatmate        
        pdf.cell(w=100, h=25, txt=flatmate2.name,border=0)
        pdf.cell(w=150, h=25, txt="$" + flatmate2_pay, border=0, align="C", ln=1)

        os.chdir("App-2-Flatmates-Bill/files")
        #os.chdir("files")
        pdf.output(self.filename)
        #pdf.output(f"App-2-Flatmates-Bill/files/{self.filename}")

        #Automatically open the generated pdf file
        # edge_path = "C:\Program Files (x86)/Microsoft/Edge/Application"
        # webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
        # webbrowser.get('edge').open(self.filename, 0)

        
        webbrowser.open(self.filename)