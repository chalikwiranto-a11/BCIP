import os
import re

# 1. Create directory
os.makedirs('HSE/sub-hse-lingkungan', exist_ok=True)

# 2. Create 10 HTML files
def create_coming_soon_file(filename, title):
    with open('HSE/lingkungan.html', 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'<!-- INNER HERO -->.*?<!-- FOOTER -->', re.DOTALL)
    new_body = f"""<!-- INNER HERO -->
    <header class="inner-hero">
        <div class="inner-hero-content">
            <h1>{title}</h1>
            <p>HSE Lingkungan</p>
        </div>
    </header>

    <!-- PAGE CONTENT -->
    <section class="page-content" style="text-align: center; padding: 100px 20px; min-height: 40vh;">
        <h2>Coming Soon</h2>
    </section>

    <!-- FOOTER -->"""
    content = pattern.sub(new_body, content)

    # Adjust paths: lingkungan.html uses "../" for root, sub-hse-lingkungan needs "../../"
    content = content.replace('href="../', 'href="../../')
    content = content.replace('src="../', 'src="../../')

    # Fix local HSE links (relative without ../)
    content = content.replace('href="keselamatan-kerja.html"', 'href="../keselamatan-kerja.html"')
    content = content.replace('href="kesehatan-kerja.html"', 'href="../kesehatan-kerja.html"')
    content = content.replace('href="lingkungan.html"', 'href="../lingkungan.html"')
    content = content.replace('href="keamanan.html"', 'href="../keamanan.html"')
    content = content.replace('href="tanggap-darurat.html"', 'href="../tanggap-darurat.html"')

    with open(f'HSE/sub-hse-lingkungan/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)

lingkungan_files = [
    ('environment-management.html', 'Environment Management'),
    ('waste-management.html', 'Waste Management'),
    ('waste-water-management.html', 'Waste Water Management'),
    ('air-emissions-control.html', 'Air Emissions Control'),
    ('energy-management.html', 'Energy Management'),
    ('carbon-reduction.html', 'Carbon Reduction'),
    ('water-conservation.html', 'Water Conservation'),
    ('recycle-programme.html', 'Recycle Programme'),
    ('biodiversity.html', 'Biodiversity'),
    ('green-and-revegetation.html', 'Green and Revegetation')
]

for f, t in lingkungan_files:
    create_coming_soon_file(f, t)
print(f"Created {len(lingkungan_files)} HTML files in HSE/sub-hse-lingkungan/")

# 3. Update all HTML files: replace the Lingkungan <a> tag with a sub-dropdown
def update_nav(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    depth = filepath.replace("\\", "/").count('/')
    if filepath.startswith('./'):
        depth -= 1
    if depth < 0:
        depth = 0
    prefix = "../" * depth

    # Match the Lingkungan dropdown-item link (icon: fa-leaf)
    pattern = re.compile(r'<a href="[^"]*lingkungan\.html"\s+class="dropdown-item">\s*<i class="fa-solid fa-leaf"></i>\s*Lingkungan\s*</a>', re.DOTALL)

    rep = f"""<div class="sub-dropdown">
                        <a href="{prefix}HSE/lingkungan.html" class="dropdown-item">
                            <i class="fa-solid fa-leaf"></i> Lingkungan <i class="fa-solid fa-chevron-down sub-dropdown-icon"></i>
                        </a>
                        <div class="sub-dropdown-menu">
                            <a href="{prefix}HSE/sub-hse-lingkungan/environment-management.html" class="dropdown-item">Environment Management</a>
                            <a href="{prefix}HSE/sub-hse-lingkungan/waste-management.html" class="dropdown-item">Waste Management</a>
                            <a href="{prefix}HSE/sub-hse-lingkungan/waste-water-management.html" class="dropdown-item">Waste Water Management</a>
                            <a href="{prefix}HSE/sub-hse-lingkungan/air-emissions-control.html" class="dropdown-item">Air Emissions Control</a>
                            <a href="{prefix}HSE/sub-hse-lingkungan/energy-management.html" class="dropdown-item">Energy Management</a>
                            <a href="{prefix}HSE/sub-hse-lingkungan/carbon-reduction.html" class="dropdown-item">Carbon Reduction</a>
                            <a href="{prefix}HSE/sub-hse-lingkungan/water-conservation.html" class="dropdown-item">Water Conservation</a>
                            <a href="{prefix}HSE/sub-hse-lingkungan/recycle-programme.html" class="dropdown-item">Recycle Programme</a>
                            <a href="{prefix}HSE/sub-hse-lingkungan/biodiversity.html" class="dropdown-item">Biodiversity</a>
                            <a href="{prefix}HSE/sub-hse-lingkungan/green-and-revegetation.html" class="dropdown-item">Green and Revegetation</a>
                        </div>
                    </div>"""

    new_content = pattern.sub(rep, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        if "sub-hse-lingkungan" in content:
            pass
        else:
            print(f"Warning: Lingkungan link not found in {filepath}")

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            update_nav(os.path.join(root, file))
