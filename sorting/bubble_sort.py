import dearpygui.dearpygui as dpg
import time


#ending the visual
def end():
    dpg.delete_item("sort_window")
    dpg.delete_item("click_end")

#sort logic
def bubble_sort(sender , app_data , user_data):
    x_value , y_value = user_data
    dpg.delete_item("click")
    for i in range(len(y_value) - 1):
        for j in range(len(y_value) - 1 - i):
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
