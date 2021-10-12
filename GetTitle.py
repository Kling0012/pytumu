from ahk import AHK

window_title = "Discord"


def GetTitle(window_title):
    ahk = AHK()
    wins = list(ahk.windows())
    titles = [win.title for win in wins]
    for t in titles:
        text = t.decode("shift-jis", errors="ignore")
        if window_title in text:
            return text
