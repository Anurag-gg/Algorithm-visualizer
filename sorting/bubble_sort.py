import dearpygui.dearpygui as dpg
import time

# sort logic
def bubble_sort(sender, app_data, user_data):
    x_value, y_value = user_data
    dpg.configure_item("click", show=False)

    for i in range(len(y_value) - 1):
        for j in range(len(y_value) - 1 - i):
            if y_value[j] > y_value[j + 1]:
                y_value[j], y_value[j + 1] = y_value[j + 1], y_value[j]
            time.sleep(0.05)

            if dpg.does_item_exist("graphs"):
                dpg.delete_item("graphs")
            if dpg.does_item_exist("highlight"):
                dpg.delete_item("highlight")

            dpg.add_bar_series(
                [x for x in x_value if x not in (x_value[j], x_value[j + 1])],
                [y for y in y_value if y not in (y_value[j], y_value[j + 1])],
                parent="y_axis",
                tag="graphs",
            )
            dpg.add_bar_series(
                [x_value[j], x_value[j + 1]],
                [y_value[j], y_value[j + 1]],
                parent="y_axis",
                tag="highlight",
            )

            dpg.bind_item_theme("graphs", "plot_theme")
            dpg.bind_item_theme("highlight", "plot_theme_highlight")

    dpg.bind_item_theme("graphs", "plot_theme_final")
    dpg.bind_item_theme("highlight", "plot_theme_final")

    dpg.configure_item("click_end", show=True)
