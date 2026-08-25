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

    # Replace `../` with `../../` first!
    content = content.replace('href="../', 'href="../../')
    content = content.replace('src="../', 'src="../../')

    # THEN, replace exact local links in HSE directory to point to parent HSE folder:
    content = content.replace('href="kesehatan-kerja.html"', 'href="../kesehatan-kerja.html"')
    content = content.replace('href="lingkungan.html"', 'href="../lingkungan.html"')
    content = content.replace('href="keamanan.html"', 'href="../keamanan.html"')
    content = content.replace('href="tanggap-darurat.html"', 'href="../tanggap-darurat.html"')
    
    # Also wait, index.html might have been href="../../index.html", which is correct.
    # What about berita.html? In HSE/keselamatan-kerja.html it was href="../berita.html", now it is href="../../berita.html". Correct.
    
    with open(f'HSE/sub-hse-keselamatan/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)

create_coming_soon_file('risk-management-system.html', 'Risk Management System')
create_coming_soon_file('inspection-and-monitoring.html', 'Inspection and Monitoring')
create_coming_soon_file('safety-culture.html', 'Safety Culture')
create_coming_soon_file('training-programme.html', 'Training Programme')
print("Fixed 4 HTML files properly.")
