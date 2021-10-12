import mss
from getwinname import GetWindowRectFromName,TargetWindowTitle




bbox=GetWindowRectFromName(TargetWindowTitle)

def SCT(bbox):
    with mss.mss() as sct:
        img=sct.grab(bbox)
    return img