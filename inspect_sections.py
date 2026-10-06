with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
en_match = re.search(r'var EN\s*=\s*(\{.*?\});', text, re.DOTALL)
if en_match:
    with open('en_dict.txt', 'w', encoding='utf-8') as out:
        out.write(en_match.group(1))
    print('EN dict saved, length:', len(en_match.group(1)))
