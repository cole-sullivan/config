from imports import *
from widgets.battery import Battery

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

        self.active_window = ActiveWindow(name="hyprland-window")

        self.workspaces = Workspaces(
            name="workspaces",
            spacing=4,
            buttons_factory=lambda ws_id: WorkspaceButton(id=ws_id, label=f"{ws_id}"),
        )

        self.battery = Battery()
        self.date_time = DateTime(formatters="%a, %b %-d  %-I:%M %p", name="date-time")

        self.children = CenterBox(
            name="bar-inner",
            start_children=Box(
                spacing=4,
                orientation="h",
                children=[
                    self.active_window,
                ],
            ),
            center_children=Box(
                spacing=4,
                orientation="h",
                children=[
                    self.workspaces,
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


if __name__ == "__main__":
    bar = StatusBar()
    app = Application("bar", bar)
    app.set_stylesheet_from_file(get_relative_path("./style.css"))

    app.run()
