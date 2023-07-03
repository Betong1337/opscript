import json
import pyautogui
import keyboard

#MIN SENSE: 835
#MAX SENSE: 1030
#195

global POS_LIST_SET_SETTINGS

POS_LIST_SET_SETTINGS = ['settings-btn', 'fps-btn', 'mouse-sens', 'save-btn', 'back-btn', 'resume-btn']

print("""
  ____  ______ _______ ____  _   _  _____  _____     ____  _   _ _  __     __   _    _ _____      _____  _____ _____  _____ _____ _______ 
 |  _ \|  ____|__   __/ __ \| \ | |/ ____|/ ____|   / __ \| \ | | | \ \   / /  | |  | |  __ \    / ____|/ ____|  __ \|_   _|  __ \__   __|
 | |_) | |__     | | | |  | |  \| | |  __| (___    | |  | |  \| | |  \ \_/ /   | |  | | |__) |  | (___ | |    | |__) | | | | |__) | | |   
 |  _ <|  __|    | | | |  | | . ` | | |_ |\___ \   | |  | | . ` | |   \   /    | |  | |  ___/    \___ \| |    |  _  /  | | |  ___/  | |   
 | |_) | |____   | | | |__| | |\  | |__| |____) |  | |__| | |\  | |____| |     | |__| | |        ____) | |____| | \ \ _| |_| |      | |   
 |____/|______|  |_|  \____/|_| \_|\_____|_____/    \____/|_| \_|______|_|      \____/|_|       |_____/ \_____|_|  \_\_____|_|      |_|   
                                                                                                                                          
 """)
print("Loading positions...")
def getPosFromJson():
    with open("./pos.json") as f:
        data = json.load(f)
    return data

def SetSettings(in_fps):
    data = getPosFromJson()
    fps_index_count = 0
    fps_index = int
    
    if in_fps == 30:
        fps_index = 0
    elif in_fps == 60:
        fps_index = 1
    elif in_fps == 90:
        fps_index = 2
    elif in_fps == 120:
        fps_index = 3
    
    pyautogui.hotkey("Escape")
    
    for pos in POS_LIST_SET_SETTINGS:
        if (fps_index_count == 1):
            x_pos = data[pos][fps_index]['x']
            y_pos = data[pos][fps_index]['y']
        else:
            x_pos = data[pos][0]['x']
            y_pos = data[pos][0]['y']
            
        pyautogui.click(1463, 461)
        pyautogui.dragTo(x_pos, y_pos)
        pyautogui.click()
        fps_index_count += 1
    
def main():
    print("Loading hotkeys...")
    data = getPosFromJson()
    set_settings_hotkey = data['hot-key'][0]['set-settings']
    default_fps = data['fps-btn'][4]['fps']
    
    fps_30_hotkey = data['hot-key'][0]['fps-30']
    fps_60_hotkey = data['hot-key'][0]['fps-60']
    fps_90_hotkey = data['hot-key'][0]['fps-90']
    fps_120_hotkey = data['hot-key'][0]['fps-120']
    
    print("Script loaded")
    while True:
        if keyboard.is_pressed(set_settings_hotkey):
            print("Set Settings")
            SetSettings(default_fps)
        elif keyboard.is_pressed(fps_30_hotkey):
            print("Set 30 FPS")
            SetSettings(30)
        elif keyboard.is_pressed(fps_60_hotkey):
            print("Set 60 FPS")
            SetSettings(60)
        elif keyboard.is_pressed(fps_90_hotkey):
            print("Set 90 FPS")
            SetSettings(90)
        elif keyboard.is_pressed(fps_120_hotkey):
            print("Set 120 FPS")
            SetSettings(120)

if __name__ == "__main__":
    main()