import cv2
import os
import time
#import http.server
#import socketserver

#PORT = 8000
#Handler = http.server.SimpleHTTPRequestHandler

# 保存先フォルダのパス
save_dir = 'image_dir'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
# カメラの設定
camera = cv2.VideoCapture(0) # 0は内蔵カメラ、1以上は外付けカメラを指定
camera.set(3,640)# 320 320 640 720
camera.set(4,360)#180 240  360 405

# カメラから画像を読み込んで保存するループ
#with socketserver.TCPServer(("", PORT), Handler) as httpd:
    #print("serving at port", PORT)
while True:
    ret, frame = camera.read() # カメラから画像を読み込む

    # 画像の保存先ファイル名を作成
    filename = os.path.join(save_dir,'image.jpg')

    # 画像を保存
    cv2.imwrite(filename, frame)

    # 0.1秒待つ
    time.sleep(2.0)
    #httpd.serve_forever()
