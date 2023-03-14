import cv2
import threading
from django.http import StreamingHttpResponse

class Camera:
    def __init__(self):


        self.video = cv2.VideoCapture(0)

    def __del__(self):

        self.video.release()

    def get_frame(self):

        ret, frame = self.video.read()

        if ret:
            _, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        else:
            return None