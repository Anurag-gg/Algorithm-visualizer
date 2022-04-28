import dearpygui.dearpygui as dpg
import time

# sort logic
def selection_sort(sender, app_data, user_data):
    completed_y, completed_x = [], []
    x_value, y_value = user_data
    dpg.configure_item("click", show=False)

    for i in range(len(y_value) - 1, 0, -1):
        idx = i
        temp = idx
        for j in range(i - 1, -1, -1):
            if y_value[idx] < y_value[j]:
                idx = j
            time.sleep(0.05)

            if dpg.does_item_exist("graphs"):
                dpg.delete_item("graphs")
            if dpg.does_item_exist("completed"):
                dpg.delete_item("completed")
            if dpg.does_item_exist("highlight"):
                dpg.delete_item("highlight")

            dpg.add_bar_series(
                [
                    x
                    for x in x_value
                    if x not in (x_value[temp], x_value[j]) and x not in completed_x
                ],
                [
                    y
                    for y in y_value
                    if y not in (y_value[temp], y_value[j]) and y not in completed_y
                ],
                parent="y_axis",
                tag="graphs",
            )

            if completed_x:
                dpg.add_bar_series(
                    completed_x,
                    completed_y,
                    parent="y_axis",
                    tag="completed",
                )

            dpg.add_bar_series(
                [x_value[temp], x_value[j]],
                [y_value[temp], y_value[j]],
                parent="y_axis",
                tag="highlight",
            )

            dpg.bind_item_theme("graphs", "plot_theme")
            if completed_x:
                dpg.bind_item_theme("completed", "plot_theme_completed")
            dpg.bind_item_theme("highlight", "plot_theme_highlight")

            temp = idx

        y_value[i], y_value[idx] = y_value[idx], y_value[i]
        completed_x.append(x_value[i])
        completed_y.append(y_value[i])

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
