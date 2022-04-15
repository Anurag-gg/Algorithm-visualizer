import dearpygui.dearpygui as dpg

SORTING_ALGOS = ("Bubble Sort","Selection Sort","Merge Sort")
MAX_WIDTH = 600
MAX_HEIGHT = 400

def size_callback(sender):
    dpg.set_value("sort_size" , dpg.get_value(sender))

def choice_callback(sender):
    dpg.set_value("sort_choice" , dpg.get_value(sender))

def button_callback():
    sort_size  = dpg.get_value("sort_size")
    sort_choice = dpg.get_value("sort_choice")
    with dpg.window(label=sort_choice,width=MAX_WIDTH , height=MAX_HEIGHT):
        dpg.add_text("Select the sorting algorithm")
    

dpg.create_context()
dpg.create_viewport(title='Sorting Visualizer', width=MAX_WIDTH, height=MAX_HEIGHT)

with dpg.window(label="Options" ,width=MAX_WIDTH , height=MAX_HEIGHT):
    dpg.add_text("Select the sorting algorithm")
    dpg.add_combo(items=SORTING_ALGOS , default_value="Bubble Sort" , tag = "sort_choice", callback=choice_callback)
    dpg.add_text("Drag to choose the number of elements")
    dpg.add_slider_int(default_value=10000, max_value=25000 ,tag="sort_size" , callback=size_callback)
    dpg.add_text("")
    dpg.add_button(label="START" ,callback=button_callback,width = MAX_WIDTH,height=40,)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
