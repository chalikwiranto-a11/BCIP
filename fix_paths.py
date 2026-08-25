import os
import re

def create_coming_soon_file(filename, title):
    with open('HSE/keselamatan-kerja.html', 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'<!-- INNER HERO -->.*?<!-- FOOTER -->', re.DOTALL)
    
    new_body = f"""<!-- INNER HERO -->
    <header class="inner-hero">
        <div class="inner-hero-content">
            <h1>{title}</h1>
            <p>HSE Keselamatan Kerja</p>
        </div>
    </header>

    <!-- PAGE CONTENT -->
    <section class="page-content" style="text-align: center; padding: 100px 20px; min-height: 40vh;">
        <h2>Coming Soon</h2>
    </section>

    <!-- FOOTER -->"""
    
    content = pattern.sub(new_body, content)

    # Clean up the paths properly:
    # Everything in HSE/keselamatan-kerja.html has `../` for root elements.
    # Since we move from HSE/ to HSE/sub-hse-keselamatan/, the depth increases by 1.
    # So `../` should become `../../`.
    # And relative links to files in HSE like `kesehatan-kerja.html` should become `../kesehatan-kerja.html`.
    
    # First, replace exact local links in HSE directory:
    content = content.replace('href="kesehatan-kerja.html"', 'href="../kesehatan-kerja.html"')
    content = content.replace('href="lingkungan.html"', 'href="../lingkungan.html"')
    content = content.replace('href="keamanan.html"', 'href="../keamanan.html"')
    content = content.replace('href="tanggap-darurat.html"', 'href="../tanggap-darurat.html"')
    # Keselamatan-kerja is already replaced by the sub-dropdown block, which uses prefix. 
    # But wait, in HSE/keselamatan-kerja.html, the Keselamatan Kerja link was already transformed to a sub-dropdown!
    # Because Step 3 ran on it.
    # The sub-dropdown block in HSE/keselamatan-kerja.html has `href="../HSE/keselamatan-kerja.html"`.
    # It also has `href="../HSE/sub-hse-keselamatan/risk-management-system.html"`.
    # If we replace `../` with `../../`, then `href="../HSE/..."` becomes `href="../../HSE/..."`. This is CORRECT!
    
    # Let's replace `../` with `../../`
    content = content.replace('href="../', 'href="../../')
    content = content.replace('src="../', 'src="../../')

    with open(f'HSE/sub-hse-keselamatan/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)

create_coming_soon_file('risk-management-system.html', 'Risk Management System')
create_coming_soon_file('inspection-and-monitoring.html', 'Inspection and Monitoring')
create_coming_soon_file('safety-culture.html', 'Safety Culture')
create_coming_soon_file('training-programme.html', 'Training Programme')
print("Fixed 4 HTML files.")
