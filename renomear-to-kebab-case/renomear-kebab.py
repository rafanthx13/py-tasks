# Renomar todos os arquivos da pasta atual para kebab-case
import os

def kebab_case(text):
    text = text.replace(' ', '')
    return '-'.join(text.lower().split())

for filename in os.listdir('.'):
    if os.path.isfile(filename):
        new_filename = kebab_case(filename)
        os.rename(filename, new_filename)

