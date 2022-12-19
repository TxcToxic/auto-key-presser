import keyboard
import time
import os


def press_key(key, timeout, log: bool = False):
    key_presses = 0
    print("starting in 3 seconds...")
    time.sleep(3)
    while True:
        try:
            keyboard.send(str(key), do_press=True, do_release=False)
            time.sleep(0.1)
            keyboard.send(str(key), do_press=False, do_release=True)
            if log:
                key_presses += 1
                print(f" [+] Pressed {key} | {key_presses}")
            time.sleep(float(timeout))
        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    os.system("title Auto-Key by -TOXIC-#1835")
    while True:
        os.system("cls")
        ckey = input(" key > ")
        ctimeout = input(" timeout > ")
        clog = input(" log pressed (y/n) > ")
        press_key(ckey, ctimeout, log=True if clog.casefold() in ('y', 'yes') else False)
