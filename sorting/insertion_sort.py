import dearpygui.dearpygui as dpg
import time

# sort logic
def insertion_sort(sender, app_data, user_data):
    x_value, y_value = user_data
    dpg.configure_item("click", show=False)

    for i in range(1, len(y_value)):
        j = i - 1
        while j >= 0 and not y_value[j] < y_value[j + 1]:
            time.sleep(0.05)

            if dpg.does_item_exist("graphs"):
                dpg.delete_item("graphs")
            if dpg.does_item_exist("completed"):
                dpg.delete_item("completed")
            if dpg.does_item_exist("highlight"):
                dpg.delete_item("highlight")

            dpg.add_bar_series(
                [x for x in x_value if x != x_value[j + 1] and x != x_value[i]],
                [y for y in y_value if y != y_value[j + 1] and y != y_value[i]],
                parent="y_axis",
                tag="graphs",
            )

            dpg.add_bar_series(
                [x_value[i]],
                [y_value[i]],
                parent="y_axis",
                tag="completed",
            )

            dpg.add_bar_series(
                [x_value[j + 1]],
                [y_value[j + 1]],
                parent="y_axis",
                tag="highlight",
            )

            dpg.bind_item_theme("graphs", "plot_theme")
            dpg.bind_item_theme("completed", "plot_theme_completed")
            dpg.bind_item_theme("highlight", "plot_theme_highlight")

            y_value[j], y_value[j + 1] = y_value[j + 1], y_value[j]
            j -= 1

    if dpg.does_item_exist("graphs"):
        dpg.delete_item("graphs")
    if dpg.does_item_exist("completed"):
        dpg.delete_item("completed")
    if dpg.does_item_exist("highlight"):
        dpg.delete_item("highlight")

    dpg.add_bar_series(
        x_value,
        y_value,
        parent="y_axis",
        tag="highlight",
    )
    dpg.bind_item_theme("highlight", "plot_theme_final")
    dpg.configure_item("click_end", show=True)
