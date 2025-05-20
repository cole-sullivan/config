from imports import *

class PowerMenu(Window):
    def __init__(self, **kwargs):
        super().__init__(
            title="fabric-menu",
            name="power",
            layer="top",
            anchor="center",
            margin="-320px 0px 0px 0px", 
            keyboard_mode="none",
            exclusivity="none",
            visible=False,
            # all_visible=False,
        )

        self.box = Box(
            name="power-menu",
            orientation="h",
            spacing=4,
            h_align="center",
            v_align="center",
            visible=True,
            **kwargs,
        )

        self.parent_button = kwargs.get("parent_button", None)
        self._is_open = False

        self.lock_button_svg = Svg(name="power-menu-button-svg", svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 0 24 24\" width=\"24px\" fill=\"#FFFFFF\"><g fill=\"none\"><path d=\"M0 0h24v24H0V0z\"/><path d=\"M0 0h24v24H0V0z\" opacity=\".87\"/></g><path d=\"M20 8h-3V6.21c0-2.61-1.91-4.94-4.51-5.19C9.51.74 7 3.08 7 6v2H4v14h16V8zm-8 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zM9 8V6c0-1.66 1.34-3 3-3s3 1.34 3 3v2H9z\"/></svg>")
        self.lock_button = Button(
            name="power-menu-button",
            child=self.lock_button_svg,
            size=22,
            on_clicked=self.lock,
        )

        self.sleep_button_svg = Svg(name="power-menu-button-svg", svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 0 24 24\" width=\"24px\" fill=\"#FFFFFF\"><path d=\"M0 0h24v24H0V0z\" fill=\"none\"/><path d=\"M7 13c1.66 0 3-1.34 3-3S8.66 7 7 7s-3 1.34-3 3 1.34 3 3 3zm16-6H11v7H3V5H1v15h2v-3h18v3h2V7z\"/></svg>")
        self.sleep_button = Button(
            name="power-menu-button",
            child=self.sleep_button_svg,
            size=22,
            on_clicked=self.sleep,
        )

        self.reboot_button_svg = Svg(name="power-menu-button-svg", svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 0 24 24\" width=\"24px\" fill=\"#FFFFFF\"><path d=\"M0 0h24v24H0V0z\" fill=\"none\"/><path d=\"M7 7h10v3l4-4-4-4v3H5v6h2V7zm10 10H7v-3l-4 4 4 4v-3h12v-6h-2v4z\"/></svg>")
        self.reboot_button = Button(
            name="power-menu-button",
            child=self.reboot_button_svg,
            size=22,
            on_clicked=self.reboot,
        )

        self.shutdown_button_svg = Svg(name="power-menu-button-svg", svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\" width=\"24px\" fill=\"#FFFFFF\"><path d=\"M480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-80q100 0 170-70t70-170q0-51-19-94.5T650-650l-57 57q22 22 34.5 51t12.5 62q0 66-47 113t-113 47q-66 0-113-47t-47-113q0-33 12.5-62t34.5-51l-57-57q-32 32-51 75.5T240-480q0 100 70 170t170 70Zm-40-240h80v-240h-80v240Zm40 0Z\"/></svg>")
        self.shutdown_button = Button(
            name="power-menu-button",
            child=self.shutdown_button_svg,
            size=22,
            on_clicked=self.shutdown,
        )
        
        self.buttons = [
            self.lock_button,
            self.sleep_button,
            self.reboot_button,
            self.shutdown_button,
        ]

        for button in self.buttons:
            self.box.add(button)
        self.box.show_all()
        self.add(self.box)

        self.add_keybinding("Escape", lambda *_: self.close())

    def open(self):
        self._is_open = True
        self.set_visible(True)
        self.set_keyboard_mode("exclusive")
        self.parent_button.add_style_class("open")
        self.parent_button.get_child().set_from_string(
            "<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0,0,256,256\"><g fill=\"#000000\" fill-opacity=\"0.8\" fill-rule=\"nonzero\" stroke=\"none\" stroke-width=\"1\" stroke-linecap=\"butt\" stroke-linejoin=\"miter\" stroke-miterlimit=\"10\" stroke-dasharray=\"\" stroke-dashoffset=\"0\" font-family=\"none\" font-weight=\"none\" font-size=\"none\" text-anchor=\"none\" style=\"mix-blend-mode: normal\"><g transform=\"scale(10.66667,10.66667)\"><path d=\"M14.3,19.414c0.216,-0.569 0.342,-1.218 0.342,-1.913c0,-2.129 -1.139,-3.86 -2.539,-3.86c-1.412,0 -2.55,1.731 -2.55,3.86c0,0.683 0.114,1.332 0.33,1.89c-4.657,0.49 -7.936,2.437 -9.268,3.313c2.243,-3.234 4.589,-7.025 6.831,-11.386c0.558,-1.082 1.082,-2.152 1.571,-3.199c0.193,0.125 0.387,0.262 0.603,0.399c1.002,0.626 1.936,0.968 2.619,1.15c-0.501,-0.376 -1.047,-0.831 -1.605,-1.389c-0.421,-0.421 -0.797,-0.843 -1.116,-1.253c0.945,-2.072 1.765,-4.065 2.482,-5.955c1.195,3.165 2.687,6.615 4.554,10.247c1.207,2.334 2.437,4.509 3.666,6.513c-0.353,-0.193 -0.74,-0.376 -1.15,-0.535c-0.706,-0.273 -1.366,-0.444 -1.936,-0.546c0.774,0.387 1.674,0.9 2.619,1.583c0.615,0.456 1.161,0.911 1.628,1.355c0.011,0.011 0.011,0.011 0.023,0.023c0.649,1.059 1.321,2.038 1.981,2.994c-1.309,-0.866 -4.531,-2.779 -9.085,-3.291z\"></path></g></g></svg>"
        )

    def close(self):
        self._is_open = False
        self.set_visible(False)
        self.set_keyboard_mode("none")
        self.parent_button.remove_style_class("open")
        self.parent_button.get_child().set_from_string(
            "<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0,0,256,256\"><g fill=\"#ffffff\" fill-rule=\"nonzero\" stroke=\"none\" stroke-width=\"1\" stroke-linecap=\"butt\" stroke-linejoin=\"miter\" stroke-miterlimit=\"10\" stroke-dasharray=\"\" stroke-dashoffset=\"0\" font-family=\"none\" font-weight=\"none\" font-size=\"none\" text-anchor=\"none\" style=\"mix-blend-mode: normal\"><g transform=\"scale(10.66667,10.66667)\"><path d=\"M14.3,19.414c0.216,-0.569 0.342,-1.218 0.342,-1.913c0,-2.129 -1.139,-3.86 -2.539,-3.86c-1.412,0 -2.55,1.731 -2.55,3.86c0,0.683 0.114,1.332 0.33,1.89c-4.657,0.49 -7.936,2.437 -9.268,3.313c2.243,-3.234 4.589,-7.025 6.831,-11.386c0.558,-1.082 1.082,-2.152 1.571,-3.199c0.193,0.125 0.387,0.262 0.603,0.399c1.002,0.626 1.936,0.968 2.619,1.15c-0.501,-0.376 -1.047,-0.831 -1.605,-1.389c-0.421,-0.421 -0.797,-0.843 -1.116,-1.253c0.945,-2.072 1.765,-4.065 2.482,-5.955c1.195,3.165 2.687,6.615 4.554,10.247c1.207,2.334 2.437,4.509 3.666,6.513c-0.353,-0.193 -0.74,-0.376 -1.15,-0.535c-0.706,-0.273 -1.366,-0.444 -1.936,-0.546c0.774,0.387 1.674,0.9 2.619,1.583c0.615,0.456 1.161,0.911 1.628,1.355c0.011,0.011 0.011,0.011 0.023,0.023c0.649,1.059 1.321,2.038 1.981,2.994c-1.309,-0.866 -4.531,-2.779 -9.085,-3.291z\"></path></g></g></svg>"
        )

    def toggle(self):
        if self._is_open == False:
            self.open()
        else:
            self.close()

    def lock(self, *args):
        exec_shell_command_async("hyprlock")
        self.close()

    def sleep(self, *args):
        exec_shell_command_async("hyprlock")
        exec_shell_command_async("systemctl suspend")
        self.close()

    def reboot(self, *args):
        exec_shell_command_async("systemctl reboot")
        self.close()

    def shutdown(self, *args):
        exec_shell_command_async("systemctl poweroff")
        self.close()
