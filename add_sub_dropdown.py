import os
import re
import shutil

# Step 1: Create directory
os.makedirs('HSE/sub-hse-keselamatan', exist_ok=True)

# Step 2: Create the 4 HTML files based on a template
def create_coming_soon_file(filename, title):
    with open('HSE/keselamatan-kerja.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Change the inner hero and page content
    pattern = re.compile(r'<!-- INNER HERO -->.*?<!-- FOOTER -->', re.DOTALL)
    
    new_body = f"""<!-- INNER HERO -->
    <header class="inner-hero">
        <div class="inner-hero-content">
            <h1>{title}</h1>
            <p>HSE Keselamatan Kerja</p>
        </div>
    </header>

    <!-- PAGE CONTENT -->
    <section class="page-content" style="text-align: center; padding: 100px 20px; min-height: 40vh;">
        <h2>Coming Soon</h2>
    </section>

    <!-- FOOTER -->"""
    
    content = pattern.sub(new_body, content)

    # Adjust paths because it's one level deeper
    # "keselamatan-kerja.html" uses "../" for root.
    # The new file is in "sub-hse-keselamatan/", so it needs "../../".
    # We will replace all "../" with "../../" EXCEPT inside the new_body if any (none exist).
    # Actually, we can just do:
    content = content.replace('href="../', 'href="../../')
    content = content.replace('src="../', 'src="../../')
    content = content.replace('href="', 'href="../../HSE/') # wait, no, links like "HSE/..." don't exist in root form inside HSE folder.
    
    # Let's be careful. In `HSE/keselamatan-kerja.html`, links to index are `../index.html`.
    # Links to other HSE files are `kesehatan-kerja.html`.
    # If we move to `HSE/sub-hse-keselamatan/`, links to index become `../../index.html`.
    # Links to HSE files become `../kesehatan-kerja.html`.
    # Let's just adjust the known ones.
    
    # "kesehatan-kerja.html" -> "../kesehatan-kerja.html"
    content = re.sub(r'href="([^/.]+)\.html"', r'href="../\1.html"', content)
    # "../" -> "../../"
    # But doing the above might double replace. Let's do a cleaner approach.
    
    # Just fix the prefix for standard assets and links.
    # In `HSE/keselamatan-kerja.html`, it has:
    # href="../styles.css"
    # href="../index.html"
    # href="../tentang/..."
    # href="../berita.html"
    # href="kesehatan-kerja.html"
    
    # Replace `../` with `../../`
    content = content.replace('../', '../../')
    
    # Replace `href="kesehatan-kerja.html"` with `href="../kesehatan-kerja.html"`
    content = content.replace('href="keselamatan-kerja.html"', 'href="../keselamatan-kerja.html"')
    content = content.replace('href="kesehatan-kerja.html"', 'href="../kesehatan-kerja.html"')
    content = content.replace('href="lingkungan.html"', 'href="../lingkungan.html"')
    content = content.replace('href="keamanan.html"', 'href="../keamanan.html"')
    content = content.replace('href="tanggap-darurat.html"', 'href="../tanggap-darurat.html"')

    with open(f'HSE/sub-hse-keselamatan/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)

create_coming_soon_file('risk-management-system.html', 'Risk Management System')
create_coming_soon_file('inspection-and-monitoring.html', 'Inspection and Monitoring')
create_coming_soon_file('safety-culture.html', 'Safety Culture')
create_coming_soon_file('training-programme.html', 'Training Programme')
print("Created 4 HTML files.")

# Step 3: Update all HTML files with the new dropdown
def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    depth = filepath.replace("\\", "/").count('/')
    if filepath.startswith('./'):
        depth -= 1
    if depth < 0:
        depth = 0
    prefix = "../" * depth

    # The original Keselamatan Kerja link varies slightly depending on if we are in index.html (uses HSE/keselamatan-kerja.html) 
    # or inside HSE/ (uses keselamatan-kerja.html) or tentang/ (uses ../HSE/keselamatan-kerja.html).
    # Wait, the previous script `update_layanan.py` used exact match. Let's use regex to find the Keselamatan Kerja a tag.
    
    pattern = re.compile(r'<a href="[^"]*keselamatan-kerja\.html"\s+class="dropdown-item">\s*<i class="fa-solid fa-hard-hat"></i>\s*Keselamatan Kerja\s*</a>', re.DOTALL)
    
    new_html = f"""<div class="sub-dropdown">
                        <a href="{prefix}HSE/keselamatan-kerja.html" class="dropdown-item">
                            <i class="fa-solid fa-hard-hat"></i> Keselamatan Kerja <i class="fa-solid fa-chevron-right sub-dropdown-icon"></i>
                        </a>
                        <div class="sub-dropdown-menu">
                            <a href="{prefix}HSE/sub-hse-keselamatan/risk-management-system.html" class="dropdown-item">Risk Management System</a>
                            <a href="{prefix}HSE/sub-hse-keselamatan/inspection-and-monitoring.html" class="dropdown-item">Inspection and Monitoring</a>
                            <a href="{prefix}HSE/sub-hse-keselamatan/safety-culture.html" class="dropdown-item">Safety Culture</a>
                            <a href="{prefix}HSE/sub-hse-keselamatan/training-programme.html" class="dropdown-item">Training Programme</a>
                        </div>
                    </div>"""

    new_content = pattern.sub(new_html, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        # Check if already updated
        if "sub-dropdown-menu" in content:
            print(f"Already updated {filepath}")
        else:
            print(f"Warning: Keselamatan Kerja link not found in {filepath}")

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

