import requests
from utils.const import UPLOAD_PHOTO_URL

async def upload_image_to_server(file):
    print(type(file))
    result = requests.post(UPLOAD_PHOTO_URL, files={"image": file})
    print(result.json())