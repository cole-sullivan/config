from imports import *

class PowerMenu(Window):
    def __init__(self, **kwargs):
        super().__init__(
            title="fabric-menu",
            name="power",
            layer="top",
            anchor="center",
            margin="-320px 0px 0px 0px", 
            exclusivity="none",
            visible=False,
        )

        self.menu = Box(
            name="power-menu",
            orientation="v",
            spacing=12,
            h_align="center",
            v_align="center",
            visible=True,
            **kwargs,
        )

        self.parent_button = kwargs.get("parent_button", None)
        self._is_open = False

        self.menu_buttons = Box(
            name="power-menu-buttons",
            orientation="h",
            spacing=12,
            h_align="center",
            v_align="center",
            visible=True,
            **kwargs,
        )

        self.menu_label = Label(
            name="power-menu-label",
            label="--",
        )

        self.lock_button_svg = Svg(name="power-menu-button-svg", svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" fill=\"#FFFFFF\" viewBox=\"0 0 72 72\"><path d=\"M 36 10 C 28.28 10 22 16.28 22 24 L 22 28.587891 C 19.069798 29.775473 17 32.643974 17 36 L 17 52 C 17 56.418 20.582 60 25 60 L 47 60 C 51.418 60 55 56.418 55 52 L 55 36 C 55 32.643974 52.930202 29.775473 50 28.587891 L 50 24 C 50 16.28 43.72 10 36 10 z M 36 18 C 39.309 18 42 20.691 42 24 L 42 28 L 30 28 L 30 24 C 30 20.691 32.691 18 36 18 z\"></path></svg>")
        self.lock_button = Button(
            name="power-menu-button",
            child=self.lock_button_svg,
            size=24,
            on_clicked=self.lock,
        )

        self.sleep_button_svg = Svg(name="power-menu-button-svg", svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"24px\" height=\"24px\" fill=\"#FFFFFF\" viewBox=\"0 0 64 64\"><path d=\"M29.883 55h-9.177c-.747 0-1.432-.417-1.775-1.08-.344-.663-.289-1.463.142-2.073L26.022 42h-5.316c-1.104 0-2-.896-2-2s.896-2 2-2h9.177c.747 0 1.432.417 1.775 1.08.344.663.289 1.463-.142 2.073L24.566 51h5.316c1.104 0 2 .896 2 2S30.987 55 29.883 55zM49.706 40H38.412c-.747 0-1.432-.417-1.775-1.08-.344-.663-.289-1.463.142-2.073L45.847 24h-7.435c-1.104 0-2-.896-2-2s.896-2 2-2h11.294c.747 0 1.432.417 1.775 1.08.344.663.289 1.463-.142 2.073L42.271 36h7.435c1.104 0 2 .896 2 2S50.811 40 49.706 40zM30.412 33H16.294c-.747 0-1.432-.417-1.775-1.08-.344-.663-.289-1.463.142-2.073L26.552 13H16.294c-1.104 0-2-.896-2-2s.896-2 2-2h14.118c.747 0 1.432.417 1.775 1.08.344.663.289 1.463-.142 2.073L20.154 29h10.258c1.104 0 2 .896 2 2S31.517 33 30.412 33z\"></path></svg>")
        self.sleep_button = Button(
            name="power-menu-button",
            child=self.sleep_button_svg,
            size=24,
            on_clicked=self.sleep,
        )

        self.reboot_button_svg = Svg(name="power-menu-button-svg", svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"24px\" height=\"24px\" fill=\"#FFFFFF\" viewBox=\"0 0 72 72\"><path d=\"M 50.070312 9.1113281 C 49.457674 9.1726406 48.860281 9.4770312 48.441406 10.050781 L 45.5625 13.994141 C 41.133998 12.063285 36.069643 11.437868 30.923828 12.542969 C 19.161828 15.068969 10.977656 26.218313 12.097656 38.195312 C 13.401656 52.104312 26.108172 61.835891 39.701172 59.712891 C 51.205172 57.915891 59.516469 48.224578 59.980469 37.017578 C 60.083469 34.526578 57.835422 32.587609 55.357422 32.974609 C 53.464422 33.270609 52.070375 34.844141 51.984375 36.744141 C 51.645375 44.188141 46.11575 50.614594 38.46875 51.808594 C 29.81275 53.160594 21.693562 47.300406 20.226562 38.691406 C 18.792563 30.275406 24.412344 22.037172 32.777344 20.326172 C 35.507837 19.768092 38.196726 19.95137 40.664062 20.708984 L 38.207031 24.074219 C 37.090031 25.604219 38.184125 27.754906 40.078125 27.753906 L 54.798828 27.75 C 56.367828 27.75 57.481906 26.222516 57.003906 24.728516 L 52.517578 10.708984 C 52.156328 9.5814844 51.091377 9.0091406 50.070312 9.1113281 z\"></path></svg>")
        self.reboot_button = Button(
            name="power-menu-button",
            child=self.reboot_button_svg,
            size=24,
            on_clicked=self.reboot,
        )

        self.shutdown_button_svg = Svg(name="power-menu-button-svg", svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"24px\" height=\"24px\" fill=\"#FFFFFF\" viewBox=\"0 0 72 72\"><path d=\"M 36 9 C 33.791 9 32 10.791 32 13 L 32 31 C 32 33.209 33.791 35 36 35 C 38.209 35 40 33.209 40 31 L 40 13 C 40 10.791 38.209 9 36 9 z M 48.208984 16.003906 C 46.926455 15.937832 45.635312 16.49 44.804688 17.59375 C 43.475687 19.35875 43.82875 21.866312 45.59375 23.195312 C 49.66475 26.261312 52 30.929 52 36 C 52 44.822 44.822 52 36 52 C 27.178 52 20 44.822 20 36 C 20 30.929 22.33425 26.260312 26.40625 23.195312 C 28.17125 21.865313 28.524313 19.35875 27.195312 17.59375 C 25.865313 15.82775 23.35875 15.475687 21.59375 16.804688 C 15.49675 21.395688 12 28.393 12 36 C 12 49.233 22.767 60 36 60 C 49.233 60 60 49.233 60 36 C 60 28.393 56.50225 21.396688 50.40625 16.804688 C 49.74475 16.305937 48.978502 16.043551 48.208984 16.003906 z\"></path></svg>")
        self.shutdown_button = Button(
            name="power-menu-button",
            child=self.shutdown_button_svg,
            size=24,
            on_clicked=self.shutdown,
        )
        
        self.buttons = [
            self.lock_button,
            self.sleep_button,
            self.reboot_button,
            self.shutdown_button,
        ]

        for button in self.buttons:
            self.menu_buttons.add(button)
        self.menu_buttons.show_all()
        self.menu.add(self.menu_buttons)
        self.menu.add(self.menu_label)
        self.menu.show_all()
        self.add(self.menu)

        self.current = -1
        self.add_keybinding("h", lambda *_: self.prev())
        self.add_keybinding("l", lambda *_: self.next())

    def set_button_color(self, color):
        match self.current:
            case 0:
                self.buttons[self.current].get_child().set_from_string(
                    f"<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" fill=\"{color}\" viewBox=\"0 0 72 72\"><path d=\"M 36 10 C 28.28 10 22 16.28 22 24 L 22 28.587891 C 19.069798 29.775473 17 32.643974 17 36 L 17 52 C 17 56.418 20.582 60 25 60 L 47 60 C 51.418 60 55 56.418 55 52 L 55 36 C 55 32.643974 52.930202 29.775473 50 28.587891 L 50 24 C 50 16.28 43.72 10 36 10 z M 36 18 C 39.309 18 42 20.691 42 24 L 42 28 L 30 28 L 30 24 C 30 20.691 32.691 18 36 18 z\"></path></svg>"
                )
            case 1:
                self.buttons[self.current].get_child().set_from_string(
                    f"<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"24px\" height=\"24px\" fill=\"{color}\" viewBox=\"0 0 64 64\"><path d=\"M29.883 55h-9.177c-.747 0-1.432-.417-1.775-1.08-.344-.663-.289-1.463.142-2.073L26.022 42h-5.316c-1.104 0-2-.896-2-2s.896-2 2-2h9.177c.747 0 1.432.417 1.775 1.08.344.663.289 1.463-.142 2.073L24.566 51h5.316c1.104 0 2 .896 2 2S30.987 55 29.883 55zM49.706 40H38.412c-.747 0-1.432-.417-1.775-1.08-.344-.663-.289-1.463.142-2.073L45.847 24h-7.435c-1.104 0-2-.896-2-2s.896-2 2-2h11.294c.747 0 1.432.417 1.775 1.08.344.663.289 1.463-.142 2.073L42.271 36h7.435c1.104 0 2 .896 2 2S50.811 40 49.706 40zM30.412 33H16.294c-.747 0-1.432-.417-1.775-1.08-.344-.663-.289-1.463.142-2.073L26.552 13H16.294c-1.104 0-2-.896-2-2s.896-2 2-2h14.118c.747 0 1.432.417 1.775 1.08.344.663.289 1.463-.142 2.073L20.154 29h10.258c1.104 0 2 .896 2 2S31.517 33 30.412 33z\"></path></svg>"
                )
            case 2:
                self.buttons[self.current].get_child().set_from_string(
                    f"<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"24px\" height=\"24px\" fill=\"{color}\" viewBox=\"0 0 72 72\"><path d=\"M 50.070312 9.1113281 C 49.457674 9.1726406 48.860281 9.4770312 48.441406 10.050781 L 45.5625 13.994141 C 41.133998 12.063285 36.069643 11.437868 30.923828 12.542969 C 19.161828 15.068969 10.977656 26.218313 12.097656 38.195312 C 13.401656 52.104312 26.108172 61.835891 39.701172 59.712891 C 51.205172 57.915891 59.516469 48.224578 59.980469 37.017578 C 60.083469 34.526578 57.835422 32.587609 55.357422 32.974609 C 53.464422 33.270609 52.070375 34.844141 51.984375 36.744141 C 51.645375 44.188141 46.11575 50.614594 38.46875 51.808594 C 29.81275 53.160594 21.693562 47.300406 20.226562 38.691406 C 18.792563 30.275406 24.412344 22.037172 32.777344 20.326172 C 35.507837 19.768092 38.196726 19.95137 40.664062 20.708984 L 38.207031 24.074219 C 37.090031 25.604219 38.184125 27.754906 40.078125 27.753906 L 54.798828 27.75 C 56.367828 27.75 57.481906 26.222516 57.003906 24.728516 L 52.517578 10.708984 C 52.156328 9.5814844 51.091377 9.0091406 50.070312 9.1113281 z\"></path></svg>"
                )
            case 3:
                self.buttons[self.current].get_child().set_from_string(
                    f"<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"24px\" height=\"24px\" fill=\"{color}\" viewBox=\"0 0 72 72\"><path d=\"M 36 9 C 33.791 9 32 10.791 32 13 L 32 31 C 32 33.209 33.791 35 36 35 C 38.209 35 40 33.209 40 31 L 40 13 C 40 10.791 38.209 9 36 9 z M 48.208984 16.003906 C 46.926455 15.937832 45.635312 16.49 44.804688 17.59375 C 43.475687 19.35875 43.82875 21.866312 45.59375 23.195312 C 49.66475 26.261312 52 30.929 52 36 C 52 44.822 44.822 52 36 52 C 27.178 52 20 44.822 20 36 C 20 30.929 22.33425 26.260312 26.40625 23.195312 C 28.17125 21.865313 28.524313 19.35875 27.195312 17.59375 C 25.865313 15.82775 23.35875 15.475687 21.59375 16.804688 C 15.49675 21.395688 12 28.393 12 36 C 12 49.233 22.767 60 36 60 C 49.233 60 60 49.233 60 36 C 60 28.393 56.50225 21.396688 50.40625 16.804688 C 49.74475 16.305937 48.978502 16.043551 48.208984 16.003906 z\"></path></svg>"
                )
            case _:
                return

    def update_label(self):
        match self.current:
            case 0:
                self.menu_label.set_label("Lock") 
            case 1:
                self.menu_label.set_label("Sleep")
            case 2:
                self.menu_label.set_label("Reboot")
            case 3:
                self.menu_label.set_label("Shut Down")
            case _:
                return


    def open(self):
        self._is_open = True
        self.set_visible(True)
        self.set_focus(None)
        self.parent_button.add_style_class("open")
        self.parent_button.get_child().set_from_string(
            "<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0,0,256,256\"><g fill=\"#000000\" fill-opacity=\"0.8\" fill-rule=\"nonzero\" stroke=\"none\" stroke-width=\"1\" stroke-linecap=\"butt\" stroke-linejoin=\"miter\" stroke-miterlimit=\"10\" stroke-dasharray=\"\" stroke-dashoffset=\"0\" font-family=\"none\" font-weight=\"none\" font-size=\"none\" text-anchor=\"none\" style=\"mix-blend-mode: normal\"><g transform=\"scale(10.66667,10.66667)\"><path d=\"M14.3,19.414c0.216,-0.569 0.342,-1.218 0.342,-1.913c0,-2.129 -1.139,-3.86 -2.539,-3.86c-1.412,0 -2.55,1.731 -2.55,3.86c0,0.683 0.114,1.332 0.33,1.89c-4.657,0.49 -7.936,2.437 -9.268,3.313c2.243,-3.234 4.589,-7.025 6.831,-11.386c0.558,-1.082 1.082,-2.152 1.571,-3.199c0.193,0.125 0.387,0.262 0.603,0.399c1.002,0.626 1.936,0.968 2.619,1.15c-0.501,-0.376 -1.047,-0.831 -1.605,-1.389c-0.421,-0.421 -0.797,-0.843 -1.116,-1.253c0.945,-2.072 1.765,-4.065 2.482,-5.955c1.195,3.165 2.687,6.615 4.554,10.247c1.207,2.334 2.437,4.509 3.666,6.513c-0.353,-0.193 -0.74,-0.376 -1.15,-0.535c-0.706,-0.273 -1.366,-0.444 -1.936,-0.546c0.774,0.387 1.674,0.9 2.619,1.583c0.615,0.456 1.161,0.911 1.628,1.355c0.011,0.011 0.011,0.011 0.023,0.023c0.649,1.059 1.321,2.038 1.981,2.994c-1.309,-0.866 -4.531,-2.779 -9.085,-3.291z\"></path></g></g></svg>"
        )

    def close(self):
        self._is_open = False
        self.buttons[self.current].remove_style_class("selected")
        self.set_button_color("#ffffff")
        self.current = -1
        self.menu_label.set_label("--")
        self.set_visible(False)
        self.parent_button.remove_style_class("open")
        self.parent_button.get_child().set_from_string(
            "<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0,0,256,256\"><g fill=\"#ffffff\" fill-rule=\"nonzero\" stroke=\"none\" stroke-width=\"1\" stroke-linecap=\"butt\" stroke-linejoin=\"miter\" stroke-miterlimit=\"10\" stroke-dasharray=\"\" stroke-dashoffset=\"0\" font-family=\"none\" font-weight=\"none\" font-size=\"none\" text-anchor=\"none\" style=\"mix-blend-mode: normal\"><g transform=\"scale(10.66667,10.66667)\"><path d=\"M14.3,19.414c0.216,-0.569 0.342,-1.218 0.342,-1.913c0,-2.129 -1.139,-3.86 -2.539,-3.86c-1.412,0 -2.55,1.731 -2.55,3.86c0,0.683 0.114,1.332 0.33,1.89c-4.657,0.49 -7.936,2.437 -9.268,3.313c2.243,-3.234 4.589,-7.025 6.831,-11.386c0.558,-1.082 1.082,-2.152 1.571,-3.199c0.193,0.125 0.387,0.262 0.603,0.399c1.002,0.626 1.936,0.968 2.619,1.15c-0.501,-0.376 -1.047,-0.831 -1.605,-1.389c-0.421,-0.421 -0.797,-0.843 -1.116,-1.253c0.945,-2.072 1.765,-4.065 2.482,-5.955c1.195,3.165 2.687,6.615 4.554,10.247c1.207,2.334 2.437,4.509 3.666,6.513c-0.353,-0.193 -0.74,-0.376 -1.15,-0.535c-0.706,-0.273 -1.366,-0.444 -1.936,-0.546c0.774,0.387 1.674,0.9 2.619,1.583c0.615,0.456 1.161,0.911 1.628,1.355c0.011,0.011 0.011,0.011 0.023,0.023c0.649,1.059 1.321,2.038 1.981,2.994c-1.309,-0.866 -4.531,-2.779 -9.085,-3.291z\"></path></g></g></svg>"
        )

    def toggle(self):
        if self._is_open == False:
            self.open()
        else:
            self.close()
    
    def prev(self):
        self.buttons[self.current].remove_style_class("selected")
        self.set_button_color("#ffffff") 
        self.current = self.current - 1
        if self.current < 0:
            self.current = 3
        self.buttons[self.current].grab_focus()
        self.buttons[self.current].add_style_class("selected")
        self.set_button_color("#000000")
        self.update_label()

    def next(self):
        self.buttons[self.current].remove_style_class("selected")
        self.set_button_color("#ffffff")
        if self.current == -1:
            self.current = 0
        else:
            self.current = (self.current + 1) % 4
        self.buttons[self.current].grab_focus()
        self.buttons[self.current].add_style_class("selected")
        self.set_button_color("#000000")
        self.update_label()

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
