import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the e-tbm-modal block
    pattern = re.compile(r'<!-- ToolBox Meeting Modal -->.*?<div id="e-tbm-modal".*?</div>\s*</div>', re.DOTALL)
    match = pattern.search(content)
    
    if not match:
        print(f"Warning: ToolBox Meeting modal not found in {filepath}")
        return

    # To keep the correct prefix for the image
    depth = filepath.replace("\\", "/").count('/') - 1
    if depth < 0:
        depth = 0
    prefix = "../" * depth

    new_modal_html = f"""<!-- ToolBox Meeting Modal -->
    <div id="e-tbm-modal" class="modal">
        <div class="modal-content">
            <span class="close-modal">&times;</span>
            <img src="{prefix}Gambar/e-tbm.webp" alt="ToolBox Meeting" class="modal-image">
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfDW2SG-r_9_YXgl9iIvdW33bao7KyAG6B9QHfcN44POObIXQ/viewform?usp=publish-editor"
                target="_blank" class="modal-postcard" style="margin-bottom: 15px;">
                <div class="postcard-content">
                    <i class="fa-solid fa-link"></i>
                    <div>
                        <h4>Click Here</h4>
                        <p>to fill the Attend form</p>
                    </div>
                </div>
                <i class="fa-solid fa-arrow-right"></i>
            </a>
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
    </div>"""

    new_content = content[:match.start()] + new_modal_html + content[match.end():]

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes made to {filepath}")

def main():
    for root, dirs, files in os.walk('.'):
        if '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                process_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
