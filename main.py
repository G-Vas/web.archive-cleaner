import os
from delete_404 import extract_404
from delete_external import replace_links

root_path = 'workdir'
broken_links: set

if __name__ == "__main__":
    extraction_404 = False
    
    our_domain = input("Enter domein in <example.com> format: ")
    target_dir = input("Enter directory: ")
    
    with open('workdir/404.txt') as file:
        broken_links = set(file.read().splitlines())
    
    if not our_domain or not target_dir:
        print('domein and directory cannot be skipped')
    else:
        for root, dirs, files in os.walk(root_path):
            for name in files:
                if name.split('.')[-1] == 'html':
                    if extraction_404:
                        extract_404(html_file=os.path.join(root, name),
                                broken_links=broken_links,
                                domain=our_domain)
                    else:
                        replace_links(html_file=os.path.join(root, name),
                                    new_url='#',
                                    our_domain=our_domain,
                                    target_dir=target_dir)
