import requests
def write_html(url):
    # Escrevendo o documento HTML do site:
    r = requests.get(url)
    r.raise_for_status()
    with open("dom.html", "w", encoding="utf-8") as dom_html_file:
        dom_html_file.write(r.text)
