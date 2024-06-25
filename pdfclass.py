import re


class PDF:

    def __init__(self, pdfstring):
        # Atributos a serem criados para o objeto PDF
        self.pdf_string = pdfstring
        self.ano_dom = self.define_year_dom()
        self.page_count = self.define_page_count()
        self.pages = self.create_pdf_pages()
        self.summary = self.pages[0]
        self.summary_text = self.summary[0]
        self.summary_index = self.summary[1]

    def define_year_dom(self):
        ano_dom_regex = re.compile('ANO\s[X|I|V]+')
        ano_dom = ano_dom_regex.search(self.pdf_string).group()
        return ano_dom

    def define_page_count(self):
        page_count = self.pdf_string.count(self.ano_dom)
        return page_count

    def create_pdf_pages(self):
        summary_text_start = self.pdf_string.find('\n')
        summary_text_end = self.pdf_string.find('2') - 4
        summary_text = self.pdf_string[summary_text_start:summary_text_end]
        summary_index_start = summary_text_end
        summary_index_end = self.pdf_string.find(self.ano_dom) - 54
        summary_index = self.pdf_string[summary_index_start:summary_index_end]
        ano_dom_pages_regex = re.compile(f'DIÁRIO OFICIAL DOSALVADOR-BAHIASEXTA-FEIRA21 DE JUNHO DE 2024{self.ano_dom}')
        ano_dom_pages = ano_dom_pages_regex.search(self.pdf_string).group()

        # excluindo o sumário do pdf_string
        pdf_string = self.pdf_string[summary_index_end::]

        # criando a lista de páginas
        pages = [[summary_text, summary_index]]

        # criando a primeira página
        next_page = pdf_string.find(ano_dom_pages)
        page = pdf_string[:next_page:]
        pages.append(page)
        pdf_string = pdf_string[next_page::]

        # criando as próximas páginas, precisa inserir um deslocamento para ele não encontrar o começo da própria página
        for n in range(self.page_count - 3):
            next_page = pdf_string[10:].find(ano_dom_pages)
            page = pdf_string[:next_page + 10:]
            pages.append(page)
            pdf_string = pdf_string[next_page + 10::]

        # última pagina
        pages.append(pdf_string)
        return pages



