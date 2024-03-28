from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort
from insertionsort import insertion_sort
from selectionsort import selection_sort
from heapsort import heap_sort

# Main window and its attributes
root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(700,600)
root.minsize(700,600)
root.config(bg='#2F4F4F')
root.iconbitmap('icon.ico')



# variables
current_algorithm = StringVar()
data = []


def popupmsg(msg, window_title="Information"):
    popup = Tk()
    popup.geometry('300x100')
    popup.iconbitmap('icon.ico')
    popup.config(bg='#2F4F4F')
    popup.wm_title(window_title)
    label = Label(popup, text=msg, font=("Comic Sans MS", 10),bg='#2F4F4F',fg='white')
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="OK", command=popup.destroy, bg='grey', width=10)
    B1.pack()
    popup.mainloop()

def drawData(data, colorlist):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 20
    spacing = 10
    normalized_data = [i / max(data) for i in data]
    for i, height in enumerate(normalized_data):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        # Fill the bar with a gradient color
        gradient_color = '#FF5733'  # Example gradient color
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorlist[i], outline=gradient_color)
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), fill="orange")
    root.update_idletasks()

def Generate():
    try:
        global data
        print('Selected Algorithm: ' + current_algorithm.get())
        minVal = int(min_value.get())
        maxVal = int(max_value.get())
        size = int(size_value.get())
        data = []
        for _ in range(size):
            data.append(random.randrange(minVal, maxVal+1))
        drawData(data, ['#B22222' for x in range(len(data))])
    except ValueError:
        popupmsg(f'Min Value must be less than or equal Max Value',window_title="Error")

def StartAlgorithm():
    global data
    if not data:
        return
    if algorithm_menu.get() == "Quick Sort":
        elapsed_time_fl=quick_sort(data,0, len(data)-1,drawData,speed_rate.get())
        drawData(data,['green' for x in range(len(data))])
        popupmsg(f'Selected Algorithm: {current_algorithm.get()}\n\nExecution Time: {elapsed_time_fl}')
    elif algorithm_menu.get() == "Bubble Sort":
        elapsed_time_fl = bubble_sort(data,drawData,speed_rate.get())
        popupmsg(f'Selected Algorithm: {current_algorithm.get()}\n\nExecution Time: {elapsed_time_fl}')
    elif algorithm_menu.get() == "Merge Sort":
        elapsed_time_fl=merge_sort(data,drawData,speed_rate.get())
        popupmsg(f'Selected Algorithm: {current_algorithm.get()}\n\nExecution Time: {elapsed_time_fl}')
    elif algorithm_menu.get() == "Insertion Sort":
        elapsed_time_fl = insertion_sort(data, drawData, speed_rate.get())
        popupmsg(f'Selected Algorithm: {current_algorithm.get()}\n\nExecution Time: {elapsed_time_fl}')
    elif algorithm_menu.get() == "Selection Sort":
        elapsed_time_fl = selection_sort(data, drawData, speed_rate.get())
        popupmsg(f'Selected Algorithm: {current_algorithm.get()}\n\nExecution Time: {elapsed_time_fl}')
    elif algorithm_menu.get() == "Heap Sort":
        elapsed_time_fl = heap_sort(data, drawData, speed_rate.get())
        popupmsg(f'Selected Algorithm: {current_algorithm.get()}\n\nExecution Time: {elapsed_time_fl}')






# frame / base layout
UI_frame = Frame(root, width= 600, height=200,bg="#2F4F4F")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='black',highlightbackground="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

# labels , buttons , speed rate
# Row[0]

Label(UI_frame, text="Algorithm: ", bg='#8FBC8F').grid(row=0, column=0, padx=5, pady=5, sticky=W,)
algorithm_menu = ttk.Combobox(UI_frame,state="readonly", textvariable=current_algorithm, values=['Bubble Sort', 'Quick Sort', 'Merge Sort','Insertion Sort',"Selection Sort","Heap Sort"])
algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
algorithm_menu.current(0)
Label(UI_frame, text="Delay (seconds)", bg='#8FBC8F').grid(row=0, column=2, padx=5, pady=5, sticky=W)
speed_rate = Scale(UI_frame, from_=0.1, to=5.0, resolution=0.2, length=100, digits=2 ,orient=HORIZONTAL, font=("Comic Sans MS", 14, "italic bold"),
                   relief=GROOVE, bd=2, width=10)
speed_rate.grid(row=0, column=3, padx=5, pady=5, sticky=W)
Button(UI_frame, text="Generate Numbers", command=Generate, bg='#B22222', fg='white', font=("Comic Sans MS", 8, "bold"),
       activebackground="#DC143C").grid(row=0, column=4, padx=5, pady=5)
Button(UI_frame, text="Start Sorting", command=StartAlgorithm, bg='green', fg='white', font=("Comic Sans MS", 8, "bold"),
       activebackground="#05945B").grid(row=0, column=5, padx=5, pady=5)
# Row[1]
Label(UI_frame, text="Size ", bg='#8FBC8F').grid(row=1, column=0, padx=5, pady=5, sticky=W)
size_value = Scale(UI_frame, from_=1, to=30, resolution=1, orient=HORIZONTAL, font=("Comic Sans MS", 14, "italic bold"),
                   relief=GROOVE, bd=2, width=10)
size_value.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Min Value ", bg='#8FBC8F').grid(row=1, column=2, padx=5, pady=5, sticky=W)
min_value = Scale(UI_frame, from_=1, to=10, resolution=1, orient=HORIZONTAL, font=("Comic Sans MS", 14, "italic bold"),
                   relief=GROOVE, bd=2, width=10)
min_value.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Max Value ", bg='#8FBC8F').grid(row=1, column=4, padx=5, pady=5, sticky=W)
max_value = Scale(UI_frame, from_=1, to=100, resolution=1, orient=HORIZONTAL, font=("Comic Sans MS", 14, "italic bold"),
                   relief=GROOVE, bd=2, width=10)
max_value.grid(row=1, column=5, padx=5, pady=5, sticky=W)


# styling
size_value.config(bg='#D3D3D3', troughcolor='#A9A9A9', sliderrelief='raised')
min_value.config(bg='#D3D3D3', troughcolor='#A9A9A9', sliderrelief='raised')
max_value.config(bg='#D3D3D3', troughcolor='#A9A9A9', sliderrelief='raised')
speed_rate.config(bg='#D3D3D3', troughcolor='#A9A9A9', sliderrelief='raised')

root.mainloop()

