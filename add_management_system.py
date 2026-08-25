import os
import re
import shutil

BASE_DIR = '/Users/wirantochalik/Desktop/BCIP'
MGMT_FILE = os.path.join(BASE_DIR, 'HSE', 'management-system.html')
TANGGAP_FILE = os.path.join(BASE_DIR, 'HSE', 'tanggap-darurat.html')

# 1. Create management-system.html by copying tanggap-darurat.html and replacing text
with open(TANGGAP_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<title>Tanggap Darurat - HSE BCIP</title>', '<title>Management System - HSE BCIP</title>')
content = content.replace('content="Standar Tanggap Darurat', 'content="Management System')
content = content.replace('<h1>Tanggap <span>Darurat</span></h1>', '<h1>Management <span>System</span></h1>')
content = content.replace('<p>Kesiapsiagaan penuh dalam menghadapi insiden', '<p>Sistem Manajemen HSE yang terintegrasi')

with open(MGMT_FILE, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Created {MGMT_FILE}')

# 2. Add Management System to the navbar in all HTML files
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
    
    # We want to insert the Management System link right after the Tanggap Darurat sub-dropdown
    # We can match the end of Tanggap Darurat block and insert it
    
    # Pattern to match the Tanggap Darurat sub-dropdown block
    # It looks like:
    #                     <div class="sub-dropdown">
    #                         <a href="...tanggap-darurat.html"...>...</a>
    #                         <div class="sub-dropdown-menu">...</div>
    #                     </div>
    #                 </div>
    #             </li>
    # We can just match the closing div of Tanggap Darurat by using regex or just string replacement
    
    # Let's find the Tanggap Darurat block.
    # The end of the sub-dropdown block for Tanggap Darurat is followed by:
    #                 </div>
    #             </li>
    #             <li class="dropdown">
    #                 <a class="nav-link">Layanan
    
    search_str = '''                        </div>
                    </div>
                </div>
            </li>
            <li class="dropdown">
                <a class="nav-link">Layanan'''
    
    # If using regex, we can match:
    # r'(<div class="sub-dropdown">\s*<a href="[^"]*tanggap-darurat\.html".*?</div>\s*</div>)'
    
    # Let's use a simpler string replace on the exact tanggap-darurat block closing.
    # Actually, tanggap-darurat is the last item in the HSE dropdown menu.
    # The HSE dropdown menu is closed by:
    #                 </div>
    #             </li>
    # And then Layanan starts.
    
    # Let's search for tanggap-darurat.html in the file.
    
    pattern = r'(<div class="sub-dropdown">\s*<a href="[^"]*tanggap-darurat\.html"[^>]*>.*?</div>\s*</div>)'
    
    new_item = f'''<a href="{prefix}HSE/management-system.html" class="dropdown-item">
                            <i class="fa-solid fa-sitemap"></i> Management System
                        </a>'''
    
    # We want to append new_item after the match (pattern).
    # Wait, does management-system have sub-items? The user didn't specify. I will add it as a normal dropdown item for now.
    
    # Let's refine the replacement:
    def repl(m):
        return m.group(1) + '\n                    ' + new_item
    
    new_content = re.sub(pattern, repl, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
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
