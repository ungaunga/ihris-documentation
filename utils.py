import subprocess
from PIL import Image
from io import BytesIO
import requests

def download_image(*, file_name='', save_to=''):
    response = requests.get(f'https://wiki.ihris.org/mediawiki/upload/{file_name[0].capitalize()}{file_name[1:]}')
    if response.status_code == 200:
        extensions = {'image/jpeg': '.jpg', 'image/png': '.png', 'image/jpg': '.jpg', 'image/gif': '.gif'}
        img = Image.open(BytesIO(response.content))
        img.save(f'{save_to}/{file_name}')

if __name__ == '__main__':
    download_image(file_name='dhis_frame.jpg')