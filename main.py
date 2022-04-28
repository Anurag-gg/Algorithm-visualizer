import dearpygui.dearpygui as dpg
import base
import os

SORTING_ALGOS = [
    os.path.splitext(filename)[0]
    for filename in os.listdir("sorting")
    if not filename.startswith("__")
]
MAX_WIDTH = 800
MAX_HEIGHT = 600


def size_callback(sender):
    dpg.set_value("sort_size", dpg.get_value(sender))


def choice_callback(sender):
    dpg.set_value("sort_choice", dpg.get_value(sender))


def button_callback():
    # dpg.delete_item("Options")
    base.sort()


dpg.create_context()
dpg.configure_app(auto_device=True)
dpg.create_viewport(
    title="Sorting Visualizer", width=MAX_WIDTH, height=MAX_HEIGHT, resizable=False
)

with dpg.window(
    label="Options",
    tag="Options",
    width=MAX_WIDTH,
    height=MAX_HEIGHT,
    no_close=True,
    no_collapse=True,
):
    dpg.add_text("Select the sorting algorithm")
    dpg.add_combo(
        items=SORTING_ALGOS,
        default_value="bubble_sort",
        tag="sort_choice",
        callback=choice_callback,
    )
    dpg.add_text("Drag to choose the number of elements")
    dpg.add_slider_int(
        default_value=50,
        min_value=2,
        max_value=100,
        tag="sort_size",
        callback=size_callback,
    )
    dpg.add_text("")
    dpg.add_button(
        label="START",
        callback=button_callback,
        width=MAX_WIDTH,
        height=40,
    )

    # initial theme for graphs
    with dpg.theme(tag="plot_theme"):
        with dpg.theme_component(dpg.mvBarSeries):
            dpg.add_theme_color(
                dpg.mvPlotCol_Fill, (150, 255, 0), category=dpg.mvThemeCat_Plots
            )

    # highlight theme for graphs
    with dpg.theme(tag="plot_theme_highlight"):
        with dpg.theme_component(dpg.mvBarSeries):
            dpg.add_theme_color(
                dpg.mvPlotCol_Fill, (255, 102, 0), category=dpg.mvThemeCat_Plots
            )

    # completed theme for graphs
    with dpg.theme(tag="plot_theme_completed"):
        with dpg.theme_component(dpg.mvBarSeries):
            dpg.add_theme_color(
                dpg.mvPlotCol_Fill, (102, 153, 0), category=dpg.mvThemeCat_Plots
            )

    # final theme for graphs
    with dpg.theme(tag="plot_theme_final"):
        with dpg.theme_component(dpg.mvBarSeries):
            dpg.add_theme_color(
                dpg.mvPlotCol_Fill, (7, 83, 138), category=dpg.mvThemeCat_Plots
            )

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
