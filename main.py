import pyautogui
import time
import webbrowser

url = "https://www.youtube.com/results?search_query=Sweet+Child+O%27+Mine"

webbrowser.open(url)

time.sleep(7)

pyautogui.click(500, 250)

time.sleep(5)

# If u wanna put other songs, just change the url variable to the new song's search query. For example, if you want to search for "Bohemian Rhapsody", you can change the url variable like this:
# url = "https://www.youtube.com/results?search_query=Bohemian+Rhapsody"
# And if u wanna put the video on full screen, you can add the following line after the pyautogui.click() line:
# pyautogui.press('f')
