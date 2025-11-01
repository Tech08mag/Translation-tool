from mss import mss
import mss.tools


def capture(monitor_number: int):
    with mss.mss() as sct:
        monitor = sct.monitors[monitor_number]
        im = sct.grab(monitor)
        mss.tools.to_png(im.rgb, im.size, output="screenshot.png")
        print(f"Screenshot taken from Monitor Number: {monitor_number} as screenshot.png")