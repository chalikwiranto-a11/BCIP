import os

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already modified
    if 'id="e-attendent-modal"' in content:
        return

    # Replacement string
    old_item = """                    <a href="#" class="dropdown-item e-induction-btn">
                        <i class="fa-solid fa-chalkboard-user"></i> E-Induction
                    </a>"""
    
    new_item = """                    <a href="#" class="dropdown-item e-induction-btn">
                        <i class="fa-solid fa-chalkboard-user"></i> E-Induction
                    </a>
                    <a href="#" class="dropdown-item e-attendent-btn">
                        <i class="fa-solid fa-clipboard-user"></i> E-Attendent List
                    </a>"""

    if old_item in content:
        content = content.replace(old_item, new_item)
    else:
        print(f"Warning: E-Induction button not found in {filepath} (Might be formatting mismatch)")

    # Determine prefix
    depth = filepath.count(os.sep) - 1
    prefix = "../" * depth if depth > 0 else ""

    modal_html = f"""
    <!-- E-Attendent Modal -->
    <div id="e-attendent-modal" class="modal">
        <div class="modal-content">
            <span class="close-modal">&times;</span>
            <img src="{prefix}Gambar/e-attendent list.webp" alt="E-Attendent List" class="modal-image">
            <a href="https://docs.google.com/forms/d/e/1FAIpQLScPDWgRgCfv_tfDiuq_bli0Xc2mq34BiY9idQ84fiTNYYAnmA/viewform?usp=dialog" target="_blank" class="modal-postcard">
                <div class="postcard-content">
                    <i class="fa-solid fa-link"></i>
                    <div>
                        <h4>Click Here</h4>
                        <p>to fill the E-Attendent Form</p>
                    </div>
                </div>
                <i class="fa-solid fa-arrow-right"></i>
            </a>
        </div>
    </div>
"""

    if "<!-- E-Attendent Modal -->" not in content:
        # Append before </body>
        content = content.replace("</body>", modal_html + "\n</body>")

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
