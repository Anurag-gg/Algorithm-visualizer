import dearpygui.dearpygui as dpg
import sorting

SORTING_ALGOS = ("Bubble Sort", "Selection Sort", "Merge Sort")
MAX_WIDTH = 800
MAX_HEIGHT = 600


def size_callback(sender):
    dpg.set_value("sort_size", dpg.get_value(sender))


def choice_callback(sender):
    dpg.set_value("sort_choice", dpg.get_value(sender))


def button_callback():
    sort_size = dpg.get_value("sort_size")
    sort_choice = dpg.get_value("sort_choice")
    #dpg.delete_item("Options")
    sorting.bubble_sort(sort_size)


dpg.create_context()
dpg.create_viewport(title="Sorting Visualizer", width=MAX_WIDTH, height=MAX_HEIGHT)

with dpg.window(label="Options", tag="Options", width=MAX_WIDTH, height=MAX_HEIGHT):
    dpg.add_text("Select the sorting algorithm")
    dpg.add_combo(
        items=SORTING_ALGOS,
        default_value="Bubble Sort",
        tag="sort_choice",
        callback=choice_callback,
    )
    dpg.add_text("Drag to choose the number of elements")
    dpg.add_slider_int(
        default_value=50, max_value=100, tag="sort_size", callback=size_callback
    )
    dpg.add_text("")
    dpg.add_button(
        label="START",
        callback=button_callback,
        width=MAX_WIDTH,
        height=40,
    )

    #initial theme for graphs
    with dpg.theme(tag="plot_theme"):
        with dpg.theme_component(dpg.mvBarSeries):
            dpg.add_theme_color(dpg.mvPlotCol_Fill, (150, 255, 0), category=dpg.mvThemeCat_Plots)
    
    #final theme for graphs
    with dpg.theme(tag="plot_theme_final"):
        with dpg.theme_component(dpg.mvBarSeries):
            dpg.add_theme_color(dpg.mvPlotCol_Fill, (7,83,138), category=dpg.mvThemeCat_Plots)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
