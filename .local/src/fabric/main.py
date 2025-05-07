import psutil
from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.overlay import Overlay
from fabric.widgets.eventbox import EventBox
from fabric.widgets.datetime import DateTime
from fabric.widgets.centerbox import CenterBox
from fabric.core.fabricator import Fabricator
from fabric.system_tray.widgets import SystemTray
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.hyprland.widgets import ActiveWindow, Workspaces, WorkspaceButton
from fabric.utils import (
    FormattedString,
    bulk_replace,
    invoke_repeater,
    get_relative_path,
)
from gi.repository import GLib, Gdk

class BatteryProvider:
    def __init__(self):
        battery = psutil.sensors_battery()
        if battery is None:
            self.percent = 0.0
            self.charging = None
        else:
            self.percent = battery.percent
            self.charging = battery.power_plugged
        
        GLib.timeout_add_seconds(1, self._update)

    def _update(self):
        battery = psutil.sensors_battery()
        if battery is None:
            self.percent = 0.0
            self.charging = None
        else:
            self.percent = battery.percent
            self.charging = battery.power_plugged
        return True

    def get_battery(self):
        return (self.percent, self.charging)

class Battery(Box):
    def __init__(
        self,
    ):
        self.provider = BatteryProvider()

        super().__init__(
            name="battery",
            spacing=0,
            visible=True,
            all_visible=True,
        )

        self.batt_fabricator = Fabricator(
            poll_from=lambda v: self.provider.get_battery(),
            on_changed=lambda f, v: self.update_battery,
            interval=1000,
            stream=False,
            default_value=0,
        )
        self.batt_fabricator.changed.connect(self.update_battery)
        GLib.idle_add(self.update_battery, None, self.provider.get_battery())

        self.percent_label = Label(label = "NULL")
        self.children = [self.percent_label]

    def _format_percentage(self, value: int) -> str:
        return f"{value}%"

    def update_battery(self, sender, battery_data):
        value, charging = battery_data
        if value == 0:
            self.set_visible = False
        self.percent_label.set_label(self._format_percentage(int(value)))

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
            buttons_factory=lambda ws_id: WorkspaceButton(id=ws_id, label=None),
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
