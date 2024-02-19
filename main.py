import pyautogui
import time

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

def type_text(start, sentence):
    words = sentence.split()
    wc = start
    try:
        for i, word in enumerate(words, start=start):
            pyautogui.write(word, interval=0.10)
            pyautogui.press("space")
            print(f"Typing word #{i}: {word}")
            wc = i
            time.sleep(0.2)
        return wc
    except KeyboardInterrupt:
        return -wc

def main():
    progress = 0
    try:
        text = read_file("answer.txt")
    except FileNotFoundError:
        print("The file does not exist. Make one!\n")
        return

    print("Will begin typing in 3 seconds...\n")
    time.sleep(3)

    progress = type_text(progress, text)
    if progress > 0:
        print("\nFinished typing all " + str(progress) + " words.\n")
    else:
        print('\nRemember to continue at word #' + str(-progress) + "...\n")

if __name__ == '__main__':
    main()
