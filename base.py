import dearpygui.dearpygui as dpg
import random
import sorting


def sort():
    if dpg.does_item_exist("sort_window"):
        dpg.delete_item("sort_window")

    sort_size = dpg.get_value("sort_size")

    with dpg.window(
        label=dpg.get_value("sort_choice"),
        tag="sort_window",
        width=dpg.get_viewport_client_width(),
        height=dpg.get_viewport_client_height(),
        no_collapse=True,
        no_close=True,
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
            dpg.add_bar_series(x_value, y_value, parent="y_axis", tag="graphs")
            # apply theme
            dpg.bind_item_theme("graphs", "plot_theme")

            def end():
                dpg.delete_item("sort_window")
                dpg.delete_item("click")
                dpg.delete_item("click_end")

            # mouse/keyboard input to start the visualization
            with dpg.handler_registry(tag="click"):
                callback = getattr(sorting, str(dpg.get_value("sort_choice")))
                dpg.add_key_down_handler(
                    callback=callback, user_data=[x_value, y_value]
                )
            dpg.configure_item("click", show=True)

            # mouse/keyboard input to end the visualization
            with dpg.handler_registry(tag="click_end"):
                dpg.add_mouse_down_handler(callback=end)
                dpg.add_key_down_handler(callback=end)
            dpg.configure_item("click_end", show=False)
