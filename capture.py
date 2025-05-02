
import pyautogui as auto
import time
import pyperclip
import random

start_page = 465
total_page = 780
book_name = '머신러닝'
capture_pos = (144, 200)# 캡쳐버튼 위치
ebook_screen_center_pos = (2500, 900)#ebook 선택 위치
const_sleep_time = 0.2

time.sleep(3.)#딜레이 주고 시작

for i in range(start_page, total_page, 2):
    file_name = book_name + '_' + str(i).zfill(4) + '.png'
    sleep_time = const_sleep_time + random.random()
    pyperclip.copy(file_name)

    auto.click(capture_pos)
    time.sleep(sleep_time)

    auto.hotkey('ctrl', 'v')
    time.sleep(sleep_time)
    auto.press('enter')
    time.sleep(sleep_time)

    auto.click(ebook_screen_center_pos)
    time.sleep(sleep_time)

    auto.press('right')
    time.sleep(sleep_time)
    auto.press('f5')
    time.sleep(2+sleep_time)

    print(i, '/', total_page - start_page +1)