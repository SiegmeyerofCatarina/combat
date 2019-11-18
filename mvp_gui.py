import tkinter as tk


def strToSortlist(event):
    s = entry.get()
    s = s.split()
    s.sort()
    label['text'] = ' '.join(s)


root = tk.Tk()
entry = tk.Entry(root, width=20)
button = tk.Button(root, text="Преобразовать")
label = tk.Label(root, bg='black', fg='white', width=20)
button.bind('<Button-1>', strToSortlist)
entry.pack()
button.pack()
label.pack()

c = tk.Canvas(root, width=200, height=200, bg='white')
c.create_line(10, 10, 190, 50)

c.create_line(
    100, 180, 50, 60, fill='green',
              width=5, arrow=tk.LAST, dash=(10, 2),
              activefill='red',
              arrowshape="10 20 10",
)

c.create_rectangle(10, 10, 190, 60)

c.create_rectangle(60, 80, 140, 190, fill='yellow', outline='green',
                   width=3, activedash=(5, 4))

c.create_oval(50, 10, 150, 110, width=2)
c.create_oval(10, 120, 190, 190, fill='grey70', outline='white')

c.pack()
root.mainloop()
