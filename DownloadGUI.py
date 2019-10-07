try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry

dateFrom = 0
dateTo = 0
root = 0

def example1(button):
    def print_sel():
        #print(cal.selection_get())
        global dateFrom
        global dateTo

        if button == "from":
            dateFrom = cal.selection_get()
            print("dateFrom is " + str(dateFrom))
        elif button == "to":
            dateTo = cal.selection_get()
            print("dateTo is " + str(dateTo))


    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2019, month=1, day=1)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def start():
    root.quit()


def main():
    global root
    root = tk.Tk()
    #root.geometry('350x200')
    s = ttk.Style(root)
    s.theme_use('clam')

    buttonFrom=ttk.Button(root, text='From', command=lambda: example1("from")).pack(padx=10, pady=10)

    buttonTo=ttk.Button(root, text='To', command=lambda: example1("to")).pack(padx=10, pady=10)

    buttonStart=ttk.Button(root, text='Start', command=start).pack(padx=10, pady=10)

    root.mainloop()

    return dateFrom, dateTo

if __name__ == '__main__':
    main()