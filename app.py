import pikepdf
import os

def remove_pwd(filepath, pwd):
    with pikepdf.open(filepath, password=pwd) as pdf:
        num_pages = len(pdf.pages)
        print('Number of pages {}'.format(num_pages))

        filename = filepath.split('/')[-1]

        pdf.save(output_path + 'no_pwd_' + filename)

input_path = './protected/'
output_path = './unprotected/'
pwd = '793'
protected_files = os.listdir(input_path)


for file in protected_files:
    print(input_path + file)
    remove_pwd(input_path + file, pwd)