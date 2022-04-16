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
        y_value = random.sample(range(1, sort_size + 1), sort_size)
        x_value = [x for x in range(1, sort_size + 1)]

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
            dpg.add_bar_series(
                x_value,
                y_value,
                parent="y_axis",
                tag="graphs"
            )
            #apply theme
            dpg.bind_item_theme("graphs", "plot_theme")

            #ending the visual
            def end():
                dpg.delete_item("sort_window")
                dpg.delete_item("click_end")

            #sort logic
            def sort():
                dpg.delete_item("click")
                for i in range(sort_size - 1):
                    for j in range(sort_size - 1 - i):
                        if y_value[j] > y_value[j + 1]:
                            y_value[j], y_value[j + 1] = y_value[j + 1], y_value[j]
                        time.sleep(0.01)
                        dpg.delete_item("graphs")
                        dpg.add_bar_series(
                            x_value, y_value, parent="y_axis",tag="graphs"
                        )
                        dpg.bind_item_theme("graphs", "plot_theme")
                dpg.bind_item_theme("graphs", "plot_theme_final")

                #mouse/keyboard input to end the visualization
                with dpg.handler_registry(tag="click_end"):
                    dpg.add_mouse_down_handler(callback=end)
                    dpg.add_key_down_handler(callback=end)

            #mouse/keyboard input to start the visualization
            with dpg.handler_registry(tag="click"):
                dpg.add_mouse_down_handler(callback=sort)
                dpg.add_key_down_handler(callback=sort)