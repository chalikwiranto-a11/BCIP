import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    depth = filepath.replace("\\", "/").count('/')
    if filepath.startswith('./'):
        depth -= 1
    if depth < 0:
        depth = 0
    prefix = "../" * depth

    # Use a more flexible pattern
    pattern = re.compile(r'<a href="[^"]*kesehatan-kerja\.html"\s+class="dropdown-item">.*?Kesehatan Kerja\s*</a>', re.DOTALL)
    
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
            pass
        else:
            print(f"Warning: Kesehatan Kerja link not found in {filepath}")

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))
