import tkinter
from tkinter import messagebox
from downloader import enter as dl
import threading
from time import perf_counter


def main():
    window = tkinter.Tk()
    window.resizable(False, False)

    def final(aicao, achoice):
        tkinter.messagebox.showinfo("Alert", "Click OK to download - Program may become unresponsive for some time")
        start = perf_counter()
        threads = []
        i = 1
        while i <= 3:
            t = threading.Thread(target=dl, args=(aicao, i, achoice))
            t.start()
            threads.append(t)
            i += 1
        for thread in threads:
            thread.join()
        finish = perf_counter()
        tkinter.messagebox.showinfo("Done!", "Finished in " + str(round(finish - start, 1)) + ' seconds')

    window.title("ChartDownloader")
    window.configure(bg='grey')

    def finalthreading(bicao, bchoice):
        t1 = threading.Thread(target=final, args=(bicao, bchoice))
        t1.start()

    i = tkinter.StringVar(window, value='KSAT')
    tkinter.Label(window,
                  bg='grey',
                  fg='white',
                  text="Enter ICAO: ",
                  font="Verdana 10 bold")\
        .grid(row=1, sticky=tkinter.W)

    icao = tkinter.Entry(window, textvariable=i)
    icao.grid(row=1, column=1, sticky=tkinter.W)
    choice = tkinter.IntVar()
    choice.set(1)

    tkinter.Radiobutton(window,
                        bg='grey',
                        text="PDF format",
                        padx=20,
                        variable=choice,
                        value=2)\
        .grid(sticky=tkinter.W)

    tkinter.Radiobutton(window, bg='grey',
                        text="Aerobask (PNG) format",
                        padx=20,
                        variable=choice,
                        value=1)\
        .grid(sticky=tkinter.W)

    tkinter.Button(window,
                   bg='grey',
                   text='Download',
                   command=lambda: finalthreading(icao.get(), choice.get()))\
        .grid(row=4, column=1, sticky=tkinter.W, pady=4)

    tkinter.Button(window,
                   bg='grey',
                   text='Quit',
                   command=window.quit)\
        .grid(row=4, column=0, sticky=tkinter.W, pady=4)

    window.mainloop()


main()
