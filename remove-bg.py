import os
import time
from removebg import RemoveBg

rmbg = RemoveBg("p5dZ8ZZgBFAXpZmGEJz8qLrK", "error.log")
path = './img/'
for img in os.listdir(path):
    if (img.endswith('jpg') or img.endswith('png') or img.endswith('jpeg')) and  not (img.endswith('jpg_no_bg.png') or img.endswith('jpg_no_bg.png')) :
        rmbg.remove_background_from_img_file(path+img)
        time.sleep(1)