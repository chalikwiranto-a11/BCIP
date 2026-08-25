import os

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'id="e-tbm-modal"' in content:
        return

    # 1. Update dropdown menu
    old_menu = """                    <a href="#" class="dropdown-item e-attendent-btn">
                        <i class="fa-solid fa-clipboard-user"></i> E-Attendent List
                    </a>"""
    
    new_menu = """                    <a href="#" class="dropdown-item e-attendent-btn">
                        <i class="fa-solid fa-clipboard-user"></i> E-Attendent List
                    </a>
                    <a href="#" class="dropdown-item e-tbm-btn">
                        <i class="fa-solid fa-toolbox"></i> ToolBox Meeting
                    </a>"""
    
    if old_menu in content:
        content = content.replace(old_menu, new_menu)
    elif "e-attendent-btn" in content:
        # Sometimes there might be slightly different indentation
        # Let's find e-attendent-btn and insert after its closing </a>
        pass
    else:
        print(f"Warning: E-Attendent link not found in {filepath}")

    # 2. Add Modal
    depth = filepath.count(os.sep) - 1
    # Adjust depth relative to root directory, which is the script's directory '.'
    # but wait, os.walk returns paths like ./index.html or ./HSE/kesehatan.html
    # so depth based on count of os.sep isn't correct if we run it from /Users/wirantochalik/Desktop/BCIP
    # filepath will be e.g. ./index.html -> depth 0
    # filepath ./HSE/kesehatan.html -> depth 1
    depth = filepath.replace("\\", "/").count('/') - 1
    if depth < 0:
        depth = 0
    prefix = "../" * depth

    modal_html = f"""
    <!-- ToolBox Meeting Modal -->
    <div id="e-tbm-modal" class="modal">
        <div class="modal-content">
            <span class="close-modal">&times;</span>
            <img src="{prefix}Gambar/e-tbm.webp" alt="ToolBox Meeting" class="modal-image">
            <a href="https://drive.google.com/drive/folders/1rQtDU7batIDYbB0fEWhWttiwbZDahkZc?usp=sharing"
                target="_blank" class="modal-postcard">
                <div class="postcard-content">
                    <i class="fa-solid fa-link"></i>
                    <div>
                        <h4>Click Here</h4>
                        <p>to view the ToolBox Meeting</p>
                    </div>
                </div>
                <i class="fa-solid fa-arrow-right"></i>
            </a>
        </div>
    </div>
"""

    if "<!-- ToolBox Meeting Modal -->" not in content:
        content = content.replace("</body>", modal_html + "</body>")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def main():
    for root, dirs, files in os.walk('.'):
        if '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                process_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
