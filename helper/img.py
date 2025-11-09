from helper.json_actions import read_json

from mss import mss
import mss.tools


def capture():
    
    with mss.mss() as sct:
        monitor_number = int(read_json("settings.json", "monitor_number"))
        monitor = sct.monitors[monitor_number]
        im = sct.grab(monitor)
        mss.tools.to_png(im.rgb, im.size, output="screenshot.png")
        print(f"Screenshot taken from Monitor Number: {monitor_number} as screenshot.png")