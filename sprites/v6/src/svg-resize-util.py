#!/usr/bin/env python3
import os
import re

directory = './new_v2'

for filename in os.listdir(directory):
    if not filename.endswith('.svg'):
        continue
    
    # Skip all shield files EXCEPT Virginia and Maryland shields
    
    
    filepath = os.path.join(directory, filename)
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Target size
    new_size = 20
    
    # Extract current width/height
    width_match = re.search(r'<svg[^>]*width="([\d.]+)"', content)
    height_match = re.search(r'<svg[^>]*height="([\d.]+)"', content)
    
    if not width_match or not height_match:
        print(f'⊘ {filename} - no dimensions found')
        continue
    
    old_width = float(width_match.group(1))
    old_height = float(height_match.group(1))
    
    # Update the SVG: set new size and create/update viewBox with old dimensions
    def update_svg(match):
        svg_content = match.group(0)
        # Remove existing viewBox, width, height
        svg_content = re.sub(r'\s*viewBox="[^"]*"', '', svg_content)
        svg_content = re.sub(r'\s*width="[^"]*"', '', svg_content)
        svg_content = re.sub(r'\s*height="[^"]*"', '', svg_content)
        # Add back with new values
        svg_content = svg_content.rstrip('>')
        svg_content += f' width="{new_size}" height="{new_size}" viewBox="0 0 {old_width} {old_height}">'
        return svg_content
    
    content = re.sub(r'<svg[^>]*>', update_svg, content)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f'✓ {filename}: {old_width}x{old_height} → {new_size}x{new_size} (viewBox preserves original)')

print('\nDone! Now run:')
print('spreet --ratio 1 light light')
print('spreet --ratio 2 light@2x light')