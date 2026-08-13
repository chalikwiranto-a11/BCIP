import os
import glob

old_footer_bottom = """        <div class="footer-bottom">
            <p>Copyright &copy;2026 Batuta Chemical Industrial Park</p>
        </div>"""

new_footer_bottom = """        <div class="footer-bottom">
            <p>Copyright &copy;2026 Batuta Chemical Industrial Park</p>
            <p style="margin-top: 5px; color: #777;">Developed by <a href="https://wirantochalik.vercel.app/" target="_blank" style="color: #0066b2; text-decoration: none; font-weight: 500;">Wiranto Chalik</a></p>
        </div>"""

files = glob.glob('*.html') + glob.glob('HSE/*.html') + glob.glob('tentang/*.html')
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    if old_footer_bottom in content:
        content = content.replace(old_footer_bottom, new_footer_bottom)
        with open(f, 'w') as file:
            file.write(content)
        print(f"Updated {f}")
    else:
        print(f"Skipped {f}")
