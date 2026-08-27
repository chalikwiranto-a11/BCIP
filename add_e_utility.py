import os
import re

BASE_DIR = '/Users/wirantochalik/Desktop/BCIP'

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
    modified = False

    # 1. Add E-Utility link to the Layanan dropdown
    # The Layanan dropdown ends with:
    # <a href="#" class="dropdown-item e-tbm-btn">
    #     <i class="fa-solid fa-toolbox"></i> ToolBox Meeting
    # </a>
    # </div>
    
    dropdown_pattern = r'(<a href="#" class="dropdown-item e-tbm-btn">\s*<i class="fa-solid fa-toolbox"></i> ToolBox Meeting\s*</a>\s*)(</div>)'
    
    new_dropdown_link = f'''<a href="#" class="dropdown-item e-utility-btn">
                        <i class="fa-solid fa-bolt"></i> E-Utility
                    </a>
                '''
                
    if re.search(dropdown_pattern, content):
        content = re.sub(dropdown_pattern, r'\1' + new_dropdown_link + r'\2', content)
        modified = True
    else:
        print(f"Warning: Could not find ToolBox Meeting link in {filepath}")

    # 2. Add E-Utility modal before </body>
    modal_html = f'''
    <!-- E-Utility Modal -->
    <div id="e-utility-modal" class="modal">
        <div class="modal-content">
            <span class="close-modal">&times;</span>
            <img src="{prefix}Gambar/e-utility.webp" alt="E-Utility" class="modal-image">
            <a href="https://drive.google.com/drive/folders/1CWyNXRcDeDUWNSYkJdqHVo3sKt_JcJnP?usp=drive_link"
                target="_blank" class="modal-postcard">
                <div class="postcard-content">
                    <i class="fa-solid fa-link"></i>
                    <div>
                        <h4>Click Here</h4>
                        <p>to view E-Utility</p>
                    </div>
                </div>
                <i class="fa-solid fa-arrow-right"></i>
            </a>
        </div>
    </div>
'''
    
    body_pattern = r'</body>'
    if re.search(body_pattern, content) and 'id="e-utility-modal"' not in content:
        content = re.sub(body_pattern, modal_html + '\n</body>', content)
        modified = True

    if modified:
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
