from retrieve_html import write_html
from retrieve_pdf import retrieve_pdf
from pdf2str import pdf2txt
import re
from pdfclass import PDF
import pymongo
client = pymongo.MongoClient()
db = client['PDF_Database']
collection = db['DOM_text']

#url = "http://www.dom.salvador.ba.gov.br/"
#write_html(url)
#retrieve_pdf("dom.html")
#pdf_string = pdf2txt("dom.pdf")

#with open("text_pdf.txt", encoding='utf-8') as file:
#    pdf_string = file.read()

#pdf = PDF(pdf_string)

#post = {
#    "Ano de publicação": pdf.ano_dom,
#    "Número de páginas": pdf.page_count,
#    "Conteúdo das páginas": pdf.pages[1::],
#    "Sumário": pdf.summary,
#}
#posts = db.posts
#post_id = posts.insert_one(post).inserted_id
#post_id










#definir atributos para a classe
#summary DONE
#summary_topic
#summary_index DONE
#page DONE
#page_count DONE


