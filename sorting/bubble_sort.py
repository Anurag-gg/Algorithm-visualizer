import dearpygui.dearpygui as dpg
import random
import time

def bubble_sort(sort_size):
    if dpg.does_item_exist("sort_window"):
        dpg.delete_item("sort_window")
    with dpg.window(
        label="Bubble Sort",
        tag="sort_window",
        width=dpg.get_viewport_client_width(),
        height=dpg.get_viewport_client_height(),
    ):
        inputs = random.sample(range(1, sort_size + 1), sort_size)

        with dpg.plot(height=-1, width=-1):
            # create x axis
            dpg.add_plot_axis(
                dpg.mvXAxis, no_gridlines=True, tag="x_axis", no_tick_labels=True
            )
            # create y axis
            dpg.add_plot_axis(
                dpg.mvYAxis, no_gridlines=True, tag="y_axis", no_tick_labels=True
            )
            # add series to y axis
            graphs = dpg.add_bar_series(
                [x for x in range(1, sort_size + 1)],
                inputs,
                parent="y_axis"
            )
            #apply theme
            dpg.bind_item_theme(graphs, "plot_theme")

            for i in range(sort_size - 1):
                for j in range(sort_size - 1 - i):
                    if inputs[j] > inputs[j + 1]:
                        inputs[j], inputs[j + 1] = inputs[j + 1], inputs[j]
                    time.sleep(0.01)
                    dpg.delete_item(graphs)
                    graphs = dpg.add_bar_series(
                        [x for x in range(1, sort_size + 1)], inputs, parent="y_axis"
                    )
                    dpg.bind_item_theme(graphs, "plot_theme")

            dpg.bind_item_theme(graphs, "plot_theme_final")
            graphs = dpg.add_bar_series(
                        [x for x in range(1, sort_size + 1)], inputs, parent="y_axis"
                    )