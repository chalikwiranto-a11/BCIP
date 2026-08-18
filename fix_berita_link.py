import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine depth for relative path
    depth = filepath.count(os.sep) - 1
    prefix = "../" * depth
    berita_href = f"{prefix}berita.html"
    new_berita_link = f'<li><a href="{berita_href}" class="nav-link">Berita</a></li>'

    # The link might be href="#" or href="berita.html"
    # We will use regex to find the Berita link in the nav-links ul.
    # Note: It could also find the footer link, so we just replace the exact navbar link we know.
    
    old_link_1 = '<li><a href="#" class="nav-link">Berita</a></li>'
    old_link_2 = '<li><a href="berita.html" class="nav-link">Berita</a></li>'

    changed = False
    if old_link_1 in content:
        content = content.replace(old_link_1, new_berita_link)
        changed = True
    elif old_link_2 in content and depth > 0:
        content = content.replace(old_link_2, new_berita_link)
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated Berita link in {filepath} to {berita_href}")

def main():
    for root, dirs, files in os.walk('.'):
        if '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                process_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
