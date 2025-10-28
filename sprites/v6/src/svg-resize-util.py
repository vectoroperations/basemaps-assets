#!/usr/bin/env python3
import os
import re

directory = './light'

for filename in os.listdir(directory):
    if not filename.endswith('.svg'):
        continue
    
    # Skip all shield files - leave them at original dimensions
    if filename.startswith('shield_'):
        print(f'⊘ {filename} (skipped - keeping original dimensions)')
        continue
    
    filepath = os.path.join(directory, filename)
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Standard square icons - resize to 19x19
    new_width = 19
    new_height = 19
    
    # Fix the svg tag
    def fix_svg_tag(match):
        tag = match.group(0)
        # Remove existing width and height
        tag = re.sub(r'\s+width="[^"]*"', '', tag)
        tag = re.sub(r'\s+height="[^"]*"', '', tag)
        # Add new dimensions
        tag = tag.rstrip('>') + f' width="{new_width}" height="{new_height}">'
        return tag
    
    content = re.sub(r'<svg[^>]*>', fix_svg_tag, content, count=1)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f'✓ {filename} → {new_width}×{new_height}')

print('\nDone! Now run:')
print('spreet --ratio 1 dark svg_icons')
print('spreet --ratio 2 dark@2x svg_icons')