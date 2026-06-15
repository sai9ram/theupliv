with open('academy.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Card solid backgrounds (rich dark tint per accent color)
replacements = [
    # Card 1 green — transparent bg → solid dark green tint
    (
        'border:1px solid rgba(197,235,217,0.4);background:rgba(197,235,217,0.03);\n                                    box-shadow:0 0 60px 0 rgba(197,235,217,0.08);',
        'border:2px solid rgba(197,235,217,0.55);background:#0c1e15;\n                                    box-shadow:0 8px 40px 0 rgba(197,235,217,0.12);'
    ),
    # Card 2 purple
    (
        'border:1px solid rgba(129,140,248,0.1);background:rgba(255,255,255,0.02);\n                                    z-index:40;',
        'border:2px solid rgba(129,140,248,0.5);background:#0e0e1e;\n                                    z-index:40;'
    ),
    # Card 3 amber
    (
        'border:1px solid rgba(245,158,11,0.1);background:rgba(255,255,255,0.02);\n                                    z-index:30;',
        'border:2px solid rgba(245,158,11,0.5);background:#1a1400;\n                                    z-index:30;'
    ),
    # Card 4 teal
    (
        'border:1px solid rgba(52,211,153,0.1);background:rgba(255,255,255,0.02);\n                                    z-index:20;',
        'border:2px solid rgba(52,211,153,0.5);background:#091a12;\n                                    z-index:20;'
    ),
    # Card 5 red
    (
        'border:1px solid rgba(248,113,113,0.1);background:rgba(255,255,255,0.02);\n                                    z-index:10;',
        'border:2px solid rgba(248,113,113,0.5);background:#1a0909;\n                                    z-index:10;'
    ),
]

count = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        count += 1
        print(f'Replaced card {count}')
    else:
        print(f'WARNING: pattern not found for card {count+1}')
        # Try partial match debug
        short = old[:60]
        if short in html:
            print(f'  Partial match found for first 60 chars')
        else:
            print(f'  No match at all. Looking for: {repr(short)}')

with open('academy.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nDone. {count}/5 replacements made.')
