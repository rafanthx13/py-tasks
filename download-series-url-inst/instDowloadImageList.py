from datetime import datetime
from tqdm import tqdm
import requests
import re
import sys

import random
import string

# Tem que ser com esse prefix e os links somente. Exemplo
# Ingles
# https://www.instagram.com/p/CAc5Z_cH_Fo/
# https://www.instagram.com/p/CAfbS8cFPL-/
# 
# food
# https://www.instagram.com/p/CAL2KKjFjbD/
# https://www.instagram.com/p/B_-jfkVAAY2/
# https://www.instagram.com/p/CAL2KKjFjbD/

# Ultimo Download: 21/02/2021

alist = """

portugues
https://www.instagram.com/p/CL2Avs1Dk86/
https://www.instagram.com/p/CL43kmRD6GX/
https://www.instagram.com/p/CNyIt2DDFkU/

be_male
https://www.instagram.com/p/CNH-EYDJhZC/

random
https://www.instagram.com/p/CNC7igLng5m/

fitness
https://www.instagram.com/p/CMAQcX4oIGa/
https://www.instagram.com/p/CNXSYZijsnh/
https://www.instagram.com/p/CMrnV44HDFv/
https://www.instagram.com/p/CMtFTesjMdP/
https://www.instagram.com/p/CMTfxwLDUSt/
https://www.instagram.com/p/CMTxYpBj58t/

namoro
https://www.instagram.com/p/CL2YtWMJka5/
https://www.instagram.com/p/CMCKCbap0vh/
https://www.instagram.com/p/CMDdp1Bpuli/
https://www.instagram.com/p/CMHqQ1mpSE8/
https://www.instagram.com/p/CN01uhEJj5Y/
https://www.instagram.com/p/CMrukTcp5ci/
https://www.instagram.com/p/CMrvAsfpDli/
https://www.instagram.com/p/CMoABEZpvhX/

direita
https://www.instagram.com/p/CNz79_0sirt/

ULTRA
https://www.instagram.com/p/CNfP5Hjp4ou/
https://www.instagram.com/p/CNfP33fpLk2/

receitas
https://www.instagram.com/p/CL7Cop0Fk9j/
https://www.instagram.com/p/CMLWaGUgUjq/

hair
https://www.instagram.com/p/CNfNSUQh6Nw/
https://www.instagram.com/p/CNVLZvWnMpI/
https://www.instagram.com/p/CMjle9GhGFS/

tmdz
https://www.instagram.com/p/CMHqMNXJItr/
https://www.instagram.com/p/CNgEGm8pKws/
https://www.instagram.com/p/CNgD4gVpDJ6/
https://www.instagram.com/p/CNfRiP9J4nE/
https://www.instagram.com/p/CNIz625FqZT/
https://www.instagram.com/p/CMZn4B4A2Hh/
https://www.instagram.com/p/CMQDMfsheqp/

english
https://www.instagram.com/p/CL9MxwzHFY1/
https://www.instagram.com/p/CMCLdDTH-w_/
https://www.instagram.com/p/CNm1dBtnSZ6/
https://www.instagram.com/p/CNUnJ-YLnxR/

gw
https://www.instagram.com/p/CKznogRpbNe/
https://www.instagram.com/p/CKgxp5YJ8QG/
https://www.instagram.com/p/CL5hNmqpjy-/
https://www.instagram.com/p/CMBCM4hsYaB/
https://www.instagram.com/p/CNtdG_blpYM/
https://www.instagram.com/p/CNkz_2kJHmY/
https://www.instagram.com/p/CMdcyRnJWPP/
https://www.instagram.com/p/CMdlNGnpm2f/
https://www.instagram.com/p/CMHrrS-pjBT/

"""

alist = alist.split("\n")
alist.pop(0)
alist.pop()

print(alist)

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#Function to check the internet connection
#Got this from https://stackoverflow.com/a/24460981

def connection(url='http://www.google.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        print("You're connected to internet\n")
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

#Function to download an instagram photo or video
def download_image_video(url, prefix):

    # url = input("Please enter image URL: ")
    x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', url)
    
    try:
        if x:
            print('Request URL ...', url)
            request_image = requests.get(url)
            src = request_image.content.decode('utf-8')
            print('src', src)
            check_type = re.search(r'<meta name="medium" content=[\'"]?([^\'" >]+)', src)
            print('check_type', check_type)
            check_type_f = check_type.group()
            final = re.sub('<meta name="medium" content="', '', check_type_f)

            if final == "image":
                print("\nDownloading the image...")
                extract_image_link = re.search(r'meta property="og:image" content=[\'"]?([^\'" >]+)', src)
                image_link = extract_image_link.group()
                final = re.sub('meta property="og:image" content="', '', image_link)
                _response = requests.get(final).content
                file_size_request = requests.get(final, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = prefix + "_" + randomString() + "_" + datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.jpg', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                print("Image downloaded successfully")

            if final == "video": 
                msg = input("You are trying to download a video. Do you want to continue? (Yes or No): ".lower())

                if msg == "yes":
                    print("Downloading the video...")
                    extract_video_link = re.search(r'meta property="og:video" content=[\'"]?([^\'" >]+)', src)
                    video_link = extract_video_link.group()
                    final = re.sub('meta property="og:video" content="', '', video_link)
                    _response = requests.get(final).content
                    file_size_request = requests.get(final, stream=True)
                    file_size = int(file_size_request.headers['Content-Length'])
                    block_size = 1024 
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                    with open(filename + '.mp4', 'wb') as f:
                        for data in file_size_request.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)
                    t.close()
                    print("Video downloaded successfully")

                if msg == "no":
                    exit()  
        else:
            print("Entered URL is not an instagram.com URL.")
    except Exception as e:
        print(e)

if connection() == True:
    prefix = ""
    for el in alist:
      isLink = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', el)
      if(not isLink):
        prefix = el
      else:
        download_image_video(el, prefix)

else:
	sys.exit()
