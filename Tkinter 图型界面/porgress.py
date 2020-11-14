from threading import Thread
from time import sleep
import tkinter
import tkinter.ttk


def on_loading(widget, value, loading_end):
    print('loading...')
    widget.start(150)
    sleep(15)
    widget.stop()
    value(100)
    on_ready()


def on_ready():
    print("now ready to work...")


def main():
    root = tkinter.Tk()
    ft = tkinter.ttk.Frame()
    ft.pack(expand=True, fill=tkinter.BOTH, side=tkinter.TOP)

    value = 0  # the value of the progressbar
    setvalue = lambda x, value=value: value + x  # the lambda to capture value
    pb_hd = tkinter.ttk.Progressbar(ft, orient='horizontal', mode='determinate', max=100.0, variable=value)
    pb_hd.pack(expand=True, fill=tkinter.BOTH, side=tkinter.TOP)

    # Creates a thread that call on_loading
    Thread(target=on_loading, args=(pb_hd, setvalue, on_loading)).start()
    root.mainloop()


if __name__ == '__main__':
    main()
