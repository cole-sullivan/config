import psutil
from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.overlay import Overlay
from fabric.widgets.eventbox import EventBox
from fabric.widgets.datetime import DateTime
from fabric.widgets.centerbox import CenterBox
from fabric.system_tray.widgets import SystemTray
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.hyprland.widgets import ActiveWindow, Workspaces, WorkspaceButton
from fabric.utils import (
    FormattedString,
    bulk_replace,
    invoke_repeater,
    get_relative_path,
)

class StatusBar(Window):
    def __init__(
        self,
    ):
        super().__init__(
            name="bar",
            layer="top",
            anchor="left top right",
            # margin="10px 10px -2px 10px",
            exclusivity="auto",
            visible=True,
            all_visible=True,
        )

        self.workspaces = Workspaces(
            name="workspaces",
            spacing=4,
            buttons_factory=lambda ws_id: WorkspaceButton(id=ws_id, label=None),
        )
        self.active_window = ActiveWindow(name="hyprland-window")
        self.date_time = DateTime(name="date-time")

        self.children = CenterBox(
            name="bar-inner",
            start_children=Box(
                spacing=4,
                orientation="h",
                children=[
                    self.workspaces,
                    self.active_window,
                ],
            ),
            center_children=Box(
                spacing=4,
                orientation="h",
                children=[
                ],
            ),
            end_children=Box(
                spacing=4,
                orientation="h",
                children=[
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
