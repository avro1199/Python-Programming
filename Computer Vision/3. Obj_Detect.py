import cv2 as cv
import cvlib as lib
from cvlib.object_detection import draw_bbox

cam_in = cv.VideoCapture(0)

while (True):
    run, frame = cam_in.read()
    if not run:
        break

    # frame = cv

    # frame = cv.resize(frame, (1080,720), interpolation=cv.INTER_LINEAR_EXACT)
    # cv.imshow('Rj', frame)
    # print(f'height = {frame.shape[0]} , width = {frame.shape[1]}, ch = {frame.shape[2]}\n')

    # bbox, label, conf = lib.detect_common_objects(frame)
    bbox, conf = lib.detect_face(frame)
    # bbox, conf = lib.detect_gender(frame)

    print(bbox, conf)
    # if conf:
    #     frame = draw_bbox(frame, bbox=bbox,labels=['person'], confidence=conf)

    if conf:
        frame = cv.rectangle(frame, (bbox[0][0], bbox[0][1]), (bbox[0][2], bbox[0][3]), int(conf[0]*150), 2, 0)

    # out_frame = draw_bbox(frame, bbox, label, conf)
    cv.imshow('WebCam', frame)
    cv.waitKey(200)

cam_in.release()
cv.destroyAllWindows()
