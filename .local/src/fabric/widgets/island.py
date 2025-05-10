from imports import *
from .power import Power

class Island(Window):
    def __init__(
        self,
        **kwargs,
    ):
        super().__init__(
            name="island",
            layer="top",
            anchor="top",
            margin="-30px 0px 0px 0px",
        )

        self.workspaces = Workspaces(
            name="workspaces",
            spacing=4,
            buttons_factory=lambda ws_id: WorkspaceButton(id=ws_id, label=None),
        )
        self.power = Power(island=self)

        self.stack = Stack(
            name="island-content",
            children=[
                self.power,
                self.workspaces,
            ],
        )

        self.stack.set_visible_child(self.workspaces)
        self.stack.add_style_class("workspaces")

        self.children=[self.stack]

    def open(self, widget):
        widgets = {
            "power": self.power,
            "workspaces": self.workspaces,
        }
        # If already showing the requested widget, close instead.
        if self.stack.get_visible_child() == widgets.get(widget):
            self.close()
            return

        for style in widgets.keys():
            self.stack.remove_style_class(style)
        for _widget in widgets.values():
            _widget.remove_style_class("open")
        
        # self.set_keyboard_mode("exclusive")
        self.stack.set_visible_child(widgets[widget])
        widgets.get(widget).add_style_class("open")
        self.stack.add_style_class(widget)

    def close(self):
        for style in ["power"]:
            self.stack.remove_style_class(style)
        self.stack.get_visible_child().remove_style_class("open")
        
        self.stack.set_visible_child(self.workspaces)
        self.stack.add_style_class("workspaces")
        
