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
MYAPP_KEY = '5245d6bac6a54cae198e9f4c1d4b2019'

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
        print(detection_result)
    # image = mosaic(args.image_file, detection_result)
    # print(face_which_list)

    # image.show()



    # 거리 기반 유사도

    # a = face_which_list[0]['faces'][0]['facial_points']
    # b = face_which_list[1]['faces'][0]['facial_points']
    # c = face_which_list[2]['faces'][0]['facial_points']
    # d = face_which_list[3]['faces'][0]['facial_points']
    # e = face_which_list[4]['faces'][0]['facial_points']
    # f = face_which_list[5]['faces'][0]['facial_points']
    # g = face_which_list[6]['faces'][0]['facial_points']
    # r = 0
    #
    #
    # for key in a.keys():
    #     for i in range(len(a[key])):
    #         r += np.linalg.norm(b[key][i][0]-a[key][i][0], ord=2)
    #         # print("------------------------------",
    #         #       math.sqrt((a[key][i][0] - b[key][i][0]) ** 2 + (a[key][i][1] - b[key][i][1]) ** 2))
    #         # print("누적값",r)
    #
    # print("아이유와 가상인물------------------------------------------", r)
    # r = 0
    # for key in a.keys():
    #     for i in range(len(a[key])):
    #         r += np.linalg.norm(b[key][i][0]-c[key][i][0], ord=2)
    #         # print("------------------------------",math.sqrt((b[key][i][0]-c[key][i][0])**2 + (b[key][i][1]-c[key][i][1])**2))
    #         # print("누적값--------------", r)
    # print("아이유와 아이유------------------------------------------", r)
    # r = 0
    # for key in a.keys():
    #     for i in range(len(a[key])):
    #         r += math.sqrt((b[key][i][0] - d[key][i][0]) ** 2 + (b[key][i][1] - d[key][i][1]) ** 2)
    #         # print("------------------------------",
    #         #       math.sqrt((b[key][i][0] - d[key][i][0]) ** 2 + (b[key][i][1] - d[key][i][1]) ** 2))
    #         # print("누적값--------------", r)
    # print("아이유와 아이유------------------------------------------", r)
    # r = 0
    # for key in a.keys():
    #     for i in range(len(a[key])):
    #         r += math.sqrt((b[key][i][0] - e[key][i][0]) ** 2 + (b[key][i][1] - e[key][i][1]) ** 2)
    #         # print("------------------------------",
    #         #       math.sqrt((b[key][i][0] - d[key][i][0]) ** 2 + (b[key][i][1] - d[key][i][1]) ** 2))
    #         # print("누적값--------------", r)
    # print("아이유와 아이유------------------------------------------", r)
    # r = 0
    # for key in a.keys():
    #     for i in range(len(a[key])):
    #         r += math.sqrt((b[key][i][0] - f[key][i][0]) ** 2 + (b[key][i][1] - f[key][i][1]) ** 2)
    #         # print("------------------------------",
    #         #       math.sqrt((b[key][i][0] - d[key][i][0]) ** 2 + (b[key][i][1] - d[key][i][1]) ** 2))
    #         # print("누적값--------------", r)
    #
    # print("아이유와 제니------------------------------------------", r)
    # r = 0
    # for key in a.keys():
    #     for i in range(len(a[key])):
    #         r += math.sqrt((b[key][i][0] - g[key][i][0]) ** 2 + (b[key][i][1] - g[key][i][1]) ** 2)
    #         # print("------------------------------",
    #         #       math.sqrt((b[key][i][0] - d[key][i][0]) ** 2 + (b[key][i][1] - d[key][i][1]) ** 2))
    #         # print("누적값--------------", r)
    # print("아이유와 유재석------------------------------------------", r)

