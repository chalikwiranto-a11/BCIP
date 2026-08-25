import os
import re

# 1. Create directories
os.makedirs('HSE/sub-hse-keselamatan', exist_ok=True)
os.makedirs('HSE/sub-hse-kesehatan', exist_ok=True)

# 2. Template function
def create_file(folder, filename, title):
    # Always read from the pristine HSE/keselamatan-kerja.html
    with open('HSE/keselamatan-kerja.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the body
    pattern = re.compile(r'<!-- INNER HERO -->.*?<!-- FOOTER -->', re.DOTALL)
    
    new_body = f"""<!-- INNER HERO -->
    <header class="inner-hero">
        <div class="inner-hero-content">
            <h1>{title}</h1>
            <p>HSE { 'Kesehatan' if 'kesehatan' in folder else 'Keselamatan' } Kerja</p>
        </div>
    </header>

    <!-- PAGE CONTENT -->
    <section class="page-content" style="text-align: center; padding: 100px 20px; min-height: 40vh;">
        <h2>Coming Soon</h2>
    </section>

    <!-- FOOTER -->"""
    
    content = pattern.sub(new_body, content)

    # Adjust base paths
    content = content.replace('href="../', 'href="../../')
    content = content.replace('src="../', 'src="../../')

    # Adjust local HSE links
    content = content.replace('href="keselamatan-kerja.html"', 'href="../keselamatan-kerja.html"')
    content = content.replace('href="kesehatan-kerja.html"', 'href="../kesehatan-kerja.html"')
    content = content.replace('href="lingkungan.html"', 'href="../lingkungan.html"')
    content = content.replace('href="keamanan.html"', 'href="../keamanan.html"')
    content = content.replace('href="tanggap-darurat.html"', 'href="../tanggap-darurat.html"')
    
    with open(f'{folder}/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)

# Generate Keselamatan files
keselamatan_files = [
    ('risk-management-system.html', 'Risk Management System'),
    ('inspection-and-monitoring.html', 'Inspection and Monitoring'),
    ('safety-culture.html', 'Safety Culture'),
    ('training-programme.html', 'Training Programme')
]
for f, t in keselamatan_files:
    create_file('HSE/sub-hse-keselamatan', f, t)

# Generate Kesehatan files
kesehatan_files = [
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
for f, t in kesehatan_files:
    create_file('HSE/sub-hse-kesehatan', f, t)

# 3. Update all HTML files with BOTH nested dropdowns
# Find exactly the two <a> tags for Keselamatan and Kesehatan and replace them.

def update_nav(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    depth = filepath.replace("\\", "/").count('/')
    if filepath.startswith('./'):
        depth -= 1
    if depth < 0:
        depth = 0
    prefix = "../" * depth

    # Use strict regex that only matches the HTML of the <a> tag
    pat_kes = re.compile(r'<a href="[^"]*keselamatan-kerja\.html"\s+class="dropdown-item">\s*<i class="fa-solid fa-hard-hat"></i>\s*Keselamatan Kerja\s*</a>')
    
    rep_kes = f"""<div class="sub-dropdown">
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

    # For Kesehatan, it has an icon: fa-notes-medical
    pat_keh = re.compile(r'<a href="[^"]*kesehatan-kerja\.html"\s+class="dropdown-item">\s*<i\s+class="fa-solid fa-notes-medical"></i>\s*Kesehatan Kerja\s*</a>')
    
    rep_keh = f"""<div class="sub-dropdown">
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

    new_content = pat_kes.sub(rep_kes, content)
    new_content = pat_keh.sub(rep_keh, new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes / couldn't match in {filepath}")

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            update_nav(os.path.join(root, file))
