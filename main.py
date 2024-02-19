import pyautogui
import time


def read_file(filename):
    f = open(filename, "r")
    stuff = f.read()
    f.close()
    return stuff


def type_text(start, sentence):
    wc = start
    try:
        for word in sentence.split(" ")[wc:]:
            pyautogui.write(word, interval=0.10)
            pyautogui.write(" ")
            wc += 1
            print("Typing word #" + str(wc) + " is '" + word + "'")
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
        exit(1)
    print("Will begin typing in 3 seconds...\n")
    time.sleep(3)
    progress = type_text(progress, text)

    if progress > 0:
        print("\nFinished typing all " + str(progress) + " words.\n")
    else:
        print('\nRemember to continue at word #' + str(-progress) + "...\n")


if __name__ == '__main__':
    main()
