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

    print('new_file_path '+new_file_path)
    print(file_dir_str)
    if not os.path.exists(f'workdir/{target_dir}/{new_file_path}'):
        print(file_dir_list)
        
        if file_dir_list:
            
            if not os.path.exists(f'workdir/{target_dir}/{file_dir_str}'):
                os.makedirs(f'workdir/{target_dir}/{file_dir_str}')

            width, height = 1, 1
            background_color = (0, 0, 0)  # Red
            image = Image.new('RGB', (width, height), background_color)
            print(f'!!!!!to workdir/{target_dir}/{new_file_path}')
            image.save(f'workdir/{target_dir}/{new_file_path}')

            print(f"Image saved to {target_dir}/{new_file_path}")
    else:
        print(f'fiel is exists')

def chack_domain(url: str) -> bool:
    split_url = url.split('//')
    print(split_url)

    if split_url[0] == 'http:' or split_url[0] == 'https:':
        domain = split_url[1].split('/')[0]
        if domain != our_domain:
            return True


def replace_links(html_file, new_url):
    with open(html_file, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    a_links = soup.find_all('a')
    img_links = soup.find_all('img')
    
    for img in img_links:
        src = img.get('src')
        split_src = src.split('//')
        file_extention = src.split('.')[-1]
        print(split_src)
        if split_src[0] == 'http:' or split_src[0] == 'https:':
            pass
        elif file_extention == "html" or file_extention == "svg": 
            pass
        else:
            create_img(target_dir=target_dir, file_path=src)

    for link in a_links:
        href = link.get('href')
        
        print('href is '+ href)

        if href and chack_domain(href):
            print(href)
            link['href'] = href.replace(href, new_url)
    
    with open(html_file, 'w') as new_file:
        new_file.write(str(soup))


if __name__ == "__main__":
    our_domain = input("Enter domein in <example.com> format: ")
    target_dir = input("Enter directory name: ")
    if not our_domain or not target_dir:
        print('не можна пропускати domein та directory name')
    else:
        for root, dirs, files in os.walk(root_path):
            for name in files:
                print(os.path.join(root, name))
                if name.split('.')[-1] == 'html':
                    replace_links(html_file=os.path.join(root, name),new_url='#')
