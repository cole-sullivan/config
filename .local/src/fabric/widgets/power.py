from imports import *

class PowerMenu(Window):
    def __init__(self, **kwargs):
        super().__init__(
            title="fabric-menu",
            name="power",
            layer="top",
            exclusivity="none",
            visible=False,
        )

        self.menu = Box(
            name="power-menu",
            orientation="v",
            spacing=4,
            visible=True,
            **kwargs,
        )

        self.parent_button = kwargs.get("parent_button", None)
        self._is_open = False

        # self.lock_icon = Svg(
        #     size=16,
        #     svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0,0,256,256\"><g fill=\"#ffffff\" fill-rule=\"nonzero\" stroke=\"none\" stroke-width=\"1\" stroke-linecap=\"butt\" stroke-linejoin=\"miter\" stroke-miterlimit=\"10\" stroke-dasharray=\"\" stroke-dashoffset=\"0\" font-family=\"none\" font-weight=\"none\" font-size=\"none\" text-anchor=\"none\" style=\"mix-blend-mode: normal\"><g transform=\"scale(4,4)\"><path d=\"M32,9c-7.168,0 -13,5.832 -13,13v5.34766c-2.32934,0.82421 -4,3.04047 -4,5.65234v16c0,3.314 2.686,6 6,6h22c3.314,0 6,-2.686 6,-6v-16c0,-2.61187 -1.67066,-4.82814 -4,-5.65234v-5.34766c0,-7.168 -5.832,-13 -13,-13zM32,13c4.963,0 9,4.038 9,9v5h-18v-5c0,-4.962 4.037,-9 9,-9zM21,31h22c1.105,0 2,0.895 2,2v16c0,1.105 -0.895,2 -2,2h-22c-1.105,0 -2,-0.895 -2,-2v-16c0,-1.105 0.895,-2 2,-2z\"></path></g></g></svg>",
        # )
        self.lock_label = Label(
            label="Lock Screen",
            name="power-menu-label",
            h_align="start",
        )
        # self.lock_children = Box(
        #     spacing=8,
        #     children=[self.lock_icon, self.lock_label],
        # )
        self.lock_button = Button(
            name="power-menu-button",
            child=self.lock_label,
            on_clicked=self.lock,
        )

        # self.sleep_icon = Svg(
        #     size=16,
        #     svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0,0,256,256\"><g fill=\"#ffffff\" fill-rule=\"nonzero\" stroke=\"none\" stroke-width=\"1\" stroke-linecap=\"butt\" stroke-linejoin=\"miter\" stroke-miterlimit=\"10\" stroke-dasharray=\"\" stroke-dashoffset=\"0\" font-family=\"none\" font-weight=\"none\" font-size=\"none\" text-anchor=\"none\" style=\"mix-blend-mode: normal\"><g transform=\"scale(4,4)\"><path d=\"M32,55C19.317,55,9,44.682,9,32S19.317,9,32,9s23,10.318,23,23S44.683,55,32,55z M32,12 c-11.028,0-20,8.972-20,20s8.972,20,20,20s20-8.972,20-20S43.028,12,32,12z\"></path><path d=\"M 50.659 39.085 C 51.593 39.085 52.353 39.753 52.353 40.58 C 52.353 41.406 51.593 42.076 50.659 42.076 C 50.149 42.076 13.861 42.076 13.352 42.076 C 12.418 42.076 11.658 41.406 11.658 40.58 C 11.658 39.753 12.418 39.085 13.352 39.085 C 13.861 39.085 50.149 39.085 50.659 39.085 Z\"></path></g></g></svg>",
        # )
        self.sleep_label = Label(
            label="Sleep",
            name="power-menu-label",
            h_align="start",
        )
        # self.sleep_children = Box(
        #     spacing=8,
        #     children=[self.sleep_icon, self.sleep_label]
        # )
        self.sleep_button = Button(
            name="power-menu-button",
            child=self.sleep_label,
            on_clicked=self.sleep,
        )

        # self.restart_icon = Svg(
        #     size=16,
        #     svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0,0,256,256\"><g fill=\"#ffffff\" fill-rule=\"nonzero\" stroke=\"none\" stroke-width=\"1\" stroke-linecap=\"butt\" stroke-linejoin=\"miter\" stroke-miterlimit=\"10\" stroke-dasharray=\"\" stroke-dashoffset=\"0\" font-family=\"none\" font-weight=\"none\" font-size=\"none\" text-anchor=\"none\" style=\"mix-blend-mode: normal\"><g transform=\"scale(4,4)\"><path d=\"M29.30469,6c-0.67613,-0.00675 -1.30469,0.53052 -1.30469,1.29102v3.08008c-10.2266,1.88732 -18,10.86444 -18,21.62891c0,12.131 9.869,22 22,22c12.131,0 22,-9.869 22,-22c0,-6.96 -3.34903,-13.58375 -8.95703,-17.71875c-0.889,-0.656 -2.14388,-0.46612 -2.79687,0.42188c-0.656,0.889 -0.46617,2.14283 0.42383,2.79883c4.59,3.384 7.33008,8.80405 7.33008,14.49805c0,9.925 -8.075,18 -18,18c-9.925,0 -18,-8.075 -18,-18c0,-8.54858 5.9965,-15.70917 14,-17.53516v2.24414c0,1.014 1.11661,1.6318 1.97461,1.0918l7.3418,-4.62305c0.868,-0.546 0.868,-1.81142 0,-2.35742l-7.3418,-4.62109c-0.2145,-0.135 -0.44455,-0.19697 -0.66992,-0.19922z\"></path></g></g></svg>",
        # )
        self.restart_label = Label(
            label="Restart...",
            name="power-menu-label",
            h_align="start",
        )
        # self.restart_children = Box(
        #     spacing=8,
        #     children=[self.restart_icon, self.restart_label]
        # )
        self.restart_button = Button(
            name="power-menu-button",
            child=self.restart_label,
            on_clicked=self.restart,
        )

        # self.shutdown_icon = Svg(
        #     size=16,
        #     svg_string="<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"100\" height=\"100\" viewBox=\"0,0,256,256\"><g fill=\"#ffffff\" fill-rule=\"nonzero\" stroke=\"none\" stroke-width=\"1\" stroke-linecap=\"butt\" stroke-linejoin=\"miter\" stroke-miterlimit=\"10\" stroke-dasharray=\"\" stroke-dashoffset=\"0\" font-family=\"none\" font-weight=\"none\" font-size=\"none\" text-anchor=\"none\" style=\"mix-blend-mode: normal\"><g transform=\"scale(4,4)\"><path d=\"M32,7c-1.104,0 -2,0.896 -2,2v18c0,1.104 0.896,2 2,2c1.104,0 2,-0.896 2,-2v-18c0,-1.104 -0.896,-2 -2,-2zM20.9707,13.32422c-0.38511,-0.00325 -0.77647,0.10366 -1.12109,0.33203c-6.168,4.093 -9.84961,10.95075 -9.84961,18.34375c0,12.131 9.869,22 22,22c12.131,0 22,-9.869 22,-22c0,-7.393 -3.68256,-14.25075 -9.85156,-18.34375c-0.919,-0.61 -2.15953,-0.3575 -2.76953,0.5625c-0.611,0.92 -0.36045,2.16048 0.56055,2.77148c5.047,3.349 8.06055,8.96077 8.06055,15.00977c0,9.925 -8.075,18 -18,18c-9.925,0 -18,-8.075 -18,-18c0,-6.049 3.01455,-11.66077 8.06055,-15.00977c0.921,-0.61 1.17155,-1.85148 0.56055,-2.77148c-0.38125,-0.575 -1.00854,-0.88911 -1.65039,-0.89453z\"></path></g></g></svg>",
        # )
        self.shutdown_label = Label(
            label="Shut Down...",
            name="power-menu-label",
            h_align="start",
        )
        # self.shutdown_children = Box(
        #     spacing=8,
        #     children=[self.shutdown_icon, self.shutdown_label]
        # )
        self.shutdown_button = Button(
            name="power-menu-button",
            child=self.shutdown_label,
            on_clicked=self.shutdown,
        )
        
        self.buttons = [
            self.lock_button,
            self.sleep_button,
            self.restart_button,
            self.shutdown_button,
        ]

        for button in self.buttons:
            self.menu.add(button)
        self.menu.show_all()
        self.add(self.menu)

        self.current = -1
        self.add_keybinding("Super k", lambda *_: self.prev())
        self.add_keybinding("Super j", lambda *_: self.next())

    def open(self):
        self._is_open = True
        self.set_visible(True)
        self.set_focus(None)
        self.parent_button.add_style_class("open")

    def close(self):
        self._is_open = False
        self.buttons[self.current].remove_style_class("selected")
        self.current = -1
        self.set_visible(False)
        self.parent_button.remove_style_class("open")

    def toggle(self):
        if self._is_open == False:
            self.open()
        else:
            self.close()
    
    def prev(self):
        self.buttons[self.current].remove_style_class("selected")
        self.current = self.current - 1
        if self.current < 0:
            self.current = 3
        self.buttons[self.current].grab_focus()
        self.buttons[self.current].add_style_class("selected")

    def next(self):
        self.buttons[self.current].remove_style_class("selected")
        if self.current == -1:
            self.current = 0
        else:
            self.current = (self.current + 1) % 4
        self.buttons[self.current].grab_focus()
        self.buttons[self.current].add_style_class("selected")

    def lock(self, *args):
        exec_shell_command_async("hyprlock")
        self.close()

    def sleep(self, *args):
        exec_shell_command_async("hyprlock")
        exec_shell_command_async("systemctl suspend")
        self.close()

    def restart(self, *args):
        exec_shell_command_async("systemctl reboot")
        self.close()

    def shutdown(self, *args):
        exec_shell_command_async("systemctl poweroff")
        self.close()
