import json

JSON_PATH = "./pos.json"
MIN_SENS = 835
MAX_SENS = 1030

def GetUserInfo():
    print("-------------------------------")
    print("       STANDARD KEYBINDS       ")
    print("Set Settings: v")
    print("STANDARD FPS: 90 (WHEN YOU DO 'Set Settings)'")
    print("Set 30 FPS: b")
    print("Set 60 FPS: n")
    print("Set 90 FPS: m")
    print("Set 120 FPS: l")
    print("IF YOU ARE FINE WITH THE KEYBINDS ONLY DO MOUSE SENS TO SAVE YOU SOME TIME")
    print("-------------------------------")
    print("Insert 1, 2, 3, 4, 5, 6 or 7")
    print("Setup EVERYTHING (If first time choose this): 1")
    print("Setup ONLY mouse sens: 2")
    print("Setup ONLY set settings hotkey: 3")
    print("Setup ONLY set 30 fps hotkey: 4")
    print("Setup ONLY set 60 fps hotkey: 5")
    print("Setup ONLY set 90 fps hotkey: 6")
    print("Setup ONLY set 120 fps hotkey: 7")
    print("-------------------------------")
    
    cmd = int(input("> "))
    
    mouse_msg = "Insert your desired mouse sens (0 - 195)"
    settings_hotkey_msg = "Insert your desired hotkey for the script"
    fps_hotkey_msg = f"Insert your desired hotkey for "
    
    if (cmd == 1):
        print(mouse_msg)
        mouse_sens = int(input("> "))
        print(settings_hotkey_msg)
        set_settings_hotkey = str(input("> "))
        print(fps_hotkey_msg + "30 fps")
        set_30_fps_hotkey = str(input("> "))
        print(fps_hotkey_msg + "60 fps")
        set_60_fps_hotkey = str(input("> "))
        print(fps_hotkey_msg + "90 fps")
        set_90_fps_hotkey = str(input("> "))
        print(fps_hotkey_msg + "120 fps")
        set_120_fps_hotkey = str(input("> "))
        user_mouse_sens = MIN_SENS + mouse_sens
        return (user_mouse_sens, set_settings_hotkey, set_30_fps_hotkey, set_60_fps_hotkey, set_90_fps_hotkey, set_120_fps_hotkey, cmd)
    elif (cmd == 2):
        print(mouse_msg)
        mouse_sens = int(input("> "))
        user_mouse_sens = MIN_SENS + mouse_sens
        return (user_mouse_sens, cmd)
    elif (cmd == 3):
        print(settings_hotkey_msg)
        set_settings_hotkey = str(input("> "))
        return (set_settings_hotkey, cmd)
    elif (cmd == 4):
        print(fps_hotkey_msg + "30 fps")
        set_30_fps_hotkey = str(input("> "))
        return(set_30_fps_hotkey, cmd)
    elif (cmd == 5):
        print(fps_hotkey_msg + "60 fps")
        set_60_fps_hotkey = str(input("> "))
        return(set_60_fps_hotkey, cmd)
    elif (cmd == 6):
        print(fps_hotkey_msg + "90 fps")
        set_90_fps_hotkey = str(input("> "))
        return(set_90_fps_hotkey, cmd)
    elif (cmd == 7):
        print(fps_hotkey_msg + "120 fps")
        set_120_fps_hotkey = str(input("> "))
        return(set_120_fps_hotkey, cmd)
    else:
        print("That's not valid :)")
        GetUserInfo()

def InsertIntoJson():
    with open('pos.json') as f:
        data = json.load(f)
    
    UserInfo = GetUserInfo()
    UserInfoLen = len(UserInfo)
    
    if (UserInfoLen == 7):
        User_mouse_sens = UserInfo[0]
        User_set_settings_hotkey = UserInfo[1]
        User_set_fps_30_hotkey = UserInfo[2]
        User_set_fps_60_hotkey = UserInfo[3]
        User_set_fps_90_hotkey = UserInfo[4]
        User_set_fps_120_hotkey = UserInfo[5]
        UserCMDSelect = UserInfo[6]
    elif (UserInfoLen == 2):
        User_hotkey = UserInfo[0]
        UserCMDSelect = UserInfo[1]
    
    hotkey = 'hot-key'
    mousesens = 'mouse-sens'
    setsettings = 'set-settings'
    
    if (UserCMDSelect == 1):
        data[mousesens][0]["x"] = User_mouse_sens
        data[hotkey][0][setsettings] = User_set_settings_hotkey
        data[hotkey][0]['fps-30'] = User_set_fps_30_hotkey
        data[hotkey][0]['fps-60'] = User_set_fps_60_hotkey
        data[hotkey][0]['fps-90'] = User_set_fps_90_hotkey
        data[hotkey][0]['fps-120'] = User_set_fps_120_hotkey
    elif (UserCMDSelect == 2):
        data[mousesens][0]["x"] = User_hotkey
    elif (UserCMDSelect == 3):
        data[hotkey][0][setsettings] = User_hotkey
    elif (UserCMDSelect == 4):
        data[hotkey][0]['fps-30'] = User_hotkey
    elif (UserCMDSelect == 5):
        data[hotkey][0]['fps-60'] = User_hotkey
    elif (UserCMDSelect == 6):
        data[hotkey][0]['fps-90'] = User_hotkey
    elif (UserCMDSelect == 7):
        data[hotkey][0]['fps-120'] = User_hotkey

    with open(JSON_PATH, "w") as f:
        json.dump(data, f)
    print("Settings have been saved!")
def main():
    print("""
  ____  ______ _______ ____  _   _  _____  _____     ____  _   _ _  __     __   _    _ _____      _____  _____ _____  _____ _____ _______ 
 |  _ \|  ____|__   __/ __ \| \ | |/ ____|/ ____|   / __ \| \ | | | \ \   / /  | |  | |  __ \    / ____|/ ____|  __ \|_   _|  __ \__   __|
 | |_) | |__     | | | |  | |  \| | |  __| (___    | |  | |  \| | |  \ \_/ /   | |  | | |__) |  | (___ | |    | |__) | | | | |__) | | |   
 |  _ <|  __|    | | | |  | | . ` | | |_ |\___ \   | |  | | . ` | |   \   /    | |  | |  ___/    \___ \| |    |  _  /  | | |  ___/  | |   
 | |_) | |____   | | | |__| | |\  | |__| |____) |  | |__| | |\  | |____| |     | |__| | |        ____) | |____| | \ \ _| |_| |      | |   
 |____/|______|  |_|  \____/|_| \_|\_____|_____/    \____/|_| \_|______|_|      \____/|_|       |_____/ \_____|_|  \_\_____|_|      |_|   
                                                                                                                                          
 """)
    
    InsertIntoJson()
    
if __name__ == "__main__":
    main()