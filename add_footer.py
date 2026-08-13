import os
import glob

footer_html = """
    <!-- FOOTER -->
    <footer class="footer">
        <div class="footer-container">
            <!-- Left Column: Logo & Address -->
            <div class="footer-col-left">
                <img src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=375,fit=crop,q=95/dOqqPM8w81tpv1go/Logo-BCIP-baru-small-mePPpRnL71H1D2NO.png" alt="BCIP Logo" class="footer-logo">
                
                <div class="footer-contact-info">
                    <p><strong>Wilayah:</strong> Desa Sekerat, Kecamatan Bengalon</p>
                    <p><strong>Kabupaten:</strong> Kutai Timur, Kalimantan Timur</p>
                    <p><strong>Kode Pos:</strong> 75618</p>
                    
                    <div class="contact-details">
                        <p>Phone : +62 853-8888-1989</p>
                        <p>Email : info@batutachemical.co.id</p>
                    </div>
                </div>
            </div>

            <!-- Middle Columns: Links -->
            <div class="footer-col">
                <h4>Tentang</h4>
                <ul>
                    <li><a href="../tentang/komitmen-kebijakan.html">Komitmen & Kebijakan</a></li>
                    <li><a href="../tentang/legal-compliance.html">Legal Compliance</a></li>
                    <li><a href="../tentang/people-competency.html">People & Competency</a></li>
                    <li><a href="../tentang/emergency-response.html">Emergency Response</a></li>
                    <li><a href="../tentang/our-core-values.html">Our Core Values</a></li>
                </ul>
            </div>
            
            <div class="footer-col">
                <h4>HSE</h4>
                <ul>
                    <li><a href="../HSE/keselamatan-kerja.html">Keselamatan Kerja</a></li>
                    <li><a href="../HSE/kesehatan-kerja.html">Kesehatan Kerja</a></li>
                    <li><a href="../HSE/lingkungan.html">Lingkungan</a></li>
                    <li><a href="../HSE/keamanan.html">Keamanan</a></li>
                    <li><a href="../HSE/tanggap-darurat.html">Tanggap Darurat</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Layanan</h4>
                <ul>
                    <li><a href="#">Layanan Kami</a></li>
                    <li><a href="#">Solusi Industri</a></li>
                    <li><a href="#">Kawasan Berikat</a></li>
                    <li><a href="#">Logistik</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Berita</h4>
                <ul>
                    <li><a href="#">Siaran Pers</a></li>
                    <li><a href="#">Artikel Terkini</a></li>
                    <li><a href="#">Pengumuman</a></li>
                    <li><a href="#">CSR & Komunitas</a></li>
                </ul>
            </div>

            <!-- Right Column: Social Media -->
            <div class="footer-col-right">
                <h4>Media Sosial</h4>
                <ul class="social-links-list">
                    <li><a href="#"><i class="fa-brands fa-instagram"></i> @bcip_official</a></li>
                    <li><a href="#"><i class="fa-brands fa-linkedin"></i> @bcip_official</a></li>
                    <li><a href="#"><i class="fa-brands fa-youtube"></i> @bcip_official</a></li>
                    <li><a href="#"><i class="fa-brands fa-tiktok"></i> @bcip_official</a></li>
                </ul>
            </div>
        </div>
        
        <div class="footer-bottom">
            <p>Copyright &copy;2026 Batuta Chemical Industrial Park</p>
        </div>
    </footer>
"""

files = glob.glob('HSE/*.html') + glob.glob('tentang/*.html')
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    if "<!-- FOOTER -->" not in content:
        content = content.replace("    <!-- WhatsApp Floating Button -->", footer_html + "\n    <!-- WhatsApp Floating Button -->")
        with open(f, 'w') as file:
            file.write(content)
        print(f"Updated {f}")
    else:
        print(f"Skipped {f}")
