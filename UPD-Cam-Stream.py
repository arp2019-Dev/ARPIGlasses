#!/usr/bin/env python3
import socket
import cv2
import numpy as np

HOST = "0.0.0.0"
PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print(f"? Listening on UDP {HOST}:{PORT}")

while True:
    data, addr = sock.recvfrom(65535)
    arr = np.frombuffer(data, np.uint8)
    frame = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if frame is None:
        continue
    mirrored = cv2.flip(frame, 1)
    cv2.imshow("?? Low-Latency Mirror Stream", mirrored)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

sock.close()
cv2.destroyAllWindows()
