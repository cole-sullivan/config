from fabric import Application
from fabric.core.fabricator import Fabricator
from fabric.core.service import Service, Signal, Property
from fabric.hyprland.widgets import ActiveWindow, Workspaces, WorkspaceButton
from fabric.utils import (
    FormattedString,
    bulk_replace,
    exec_shell_command_async,
    get_relative_path,
    invoke_repeater,
    truncate,
)
from fabric.widgets.box import Box
from fabric.widgets.button import Button
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.datetime import DateTime
from fabric.widgets.eventbox import EventBox
from fabric.widgets.svg import Svg
from fabric.widgets.label import Label
from fabric.widgets.overlay import Overlay
from fabric.widgets.wayland import WaylandWindow
from fabric.widgets.window import Window
