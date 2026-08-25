import os
import re

BASE_DIR = '/Users/wirantochalik/Desktop/BCIP'
SUB_DIR = os.path.join(BASE_DIR, 'HSE', 'sub-hse-management-system')
TEMPLATE_FILE = os.path.join(BASE_DIR, 'HSE', 'management-system.html')

os.makedirs(SUB_DIR, exist_ok=True)

ITEMS = [
    ("Polecy dan Kebijakan", "polecy-dan-kebijakan.html"),
    ("Structure Organisasi", "structure-organisasi.html"),
    ("Legal Compliance", "legal-compliance.html"),
    ("HSE Mangement System", "hse-mangement-system.html"),
    ("HSE Digitalization", "hse-digitalization.html"),
    ("HSE Improvement", "hse-improvement.html"),
    ("KPI QHSSE Performend", "kpi-qhsse-performend.html"),
    ("Control Improvement", "control-improvement.html")
]

# Read the template file
with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Replace the Management System link in the template with the new dropdown so that when we copy it, it has the right base format
# Actually, it's easier to just generate them first, then run the update on ALL HTML files.

def get_template(title):
    content = template_content
    # Replace title
    content = re.sub(r'<title>Management System - HSE BCIP</title>', f'<title>{title} - HSE BCIP</title>', content)
    content = re.sub(r'content="Management System[^"]*"', f'content="{title} di Batuta Chemical Industrial Park (BCIP)."', content)
    content = re.sub(r'<h1>Management <span>System</span></h1>', f'<h1>{title}</h1>', content)
    return content

for title, filename in ITEMS:
    file_path = os.path.join(SUB_DIR, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(get_template(title))
    print(f'Created {file_path}')

# Now update all HTML files
def get_management_system_subdropdown(prefix):
    return f'''<div class="sub-dropdown">
                        <a href="{prefix}HSE/management-system.html" class="dropdown-item">
                            <i class="fa-solid fa-sitemap"></i> Management System <i class="fa-solid fa-chevron-down sub-dropdown-icon"></i>
                        </a>
                        <div class="sub-dropdown-menu">
                            <a href="{prefix}HSE/sub-hse-management-system/polecy-dan-kebijakan.html" class="dropdown-item">Polecy dan Kebijakan</a>
                            <a href="{prefix}HSE/sub-hse-management-system/structure-organisasi.html" class="dropdown-item">Structure Organisasi</a>
                            <a href="{prefix}HSE/sub-hse-management-system/legal-compliance.html" class="dropdown-item">Legal Compliance</a>
                            <a href="{prefix}HSE/sub-hse-management-system/hse-mangement-system.html" class="dropdown-item">HSE Mangement System</a>
                            <a href="{prefix}HSE/sub-hse-management-system/hse-digitalization.html" class="dropdown-item">HSE Digitalization</a>
                            <a href="{prefix}HSE/sub-hse-management-system/hse-improvement.html" class="dropdown-item">HSE Improvement</a>
                            <a href="{prefix}HSE/sub-hse-management-system/kpi-qhsse-performend.html" class="dropdown-item">KPI QHSSE Performend</a>
                            <a href="{prefix}HSE/sub-hse-management-system/control-improvement.html" class="dropdown-item">Control Improvement</a>
                        </div>
                    </div>'''

def get_prefix_for_file(filepath):
    rel = os.path.relpath(filepath, BASE_DIR)
    parts = rel.split(os.sep)
    if len(parts) == 1:
        return ''
    elif len(parts) == 2:
        return '../'
    elif len(parts) == 3:
        return '../../'
    return ''

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    prefix = get_prefix_for_file(filepath)
    new_dropdown = get_management_system_subdropdown(prefix)
    
    # We want to replace the single Management System link:
    # <a href="...HSE/management-system.html" class="dropdown-item">
    #     <i class="fa-solid fa-sitemap"></i> Management System
    # </a>
    
    # Regex to match this exact block
    # Note: the previous script used:
    # <a href="{prefix}HSE/management-system.html" class="dropdown-item">
    #                         <i class="fa-solid fa-sitemap"></i> Management System
    #                     </a>
    
    # We will use regex that matches <a href=".../management-system.html" class="dropdown-item">\s*<i class="fa-solid fa-sitemap"></i> Management System\s*</a>
    # Or more robust:
    
    pattern = r'<a href="[^"]*management-system\.html"[^>]*>\s*<i class="fa-solid fa-sitemap"></i>\s*Management System\s*</a>'
    
    if re.search(pattern, content):
        content = re.sub(pattern, new_dropdown, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {filepath}')
        return True
    return False

count = 0
for root, dirs, files in os.walk(BASE_DIR):
    if '.git' in root:
        continue
    for filename in files:
        if filename.endswith('.html'):
            filepath = os.path.join(root, filename)
            if process_file(filepath):
                count += 1

print(f'\\nTotal files updated: {count}')
