from bs4 import BeautifulSoup
import requests, re
def retrieve_pdf(file):
#Criando a soup
    with open(file) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    #Encontrando a tag onde está o arquivo pdf
    tag = soup.find_all('a', {'href': re.compile('http://www.dom.salvador.ba.gov.br/images/stories/pdf/+([0-9]{4})+/+([a-z]*)+/+dom+-+([0-9]*)+-+([0-9]{2})+-+([0-9]{2})+-+([0-9]{4})+.+pdf')})

    #Passando o link do arquivo para uma lista de links
    links = [tags['href'] for tags in tag]
    first_link= links[0]

    #Transformando o link em um arquivo .pdf
    with open("dom.pdf", "wb") as pdf:
        response = requests.get(first_link)
        pdf.write(response.content)

