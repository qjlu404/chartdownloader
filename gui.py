#import tkinter
from downloader import enter as dl


def main():
#    window = tkinter.Tk()
#    window.mainloop()

    condit = True
    while condit:
        icao = input("enter ICAO: ")
        choice = input('Save for Aerobask aircraft?(y/n): ')

        if len(icao) != 4:
            print('ICAO must be four characters')
        elif len(choice) != 1:
            print('Aerobask choice can only be one character')
        elif choice.lower() != "y":
            print('Must be Y/N')
        elif choice.lower() != 'n':
            print('Must be Y/N')
        else:
            condit = False
    n = 1
    while n < 5:
        dl(icao, str(n), choice)
        n += 1

