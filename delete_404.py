from bs4 import BeautifulSoup

def extract_tag(bs4_tag, atr: str, broken_links: set, domain: str):
    
    for link in bs4_tag:

        href = link.get(atr)
        if href:
            splited_link = [i for i in href.split('/') if i and i != '..']
            new_link = "/"+"/".join(splited_link)
            if f'https://{domain}{new_link}' in broken_links:
                link.extract()
        
        if f'https://{domain}/{href}' in broken_links:
            link.extract()
        elif f'http://{domain}/{href}' in broken_links:
            link.extract()
        elif href in broken_links:
            link.extract()
        else:
            pass

def replace_linc(bs4_tag, atr: str, broken_links: set, domain: str):
    
    for link in bs4_tag:

        href = link.get(atr)
        if href:
            splited_link = [i for i in href.split('/') if i and i != '..']
            new_link = "/"+"/".join(splited_link)
            if f'https://{domain}{new_link}' in broken_links:
                link[atr] = href.replace(href, '#')

        if f'https://{domain}/{href}' in broken_links or f'https://{domain}{href}' in broken_links:
            link[atr] = href.replace(href, '#')
        elif f'http://{domain}/{href}' in broken_links or f'http://{domain}{href}' in broken_links:
            link[atr] = href.replace(href, '#')
        elif href in broken_links:
            link[atr] = href.replace(href, '#')
        else:
            pass

def extract_404(html_file, broken_links: set, domain: str):

    with open(html_file, 'r',  encoding="utf-8", errors='ignore') as file:
        html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')

    a_tags = soup.find_all('a')
    img_tags = soup.find_all('img')
    link_tags = soup.find_all('link')
    script_tags = soup.find_all('script')
    
    replace_linc(a_tags, 'href', broken_links, domain)
    extract_tag(img_tags, 'src', broken_links, domain)
    extract_tag(link_tags, 'href', broken_links, domain)
    extract_tag(script_tags, 'src', broken_links, domain)
    
    with open(html_file, 'w',  encoding="utf-8", errors='ignore') as new_file:
        new_file.write(str(soup))
