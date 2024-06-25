from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
def pdf2str(pdf_file):
    pdf_rm = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(pdf_rm, retstr, laparams=laparams)
    process_pdf(pdf_rm, device, pdf_file)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content

def pdf2txt(file):
    pdf = open(file,'rb')
    pdf_string = pdf2str(pdf_file=pdf)
    with open("text_pdf.txt", 'w', encoding='utf-8') as txtfile:
        txtfile.write(pdf_string)
    pdf.close()
    return pdf_string