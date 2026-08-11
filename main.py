import pyautogui
import time
import webbrowser

url = "https://www.youtube.com/results?search_query=Sweet+Child+O%27+Mine"

webbrowser.open(url)

time.sleep(7)

pyautogui.click(500, 250)

time.sleep(5)