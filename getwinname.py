
import ctypes
from ctypes.wintypes import HWND ,DWORD,RECT

from matplotlib.patches import Rectangle

from GetTitle import GetTitle, window_title

TargetWindowTitle= GetTitle(window_title)

def GetWindowRectFromName(TargetWindowTitle):
    TargetWindowHandel = ctypes.windll.user32.FindWindowW(0,TargetWindowTitle)
    Recttangel = ctypes.wintypes,RECT()
    ctypes.windll.user32.GetwindowRect(
        TargetWindowHandel,ctypes.pointer(Rectangle))
    return (Rectangle.left,Rectangle.top,Rectangle.right,Rectangle.bottom)
