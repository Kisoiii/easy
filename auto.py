import pyautogui as pag  
import time
# time.sleep(5)
# pos = pag.position()

# #autoclick
# for _ in range(3)
#     pag.click(pos)
#     time.sleep(3)

# tim theo doi tuong
image = 'setting.png'
loc = pag.locateOnScreen(image)
pag.click(loc)
