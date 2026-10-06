with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check where baseera section is
start_baseera = html.find('<section id="baseera">')
end_baseera = html.find('</section>', start_baseera)

print('Baseera section start:', start_baseera)
print('Baseera section end:', end_baseera)
print('Section content:\n', html[start_baseera:end_baseera+10])
