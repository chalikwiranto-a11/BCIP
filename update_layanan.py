import os

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already modified
    if 'id="e-induction-link"' in content:
        return

    # Replacement string
    old_layanan = '<li><a href="#" class="nav-link">Layanan</a></li>'
    new_layanan = """<li class="dropdown">
                <a class="nav-link">Layanan <i class="fa-solid fa-chevron-down"></i></a>
                <div class="dropdown-menu">
                    <a href="#" class="dropdown-item e-induction-btn">
                        <i class="fa-solid fa-chalkboard-user"></i> E-Induction
                    </a>
                </div>
            </li>"""

    if old_layanan in content:
        content = content.replace(old_layanan, new_layanan)
    else:
        print(f"Warning: Layanan link not found in {filepath}")

    # Determine prefix
    depth = filepath.count(os.sep) - 1
    prefix = "../" * depth

    modal_html = f"""
    <!-- E-Induction Modal -->
    <div id="e-induction-modal" class="modal">
        <div class="modal-content">
            <span class="close-modal">&times;</span>
            <img src="{prefix}Gambar/e-induction.webp" alt="E-Induction" class="modal-image">
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfki_vRWtetunMT1GbCxkTQt23V2u_zFNrzNitY-tTTfn6Q5A/viewform" target="_blank" class="modal-postcard">
                <div class="postcard-content">
                    <i class="fa-solid fa-link"></i>
                    <div>
                        <h4>Click Here</h4>
                        <p>to fill the E-Induction Form</p>
                    </div>
                </div>
                <i class="fa-solid fa-arrow-right"></i>
            </a>
        </div>
    </div>
"""

    if "<!-- E-Induction Modal -->" not in content:
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
