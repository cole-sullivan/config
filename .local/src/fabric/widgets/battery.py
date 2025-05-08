from imports import *
import psutil
# from gi.repository import GLib, Gdk

# class BatteryProvider:
#     def __init__(self):
#         battery = psutil.sensors_battery()
#         if battery is None:
#             self.percent = 0.0
#             self.charging = None
#         else:
#             self.percent = battery.percent
#             self.charging = battery.power_plugged
#
#         GLib.timeout_add_seconds(1, self._update)
#
#     def _update(self):
#         battery = psutil.sensors_battery()
#         if battery is None:
#             self.percent = 0.0
#             self.charging = None
#         else:
#             self.percent = battery.percent
#             self.charging = battery.power_plugged
#         return True
#
#     def get_battery(self):
#         return (self.percent, self.charging)
#
# class Battery(Box):
#     def __init__(
#         self,
#     ):
#         self.provider = BatteryProvider()
#
#         super().__init__(
#             name="battery",
#             spacing=0,
#             visible=True,
#             all_visible=True,
#         )
#
#         self.batt_fabricator = Fabricator(
#             poll_from=lambda v: self.provider.get_battery(),
#             on_changed=lambda f, v: self.update_battery,
#             interval=1000,
#             stream=False,
#             default_value=0,
#         )
#         self.batt_fabricator.changed.connect(self.update_battery)
#         GLib.idle_add(self.update_battery, None, self.provider.get_battery())
#
#         self.percent_label = Label(label = "NULL")
#         self.children = [self.percent_label]
#
#     def _format_percentage(self, value: int) -> str:
#         return f"{value}%"
#
#     def update_battery(self, sender, battery_data):
#         value, charging = battery_data
#         if value == 0:
#             self.set_visible = False
#         self.percent_label.set_label(self._format_percentage(int(value)))

class Battery(Box):
    def __init__(
        self,
        **kwargs,
    ):
        super().__init__(
            **kwargs,
        )

        self.battery_info = Fabricator(
            poll_from=lambda f: {
                "battery": int(
                    psutil.sensors_battery().percent
                    if psutil.sensors_battery() is not None
                    else 0
                ),
                "secsleft": int(
                    psutil.sensors_battery().secsleft
                    if psutil.sensors_battery() is not None
                    else 0
                ),
                "charging": bool(
                    psutil.sensors_battery().power_plugged
                    if psutil.sensors_battery() is not None
                    else False
                ),
            },
            interval=1000,
        )

        initial_label = int(
            psutil.sensors_battery().percent
            if psutil.sensors_battery() is not None
            else 0
        )
        self.status = Label(label=f"{initial_label}%")
        self.battery = Box(children=self.status, name="battery")

        self.battery_info.connect(
            "changed",
            lambda _, value: (
                self.status.set_label(
                    f"{value['battery']}%"
                    # f"{value['battery']}% ~ {('Charging' if value['charging'] is True else str(datetime.timedelta(seconds=value['secsleft'])))}"
                ),
            ),
        )
        
        self.children = [self.battery]

