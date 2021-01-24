import tkinter
from tkinter import messagebox
from downloader import enter as dl


def main():

    window = tkinter.Tk()

    def convert(aicao, achoice):
        tkinter.messagebox.showinfo("Alert", "Click OK to download - Program may become unresponsive for some time")
        n = 1
        while n < 5:
            dl(aicao, n, achoice)
            n += 1
        tkinter.messagebox.showinfo("Alert", "Finished!")

    window.title("ChartDownloader")
    icao = tkinter.Entry(window)
    window.configure(bg='grey')
    tkinter.Label(window, bg='grey', fg='white', text="Enter ICAO: ", font="Verdana 10 bold").grid(row=1, sticky=tkinter.W)
    choice = tkinter.IntVar()
    tkinter.Radiobutton(window, bg='grey', text="PDF format", padx=20, variable=choice, value=2).grid(sticky=tkinter.W)
    tkinter.Radiobutton(window, bg='grey', text="Aerobask (PNG) format", padx=20, variable=choice, value=1).grid(sticky=tkinter.W)
    tkinter.Button(window, bg='grey', text='download', command=lambda: convert(icao.get(), choice.get())).grid(row=4, column=1, sticky=tkinter.W, pady=4)
    icao.grid(row=1, column=1, sticky=tkinter.W)
    tkinter.Button(window, bg='grey', text='Quit', command=window.quit).grid(row=4, column=0, sticky=tkinter.W, pady=4)
    window.mainloop()


main()
