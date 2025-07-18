from imports import *
from widgets.battery import Battery
from widgets.power import PowerMenu

class StatusBar(WaylandWindow):
    def __init__(
        self,
        monitor=None,
    ):
        super().__init__(
            name="bar",
            layer="top",
            anchor="left top right",
            monitor=monitor,
            exclusivity="auto",
            visible=True,
            all_visible=True,
        )

        self.power_menu = PowerMenu()
        self.power_button_svg = Svg(name="power-button-svg", svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0,0,256,256\"><g fill=\"#ffffff\" fill-rule=\"nonzero\" stroke=\"none\" stroke-width=\"1\" stroke-linecap=\"butt\" stroke-linejoin=\"miter\" stroke-miterlimit=\"10\" stroke-dasharray=\"\" stroke-dashoffset=\"0\" font-family=\"none\" font-weight=\"none\" font-size=\"none\" text-anchor=\"none\" style=\"mix-blend-mode: normal\"><g transform=\"scale(10.66667,10.66667)\"><path d=\"M14.3,19.414c0.216,-0.569 0.342,-1.218 0.342,-1.913c0,-2.129 -1.139,-3.86 -2.539,-3.86c-1.412,0 -2.55,1.731 -2.55,3.86c0,0.683 0.114,1.332 0.33,1.89c-4.657,0.49 -7.936,2.437 -9.268,3.313c2.243,-3.234 4.589,-7.025 6.831,-11.386c0.558,-1.082 1.082,-2.152 1.571,-3.199c0.193,0.125 0.387,0.262 0.603,0.399c1.002,0.626 1.936,0.968 2.619,1.15c-0.501,-0.376 -1.047,-0.831 -1.605,-1.389c-0.421,-0.421 -0.797,-0.843 -1.116,-1.253c0.945,-2.072 1.765,-4.065 2.482,-5.955c1.195,3.165 2.687,6.615 4.554,10.247c1.207,2.334 2.437,4.509 3.666,6.513c-0.353,-0.193 -0.74,-0.376 -1.15,-0.535c-0.706,-0.273 -1.366,-0.444 -1.936,-0.546c0.774,0.387 1.674,0.9 2.619,1.583c0.615,0.456 1.161,0.911 1.628,1.355c0.011,0.011 0.011,0.011 0.023,0.023c0.649,1.059 1.321,2.038 1.981,2.994c-1.309,-0.866 -4.531,-2.779 -9.085,-3.291z\"></path></g></g></svg>")
        self.power_button = Button(
            name="power-button",
            child=self.power_button_svg,
            size=22,
            on_clicked=lambda *_: self.power_menu.toggle(),
        )
        self.power_menu.parent_button = self.power_button
        self.active_window = ActiveWindow(
            name="hyprland-window",
            formatter=FormattedString(
                f"{{'Desktop' if not win_title or win_title == 'unknown' else truncate(win_title, 64)}}",
                truncate=truncate,
            ),
        )

        self.workspaces = Workspaces(
            name="workspaces",
            spacing=4,
            buttons_factory=lambda ws_id: WorkspaceButton(id=ws_id, label=f"{ws_id}"),
        )

        self.battery = Battery()
        self.date_time = DateTime(formatters="%a, %b %-d  %-I:%M %p", name="date-time")

        self.box = CenterBox(
            name="bar-inner",
            start_children=Box(
                name="box-start",
                spacing=4,
                orientation="h",
                children=[
                    self.power_button,
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
                name="box-end",
                spacing=4,
                orientation="h",
                children=[
                    self.battery,
                    self.date_time,
                ],
            ),
        )

        self.children = self.box
        # self.show_all()

        self._is_open = False
        self.set_visible(False)

    def show(self):
        self._is_open = True
        self.set_visible(True)

    def hide(self):
        self._is_open = False
        self.set_visible(False)
