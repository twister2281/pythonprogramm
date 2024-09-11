import os
import time
from datetime import datetime
import pyautogui

def take_screenshot_and_save(folder_path):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"screenshot_{timestamp}.png"
    file_path = os.path.join(folder_path, file_name)
    screenshot = pyautogui.screenshot()
    screenshot.save(file_path)
    print(f"Скриншот сохранен: {file_path}")
def main():
    folder_path = "C:/Users/user/Desktop/test" 
# Путь папки должен быть свой!!
# И обязательно нужно поменять кривые левые палочки на кривые правые "C:/Users/user/Desktop/test" - вот так
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    try:
        while True:
            take_screenshot_and_save(folder_path)
            time.sleep(5)
    except KeyboardInterrupt:
        print("Программа завершена.")
if __name__ == "__main__":
    main()
