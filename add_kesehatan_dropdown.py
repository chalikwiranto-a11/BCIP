import os
import re
import shutil

# Step 1: Create directory
os.makedirs('HSE/sub-hse-kesehatan', exist_ok=True)

# Step 2: Create the 10 HTML files based on a template
def create_coming_soon_file(filename, title):
    with open('HSE/kesehatan-kerja.html', 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'<!-- INNER HERO -->.*?<!-- FOOTER -->', re.DOTALL)
    
    new_body = f"""<!-- INNER HERO -->
    <header class="inner-hero">
        <div class="inner-hero-content">
            <h1>{title}</h1>
            <p>HSE Kesehatan Kerja</p>
        </div>
    </header>

    <!-- PAGE CONTENT -->
    <section class="page-content" style="text-align: center; padding: 100px 20px; min-height: 40vh;">
        <h2>Coming Soon</h2>
    </section>

    <!-- FOOTER -->"""
    
    content = pattern.sub(new_body, content)

    # First, replace `../` with `../../`
    content = content.replace('href="../', 'href="../../')
    content = content.replace('src="../', 'src="../../')

    # THEN, replace exact local links in HSE directory to point to parent HSE folder:
    content = content.replace('href="keselamatan-kerja.html"', 'href="../keselamatan-kerja.html"')
    content = content.replace('href="kesehatan-kerja.html"', 'href="../kesehatan-kerja.html"')
    content = content.replace('href="lingkungan.html"', 'href="../lingkungan.html"')
    content = content.replace('href="keamanan.html"', 'href="../keamanan.html"')
    content = content.replace('href="tanggap-darurat.html"', 'href="../tanggap-darurat.html"')
    
    with open(f'HSE/sub-hse-kesehatan/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)

files_to_create = [
    ('occupational-health.html', 'Occupational Health'),
    ('medical-check-up.html', 'Medical Check Up'),
    ('ergonomic-programme.html', 'Ergonomic Programme'),
    ('mental-health.html', 'Mental Health'),
    ('heat-stress-management.html', 'Heat Stress Management'),
    ('noise-monitoring.html', 'Noise Monitoring'),
    ('industrial-hygiene.html', 'Industrial Hygiene'),
    ('air-quality-monitoring.html', 'Air Quality Monitoring'),
    ('healthy-lifestyle-program.html', 'Healthy Lifestyle Program'),
    ('vaccination-programme.html', 'Vaccination Programme')
]

for filename, title in files_to_create:
    create_coming_soon_file(filename, title)
print(f"Created {len(files_to_create)} HTML files.")

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

    # We want to replace the `Kesehatan Kerja` link with a sub-dropdown block.
    # The current pattern is roughly:
    # <a href=".../kesehatan-kerja.html" class="dropdown-item"><i class="fa-solid fa-notes-medical"></i> Kesehatan Kerja</a>
    
    pattern = re.compile(r'<a href="[^"]*kesehatan-kerja\.html"\s+class="dropdown-item">\s*<i class="fa-solid fa-notes-medical"></i>\s*Kesehatan Kerja\s*</a>', re.DOTALL)
    
    new_html = f"""<div class="sub-dropdown">
                        <a href="{prefix}HSE/kesehatan-kerja.html" class="dropdown-item">
                            <i class="fa-solid fa-notes-medical"></i> Kesehatan Kerja <i class="fa-solid fa-chevron-right sub-dropdown-icon"></i>
                        </a>
                        <div class="sub-dropdown-menu" style="top: -50px;">
                            <a href="{prefix}HSE/sub-hse-kesehatan/occupational-health.html" class="dropdown-item">Occupational Health</a>
                            <a href="{prefix}HSE/sub-hse-kesehatan/medical-check-up.html" class="dropdown-item">Medical Check Up</a>
                            <a href="{prefix}HSE/sub-hse-kesehatan/ergonomic-programme.html" class="dropdown-item">Ergonomic Programme</a>
                            <a href="{prefix}HSE/sub-hse-kesehatan/mental-health.html" class="dropdown-item">Mental Health</a>
                            <a href="{prefix}HSE/sub-hse-kesehatan/heat-stress-management.html" class="dropdown-item">Heat Stress Management</a>
                            <a href="{prefix}HSE/sub-hse-kesehatan/noise-monitoring.html" class="dropdown-item">Noise Monitoring</a>
                            <a href="{prefix}HSE/sub-hse-kesehatan/industrial-hygiene.html" class="dropdown-item">Industrial Hygiene</a>
                            <a href="{prefix}HSE/sub-hse-kesehatan/air-quality-monitoring.html" class="dropdown-item">Air Quality Monitoring</a>
                            <a href="{prefix}HSE/sub-hse-kesehatan/healthy-lifestyle-program.html" class="dropdown-item">Healthy Lifestyle Program</a>
                            <a href="{prefix}HSE/sub-hse-kesehatan/vaccination-programme.html" class="dropdown-item">Vaccination Programme</a>
                        </div>
                    </div>"""

    new_content = pattern.sub(new_html, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        # Check if already updated
        if "sub-hse-kesehatan/occupational-health.html" in content:
            print(f"Already updated {filepath}")
        else:
            print(f"Warning: Kesehatan Kerja link not found in {filepath}")

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

