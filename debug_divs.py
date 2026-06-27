import re
import sys

with open('tripplan.html', 'r', encoding='utf-8') as f:
    html = f.read()

lines = html.split('\n')
depth = 0

for i, line in enumerate(lines, 1):
    opens = len(re.findall(r'<div[>\s]', line))
    closes = len(re.findall(r'</div>', line))
    new_depth = depth + opens - closes
    if opens != closes:
        change = new_depth - depth
        clean = line.strip()[:120].encode('ascii', 'replace').decode('ascii')
        print(f'L{i:5d} (depth {depth:2d}->{new_depth:2d}) [{change:+d}]: {clean}')
    depth = new_depth

print(f'\nFinal depth at end of file: {depth}')