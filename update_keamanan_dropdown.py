import os
import re

BASE_DIR = '/Users/wirantochalik/Desktop/BCIP'

# Define the keamanan sub-dropdown for different path depths
def get_keamanan_subdropdown(prefix):
    """Generate Keamanan sub-dropdown HTML with appropriate path prefix."""
    return f'''                    <div class="sub-dropdown">
                        <a href="{prefix}HSE/keamanan.html" class="dropdown-item">
                            <i class="fa-solid fa-shield-halved"></i> Keamanan <i class="fa-solid fa-chevron-down sub-dropdown-icon"></i>
                        </a>
                        <div class="sub-dropdown-menu">
                            <a href="{prefix}HSE/sub-hse-keamanan/secure-and-asset-management.html" class="dropdown-item">Secure and Asset Management</a>
                            <a href="{prefix}HSE/sub-hse-keamanan/operation-control.html" class="dropdown-item">Operation Control</a>
                            <a href="{prefix}HSE/sub-hse-keamanan/fasilitas-hse.html" class="dropdown-item">Fasilitas HSE</a>
                            <a href="{prefix}HSE/sub-hse-keamanan/security-patrol.html" class="dropdown-item">Security Patrol</a>
                            <a href="{prefix}HSE/sub-hse-keamanan/insection-sajam-alcohol-and-drug.html" class="dropdown-item">Insection Sajam, Alcohol and Drug</a>
                        </div>
                    </div>'''

# Patterns to match the old Keamanan link (various formats found in the codebase)
# Pattern 1: root level (index.html, berita.html) - prefix is empty or ""
# Pattern 2: HSE level (HSE/*.html) - prefix is "../"
# Pattern 3: sub-HSE level (HSE/sub-hse-*/*.html) - prefix is "../../"
# Pattern 4: tentang level (tentang/*.html) - prefix is "../"

def get_prefix_for_file(filepath):
    """Determine the correct prefix based on file location."""
    rel = os.path.relpath(filepath, BASE_DIR)
    parts = rel.split(os.sep)
    
    if len(parts) == 1:
        # Root level: index.html, berita.html
        return ''
    elif len(parts) == 2:
        # One level deep: HSE/*.html, tentang/*.html
        return '../'
    elif len(parts) == 3:
        # Two levels deep: HSE/sub-hse-*/*.html
        return '../../'
    return ''

def process_file(filepath):
    """Process a single HTML file to replace Keamanan link with sub-dropdown."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip files in sub-hse-keamanan (they already have the correct navbar)
    if 'sub-hse-keamanan' in filepath:
        return False
    
    prefix = get_prefix_for_file(filepath)
    new_dropdown = get_keamanan_subdropdown(prefix)
    
    # Try various patterns of the old Keamanan link
    # The key patterns observed:
    
    # Pattern for root level files (index.html, berita.html):
    # <a href="HSE/keamanan.html" class="dropdown-item"><i class="fa-solid fa-shield-halved"></i>\n                         Keamanan</a>
    
    # Pattern for HSE level files:
    # <a href="keamanan.html" class="dropdown-item"><i class="fa-solid fa-shield-halved"></i> Keamanan</a>
    
    # Pattern for sub-HSE level files:
    # <a href="../keamanan.html" class="dropdown-item"><i class="fa-solid fa-shield-halved"></i> Keamanan</a>
    
    # Pattern for tentang level files:
    # <a href="../HSE/keamanan.html" class="dropdown-item"><i class="fa-solid fa-shield-halved"></i> Keamanan</a>
    
    # Use regex to match all variants
    # Match the entire keamanan link line(s)
    patterns = [
        # Multi-line pattern (root level)
        r'[ \t]*<a href="[^"]*keamanan\.html" class="dropdown-item"><i class="fa-solid fa-shield-halved"></i>\s*\n\s*Keamanan</a>',
        # Single line pattern
        r'[ \t]*<a href="[^"]*keamanan\.html" class="dropdown-item"><i class="fa-solid fa-shield-halved"></i> Keamanan</a>',
    ]
    
    modified = False
    for pattern in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, new_dropdown, content)
            modified = True
            break
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {filepath}')
        return True
    else:
        print(f'No match found: {filepath}')
        return False

# Find all HTML files
count = 0
for root, dirs, files in os.walk(BASE_DIR):
    # Skip .git directory
    if '.git' in root:
        continue
    for filename in files:
        if filename.endswith('.html'):
            filepath = os.path.join(root, filename)
            if process_file(filepath):
                count += 1

print(f'\nTotal files updated: {count}')
