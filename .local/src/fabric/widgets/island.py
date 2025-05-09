from imports import *

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

        self.test = Button(name="test") 

        self.workspaces = Workspaces(
            name="workspaces",
            spacing=4,
            buttons_factory=lambda ws_id: WorkspaceButton(id=ws_id, label=None),
        )

        self.stack = Stack(
            name="island-content",
            children=[
                self.workspaces,
            ],
        )

        self.children=[self.stack]
