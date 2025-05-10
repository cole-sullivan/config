from imports import *
from .battery import Battery
from .power import Power

class StatusBar(Window):
    def __init__(
        self,
    ):
        super().__init__(
            name="bar",
            layer="top",
            anchor="left top right",
            exclusivity="auto",
            visible=True,
            all_visible=True,
        )

        self.power_button = Button(label="Open power menu", on_clicked=lambda *_:self.island.open("power"))
        self.active_window = ActiveWindow(name="hyprland-window")

        self.battery = Battery()
        self.date_time = DateTime(formatters="%a, %b %-d  %-I:%M %p", name="date-time")

        self.children = CenterBox(
            name="bar-inner",
            start_children=Box(
                spacing=4,
                orientation="h",
                children=[
                    self.power_button,
                    self.active_window,
                ],
            ),
            end_children=Box(
                spacing=4,
                orientation="h",
                children=[
                    self.battery,
                    self.date_time,
                ],
            ),
        )

        self.show_all()

