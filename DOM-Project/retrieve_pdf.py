from bs4 import BeautifulSoup
import requests
import re
from io import *
from pdf2str import pdf2txt


def retrieve_pdf(url:str):
    #Criando a soup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print("Soup creation done!")
    #Encontrando a tag onde está o arquivo pdf
    link_regex = re.compile('http://www.dom.salvador.ba.gov.br/images/stories/pdf/+([0-9]{4})+/+([a-z]*)+/+dom+-+([0-9]*)+-+([0-9]{2})+-+([0-9]{2})+-+([0-9]{4})+.+pdf')
    dom_name_regex = re.compile('dom+-+([0-9]*)+-+([0-9]{2})+-+([0-9]{2})+-+([0-9]{4})')
    print("RegEx done!")
    tag = soup.find_all('a', {'href': link_regex})
    #Passando o link do arquivo para uma lista de links
    links: list[str] = [tags['href'] for tags in tag]
    first_link: str = links[0]
    print("Link found")
    dom_name: str = dom_name_regex.search(first_link).group()
    print("Diary name done")
    response = requests.get(first_link)
    content = BytesIO(response.content)
    print("PDF file wrote!")
    pdf_string: str = pdf2txt(content)
    print("PDF string retrieved!")
    return dom_name, pdf_string
