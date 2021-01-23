#import tkinter
from downloader import enter as dl


def main():
#    window = tkinter.Tk()
#    window.mainloop()

    condit = True
    while condit:
        icao = input("enter ICAO: ")
        choice = input("save for aerobask planes?(y/n): ")
        if len(icao) is not 4:
            print("ICAO must be 4 characters")
        else: break

    n = 1
    while n < 5:
        dl(icao, str(n), choice)
        n += 1

