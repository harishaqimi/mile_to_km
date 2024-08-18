import tkinter

def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.609
    label3.config(text=f"{km}")

window = tkinter.Tk()
window.title("Mile to KM Converter")
# window.minsize(height=100, width=300)
window.config(padx=5, pady=5)
# window.configure(bg="white")

label1 = tkinter.Label(window, text="Miles")
label1.grid(column=2, row=0)
label2 = tkinter.Label(window, text="is equal to")
label2.grid(column=0, row=1)
label3 = tkinter.Label(window, text="0")
label3.grid(column=1, row=1)
label1 = tkinter.Label(window, text="Km")
label1.grid(column=2, row=1)

entry = tkinter.Entry(width=20)
entry.grid(column=1, row=0)

button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()