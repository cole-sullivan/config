from imports import *
from fabric.core.service import Service, Signal, Property
from widgets.bar import StatusBar
import json
import subprocess
import os
from gi.repository import GObject

class MonitorService(Service):
    def __init__(self):
        super().__init__()
        self._monitor_ids = get_monitors()
        socket_path = f"{os.environ['XDG_RUNTIME_DIR']}/hypr/{os.environ['HYPRLAND_INSTANCE_SIGNATURE']}/.socket2.sock"
        self.event_fabricator = Fabricator(
            stream=True,
            poll_from=f"socat -U - UNIX-CONNECT:{socket_path}",
            on_changed=self._handle_event
        )

    @Signal
    def monitors_changed(self, monitor_ids: GObject.TYPE_PYOBJECT) -> None:
        pass

    @Property(GObject.TYPE_PYOBJECT, flags="read-write")
    def monitor_ids(self) -> list:
        return self._monitor_ids

    @monitor_ids.setter
    def monitor_ids(self, value: list):
        self._monitor_ids = value
        self.monitors_changed(value)

    def _handle_event(self, fabricator, event: str):
        event = event.strip()
        if event.startswith("monitoradded>>") or event.startswith("monitorremoved>>"):
            new_monitor_ids = get_monitors()
            if new_monitor_ids != self._monitor_ids:
                self.monitor_ids = new_monitor_ids

def get_monitors():
    result = subprocess.run(['hyprctl', 'monitors', '-j'], capture_output=True, text=True, check=True)
    monitors = json.loads(result.stdout)
    return [monitor['id'] for monitor in monitors]

if __name__ == "__main__":
    app = Application("bar")
    monitor_service = MonitorService()

    status_bars = {}

    def update_status_bars(monitor_ids: list):
        for mid in list(status_bars.keys()):
            app.remove_window(status_bars[mid])
            status_bars[mid].destroy()
            del status_bars[mid]

        for mid in monitor_ids:
            if mid not in status_bars:
                status_bars[mid] = StatusBar(mid)
                app.add_window(status_bars[mid])

    monitor_service.connect("monitors_changed", lambda _, ids: update_status_bars(ids))
    update_status_bars(monitor_service.monitor_ids)

    app.set_stylesheet_from_file(get_relative_path("./style.css"))

    app.run()
