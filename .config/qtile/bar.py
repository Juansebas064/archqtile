# Libraries needed
from libqtile import bar
from libqtile.lazy import lazy
from libqtile.config import Screen
import subprocess
import widgets
from libqtile import qtile
# from libqtile import hook
# from libqtile.backend.x11 import window


# @hook.subscribe.client_focus
# def windowName(window.win) -> str:
#     return widgets.text(COLORS['background'], COLORS['cwhite'], , 'both')


# Verify if the host is a laptop or desktop
LAPTOP = True if subprocess.call(
    "[ -d /proc/acpi/button/lid ] && true || false", shell=True) == 0 else False


# Color scheme
COLORS = {
    'background': '#1a1d1f00',
    'cwhite': '#ffffff',
    'cdark': '#000000',
    'cred': '#bd3752',
    'cskin': '#11263b',
    'cgray': '#1d262a',
    'caquamarine': '#457c8a',
    'cblue': '#84b5cc',
    'cpurple': '#894bb3'
}


# Callbacks
CALLBACKS = {
    'htop': {"Button2": lazy.spawn("alacritty -e htop")},
    'pavucontrol': {"Button2": lazy.spawn("pavucontrol")}
}


# Function to show battery level only if it's a laptop
def laptopWidgets():
    if (LAPTOP):
        return (widgets.battery(COLORS['cpurple'], COLORS['cwhite'], COLORS['cwhite']))
    else:
        return (widgets.invisibleSeparator(COLORS['background']))


# Bar
def qtileBar():
    return [
        Screen(
            bottom=bar.Bar(
                [
                    widgets.invisibleSeparator(COLORS['background']),

                    # System tray
                    widgets.systemTray(),

                    widgets.invisibleSeparator(COLORS['background']),

                    # Window name
                    widgets.windowName(),

                    # Spacer
                    widgets.spacer(),

                    # Layout icon
                    widgets.layoutIcon(COLORS['background'], COLORS['cwhite']),

                    # Desktop indicator
                    widgets.text(
                        COLORS['cred'], COLORS['background'], 'h', 'left'),
                    widgets.desktopIndicator(
                        COLORS['cred'], COLORS['cwhite'], COLORS['cskin'], COLORS['cdark']),
                    widgets.text(
                        COLORS['cred'], COLORS['background'], 'h', 'right'),


                    # Windows opened
                    widgets.windowCounter(),
                    widgets.text(
                        COLORS['background'], COLORS['cwhite'], '󱂬', 'left'),

                    # Spacer
                    widgets.spacer(),

                    # Battery (only for laptop)
                    laptopWidgets(),

                    widgets.invisibleSeparator(COLORS['background']),

                    # RAM usage
                    widgets.text(
                        COLORS['cblue'], COLORS['cdark'], '  󰍛', 'left', CALLBACKS['htop']),

                    widgets.RAMUsage(COLORS['cblue'], COLORS['cdark']),

                    widgets.invisibleSeparator(COLORS['background']),

                    # Volume level
                    widgets.volume(COLORS['caquamarine'], COLORS['cwhite']),

                    # widgets.invisibleSeparator(COLORS['background']),

                    # Date
                    widgets.date(COLORS['cgray'], COLORS['cwhite']),

                    # widgets.invisibleSeparator(COLORS['background']),

                    # Clock
                    widgets.clock(COLORS['cwhite'], COLORS['cdark']),
                ],
                25,
                background=COLORS['background'],
                margin=[2, 0, 8, 0],
                border_color=COLORS['background'],
                border_width=0,
            ),
        ),
    ]
