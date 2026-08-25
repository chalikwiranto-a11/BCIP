import os
import re

# 1. Create directory
os.makedirs('HSE/sub-hse-keamanan', exist_ok=True)

# 2. Create 5 HTML files
def create_coming_soon_file(filename, title):
    with open('HSE/keamanan.html', 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'<!-- INNER HERO -->.*?<!-- FOOTER -->', re.DOTALL)
    new_body = f"""<!-- INNER HERO -->
    <header class="inner-hero">
        <div class="inner-hero-content">
            <h1>{title}</h1>
            <p>HSE Keamanan</p>
        </div>
    </header>

    <!-- PAGE CONTENT -->
    <section class="page-content" style="text-align: center; padding: 100px 20px; min-height: 40vh;">
        <h2>Coming Soon</h2>
    </section>

    <!-- FOOTER -->"""
    content = pattern.sub(new_body, content)

    content = content.replace('href="../', 'href="../../')
    content = content.replace('src="../', 'src="../../')

    content = content.replace('href="keselamatan-kerja.html"', 'href="../keselamatan-kerja.html"')
    content = content.replace('href="kesehatan-kerja.html"', 'href="../kesehatan-kerja.html"')
    content = content.replace('href="lingkungan.html"', 'href="../lingkungan.html"')
    content = content.replace('href="keamanan.html"', 'href="../keamanan.html"')
    content = content.replace('href="tanggap-darurat.html"', 'href="../tanggap-darurat.html"')

    with open(f'HSE/sub-hse-keamanan/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)

keamanan_files = [
    ('secure-and-asset-management.html', 'Secure and Asset Management'),
    ('operation-control.html', 'Operation Control'),
    ('fasilitas-hse.html', 'Fasilitas HSE'),
    ('security-patrol.html', 'Security Patrol'),
    ('inspection-sajam-alcohol-and-drug.html', 'Inspection Sajam, Alcohol and Drug')
]

for f, t in keamanan_files:
    create_coming_soon_file(f, t)
print(f"Created {len(keamanan_files)} HTML files in HSE/sub-hse-keamanan/")

# 3. Update all HTML files
def update_nav(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    depth = filepath.replace("\\", "/").count('/')
    if filepath.startswith('./'):
        depth -= 1
    if depth < 0:
        depth = 0
    prefix = "../" * depth

    pattern = re.compile(r'<a href="[^"]*keamanan\.html"\s+class="dropdown-item">\s*<i class="fa-solid fa-shield-halved"></i>\s*Keamanan\s*</a>', re.DOTALL)

    rep = f"""<div class="sub-dropdown">
                        <a href="{prefix}HSE/keamanan.html" class="dropdown-item">
                            <i class="fa-solid fa-shield-halved"></i> Keamanan <i class="fa-solid fa-chevron-down sub-dropdown-icon"></i>
                        </a>
                        <div class="sub-dropdown-menu">
                            <a href="{prefix}HSE/sub-hse-keamanan/secure-and-asset-management.html" class="dropdown-item">Secure and Asset Management</a>
                            <a href="{prefix}HSE/sub-hse-keamanan/operation-control.html" class="dropdown-item">Operation Control</a>
                            <a href="{prefix}HSE/sub-hse-keamanan/fasilitas-hse.html" class="dropdown-item">Fasilitas HSE</a>
                            <a href="{prefix}HSE/sub-hse-keamanan/security-patrol.html" class="dropdown-item">Security Patrol</a>
                            <a href="{prefix}HSE/sub-hse-keamanan/inspection-sajam-alcohol-and-drug.html" class="dropdown-item">Inspection Sajam, Alcohol and Drug</a>
                        </div>
                    </div>"""

    new_content = pattern.sub(rep, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        if "sub-hse-keamanan" in content:
            pass
        else:
            print(f"Warning: Keamanan link not found in {filepath}")

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            update_nav(os.path.join(root, file))
