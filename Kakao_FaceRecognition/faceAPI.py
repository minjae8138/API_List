import sys
import argparse
import requests
from PIL import Image, ImageFilter
import pandas as pd
import numpy as np
import math
import os
print(os.getcwd())


API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
MYAPP_KEY = 'MYAPP_KEY '

def detect_face(filename):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        files = { 'image' : open(filename, 'rb')}
        resp = requests.post(API_URL, headers=headers, files=files)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)

    return image


def mosaic(filename, detection_result):
    image = Image.open(filename)

    for face in detection_result['result']['faces']:
        x = int(face['x']*image.width)
        w = int(face['w']*image.width)
        y = int(face['y']*image.height)
        h = int(face['h']*image.height)
        box = image.crop((x,y,x+w, y+h))
        box = box.resize((20,20), Image.NEAREST).resize((w,h), Image.NEAREST)
        image.paste(box, (x,y,x+w, y+h))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Mosaic faces.')

    path_dir = './images'
    file_list = os.listdir(path_dir)

    face_which_list = []        # 최종 산출물이 담길 리스트
    for l in file_list :
        parser.add_argument('image_file', type=str, nargs='?', default="./images/{}".format(l),
                            help='image file to hide faces')
        print(l)
        args = parser.parse_args()
        detection_result = detect_face(args.image_file)
        face_which_list.append(detection_result["result"])

    # image = mosaic(args.image_file, detection_result)
    print(face_which_list)

    # image.show()




