from imports import *
import psutil

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
        self.status = Label(name="battery-status", label=f"{initial_label}%")
        self.icon = Svg(name="battery-svg", size=24, svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0 0 50 50\"><path fill=\"#FFFFFF\" d=\"M 10 19 C 7.791 19 6 20.791 6 23 L 6 30 C 6 32.209 7.791 34 10 34 L 36 34 C 38.209 34 40 32.209 40 30 L 40 23 C 40 20.791 38.209 19 36 19 L 10 19 Z\"/><path fill=\"#9A9A9A\" d=\"M 9.5 17 C 6.468 17 4 19.467 4 22.5 L 4 30.5 C 4 33.533 6.468 36 9.5 36 L 36.5 36 C 39.532 36 42 33.533 42 30.5 L 42 22.5 C 42 19.467 39.532 17 36.5 17 L 9.5 17 Z M 9.5 18 L 36.5 18 C 38.981 18 41 20.019 41 22.5 L 41 30.5 C 41 32.981 38.981 35 36.5 35 L 9.5 35 C 7.019 35 5 32.981 5 30.5 L 5 22.5 C 5 20.019 7.019 18 9.5 18 Z M 43 21.5 L 43 31.5 C 44.744 30.766 46 28.816 46 26.5 C 46 24.184 44.744 22.234 43 21.5 Z\"/></svg>")
        self.battery = Box(
            name="battery",
            orientation="h",
            spacing=2,
            visible=True,
            children=[self.status, self.icon],
        )

        def update(status, value, icon):
            current = value['battery']
            status.set_label(f"{current}%")
            if value['charging']:
                status.remove_style_class("low")
                icon.set_from_string(
                    "<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0 0 50 50\"><path fill=\"#FFFFFF\" d=\"M 26.792969 13.791016 C 26.655969 13.791016 26.517156 13.847469 26.410156 13.980469 L 16.599609 26.199219 C 16.352609 26.529219 16.588 27 17 27 L 23 27 L 19.019531 37.349609 C 18.875531 37.722609 19.177141 38.033203 19.494141 38.033203 C 19.628141 38.033203 19.870094 37.850609 19.871094 37.849609 L 30.359375 24.806641 C 30.360375 24.805641 31.000844 24 29.964844 24 L 24 24 L 27.277344 14.449219 C 27.278344 14.448219 27.431969 13.791016 26.792969 13.791016 z\"/><path fill=\"#9A9A9A\" d=\"M 9.5 17 C 6.468 17 4 19.467 4 22.5 L 4 30.5 C 4 33.533 6.468 36 9.5 36 L 18.466797 36 C 18.467797 35.999 18.641625 35.549781 18.640625 35.550781 C 18.639625 35.551781 18.852563 34.999 18.851562 35 L 9.5 35 C 7.019 35 5 32.981 5 30.5 L 5 22.5 C 5 20.019 7.019 18 9.5 18 L 21.900391 18 L 22.703125 17 L 9.5 17 z M 27.478516 17 C 27.425516 17.156 27.371359 17.313703 27.318359 17.470703 C 27.258359 17.646703 27.198672 17.824 27.138672 18 L 36.5 18 C 38.981 18 41 20.019 41 22.5 L 41 30.5 C 41 32.981 38.981 35 36.5 35 L 23.480469 35 L 22.671875 36 L 36.5 36 C 39.532 36 42 33.533 42 30.5 L 42 22.5 C 42 19.467 39.532 17 36.5 17 L 27.478516 17 z\"/><path fill=\"#FFFFFF\" d=\"M 10 19 C 7.791 19 6 20.791 6 23 L 6 30 C 6 32.209 7.791 34 10 34 L 19.236328 34 L 21.544922 28 L 17 28 C 16.428 28 15.914203 27.682875 15.658203 27.171875 C 15.402203 26.659875 15.457313 26.058219 15.820312 25.574219 L 21.097656 19 L 10 19 z M 26.796875 19 L 25.410156 23 L 29.964844 23 C 30.547844 23 31.065359 23.325609 31.318359 23.849609 C 31.569359 24.370609 31.549578 24.865687 31.142578 25.429688 L 24.285156 34 L 36 34 C 38.209 34 40 32.209 40 30 L 40 23 C 40 20.791 38.209 19 36 19 L 26.796875 19 z \"/><path fill=\"#9A9A9A\" d=\"M 43 21.5 L 43 31.5 C 44.744 30.766 46 28.816 46 26.5 C 46 24.184 44.744 22.234 43 21.5 z\"/></svg>"
                )
            elif current >= 75:
                status.remove_style_class("low")
                icon.set_from_string(
                    "<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0 0 50 50\"><path fill=\"#FFFFFF\" d=\"M 10 19 C 7.791 19 6 20.791 6 23 L 6 30 C 6 32.209 7.791 34 10 34 L 36 34 C 38.209 34 40 32.209 40 30 L 40 23 C 40 20.791 38.209 19 36 19 L 10 19 Z\"/><path fill=\"#9A9A9A\" d=\"M 9.5 17 C 6.468 17 4 19.467 4 22.5 L 4 30.5 C 4 33.533 6.468 36 9.5 36 L 36.5 36 C 39.532 36 42 33.533 42 30.5 L 42 22.5 C 42 19.467 39.532 17 36.5 17 L 9.5 17 Z M 9.5 18 L 36.5 18 C 38.981 18 41 20.019 41 22.5 L 41 30.5 C 41 32.981 38.981 35 36.5 35 L 9.5 35 C 7.019 35 5 32.981 5 30.5 L 5 22.5 C 5 20.019 7.019 18 9.5 18 Z M 43 21.5 L 43 31.5 C 44.744 30.766 46 28.816 46 26.5 C 46 24.184 44.744 22.234 43 21.5 Z\"/></svg>"
                )
            elif current >= 50:
                status.remove_style_class("low")
                icon.set_from_string(
                    "<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0 0 50 50\"><path fill=\"#FFFFFF\" d=\"M 10 19 C 7.791 19 6 20.791 6 23 L 6 30 C 6 32.209 7.791 34 10 34 L 24.5 34 C 26.709 34 28.5 32.209 28.5 30 L 28.5 23 C 28.5 20.791 26.709 19 24.5 19 L 10 19 Z\"/><path fill=\"#9A9A9A\" d=\"M 9.5 17 C 6.468 17 4 19.467 4 22.5 L 4 30.5 C 4 33.533 6.468 36 9.5 36 L 36.5 36 C 39.532 36 42 33.533 42 30.5 L 42 22.5 C 42 19.467 39.532 17 36.5 17 L 9.5 17 Z M 9.5 18 L 36.5 18 C 38.981 18 41 20.019 41 22.5 L 41 30.5 C 41 32.981 38.981 35 36.5 35 L 9.5 35 C 7.019 35 5 32.981 5 30.5 L 5 22.5 C 5 20.019 7.019 18 9.5 18 Z M 43 21.5 L 43 31.5 C 44.744 30.766 46 28.816 46 26.5 C 46 24.184 44.744 22.234 43 21.5 Z\"/></svg>"
                )
            elif current >= 25:
                status.remove_style_class("low")
                icon.set_from_string(
                    "<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0 0 50 50\"><path fill=\"#FFFFFF\" d=\"M 10 19 C 7.791 19 6 20.791 6 23 L 6 30 C 6 32.209 7.791 34 10 34 L 19.5 34 C 21.709 34 23.5 32.209 23.5 30 L 23.5 23 C 23.5 20.791 21.709 19 19.5 19 L 10 19 Z\"/><path fill=\"#9A9A9A\" d=\"M 9.5 17 C 6.468 17 4 19.467 4 22.5 L 4 30.5 C 4 33.533 6.468 36 9.5 36 L 36.5 36 C 39.532 36 42 33.533 42 30.5 L 42 22.5 C 42 19.467 39.532 17 36.5 17 L 9.5 17 Z M 9.5 18 L 36.5 18 C 38.981 18 41 20.019 41 22.5 L 41 30.5 C 41 32.981 38.981 35 36.5 35 L 9.5 35 C 7.019 35 5 32.981 5 30.5 L 5 22.5 C 5 20.019 7.019 18 9.5 18 Z M 43 21.5 L 43 31.5 C 44.744 30.766 46 28.816 46 26.5 C 46 24.184 44.744 22.234 43 21.5 Z\"/></svg>"
                )
            elif current <= 10:
                status.add_style_class("low")
                icon.set_from_string(
                    "<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0 0 50 50\"><path fill=\"#EB4C3D\" d=\"M 10 19 C 7.791 19 6 20.791 6 23 L 6 30 C 6 32.209 7.791 34 10 34 L 12.5 34 C 14.709 34 16.5 32.209 16.5 30 L 16.5 23 C 16.5 20.791 14.709 19 12.5 19 L 10 19 Z\"/><path fill=\"#9A9A9A\" d=\"M 9.5 17 C 6.468 17 4 19.467 4 22.5 L 4 30.5 C 4 33.533 6.468 36 9.5 36 L 36.5 36 C 39.532 36 42 33.533 42 30.5 L 42 22.5 C 42 19.467 39.532 17 36.5 17 L 9.5 17 Z M 9.5 18 L 36.5 18 C 38.981 18 41 20.019 41 22.5 L 41 30.5 C 41 32.981 38.981 35 36.5 35 L 9.5 35 C 7.019 35 5 32.981 5 30.5 L 5 22.5 C 5 20.019 7.019 18 9.5 18 Z M 43 21.5 L 43 31.5 C 44.744 30.766 46 28.816 46 26.5 C 46 24.184 44.744 22.234 43 21.5 Z\"/></svg>"
                )
            else:
                status.remove_style_class("low")
                icon.set_from_string(
                    "<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0 0 50 50\"><path fill=\"#FFFFFF\" d=\"M 10 19 C 7.791 19 6 20.791 6 23 L 6 30 C 6 32.209 7.791 34 10 34 L 12.5 34 C 14.709 34 16.5 32.209 16.5 30 L 16.5 23 C 16.5 20.791 14.709 19 12.5 19 L 10 19 Z\"/><path fill=\"#9A9A9A\" d=\"M 9.5 17 C 6.468 17 4 19.467 4 22.5 L 4 30.5 C 4 33.533 6.468 36 9.5 36 L 36.5 36 C 39.532 36 42 33.533 42 30.5 L 42 22.5 C 42 19.467 39.532 17 36.5 17 L 9.5 17 Z M 9.5 18 L 36.5 18 C 38.981 18 41 20.019 41 22.5 L 41 30.5 C 41 32.981 38.981 35 36.5 35 L 9.5 35 C 7.019 35 5 32.981 5 30.5 L 5 22.5 C 5 20.019 7.019 18 9.5 18 Z M 43 21.5 L 43 31.5 C 44.744 30.766 46 28.816 46 26.5 C 46 24.184 44.744 22.234 43 21.5 Z\"/></svg>"
                )

        self.battery_info.connect(
            "changed",
            lambda _, value: (
                update(self.status, value, self.icon)
                # self.status.set_label(
                    # f"{value['battery']}%"
                    # f"{value['battery']}% ~ {('Charging' if value['charging'] is True else str(datetime.timedelta(seconds=value['secsleft'])))}"
                # ),
            ),
        )
        
        self.children = [self.battery]

