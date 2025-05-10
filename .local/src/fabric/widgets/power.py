from imports import *

class Power(Box):
    def __init__(
        self,
        **kwargs,
    ):
        super().__init__(
            name="power",
            orientation="v",
            spacing=4,
            visible=True,
            **kwargs,
        )

        self.island = kwargs["island"]

        self.lock_button = Button(
            child=Label(name="button-label", label="LOCK"),
            on_clicked=self.lock,
        )

        self.reboot_button = Button(
            child=Label(name="button-label", label="REBOOT"),
            on_clicked=self.reboot,
        )

        self.children = [
            self.lock_button,
            self.reboot_button,
        ]

    def close(self):
        self.island.close()

    def lock(self, *args):
        print("Locking screen...")
        exec_shell_command_async("hyprlock")
        self.close()

    def reboot(self, *args):
        print("Rebooting system...")
        exec_shell_command_async("systemctl reboot")
        self.close()
