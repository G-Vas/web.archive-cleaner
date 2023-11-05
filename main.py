import os
from PIL import Image, ImageDraw
from bs4 import BeautifulSoup

our_domain = ""
target_dir = ""
root_path = 'workdir'

def create_img(target_dir: str, file_path: str):
    
    file_dir_list = [i for i in file_path.split('/') if i and i != '..']
    file_dir_str = "/".join(file_dir_list[:-1])
    new_file_path = "/".join(file_dir_list)

    if not os.path.exists(f'workdir/{target_dir}/{new_file_path}'):
        
        if file_dir_list:
            
            if not os.path.exists(f'workdir/{target_dir}/{file_dir_str}'):
                os.makedirs(f'workdir/{target_dir}/{file_dir_str}')

            width, height = 1, 1
            background_color = (228,213,181)  # White
            image = Image.new('RGB', (width, height), background_color)
            image.save(f'workdir/{target_dir}/{new_file_path}')

    else:
         print(f'fiel is exists')

def chack_extermal_domen(url: str) -> bool:
    print(url)
    split_url = url.split('//')

    if split_url[0] == 'http:' or split_url[0] == 'https:':
        domain = split_url[1].split('/')[0]
        if domain != our_domain and domain != f'www.{our_domain}':
            return True
    return False

def replace_links(html_file, new_url):
    with open(html_file, 'r',  encoding="utf-8", errors='ignore') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    a_links = soup.find_all('a')
    img_links = soup.find_all('img')
    links = soup.find_all('link')
    
    for link in links:
        href = link.get('href')
        split_src = href.split('//')
        if split_src[0] == 'http:':
            new_href = f'https://{split_src[1]}'
            link['href'] = href.replace(href, new_href)  
    
    for img in img_links:
        src = img.get('src')
        split_src = src.split('//')
        file_extention = src.split('.')[-1]

        if split_src[0] == 'http:' or split_src[0] == 'https:':
            
            if not chack_extermal_domen(url=src):
                print('not ext'+ src)
                path = str(split_src[1]).split('/')[1:]
                file_path = '/'.join(path)
                print(file_path)
                create_img(target_dir=target_dir, file_path=file_path)

                new_src = f'https://{our_domain}/{file_path}'
                img['src'] = src.replace(src, new_src)
                
        elif file_extention == "html" or file_extention == "svg": 
            pass
        else:
            create_img(target_dir=target_dir, file_path=src)

    for link in a_links:
        href = link.get('href')
        split_href = href.split('//')

        if href and chack_extermal_domen(href):
            link['href'] = href.replace(href, new_url)

        if href and split_href[0] == 'http:':
            new_href = f'https://{split_href[1]}'
            link['href'] = href.replace(href, new_href)
    
    with open(html_file, 'w',  encoding="utf-8", errors='ignore') as new_file:
        new_file.write(str(soup))

if __name__ == "__main__":
    our_domain = input("Enter domein in <example.com> format: ")
    target_dir = input("Enter directory: ")
    if not our_domain or not target_dir:
        print('domein and directory cannot be skipped')
    else:
        for root, dirs, files in os.walk(root_path):
            for name in files:
                if name.split('.')[-1] == 'html':
                    replace_links(os.path.join(root, name), '#')
