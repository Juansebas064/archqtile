# Libraries needed
from libqtile import bar
from libqtile.lazy import lazy
from libqtile.config import Screen
import subprocess
import widgets


# Verify if the host is a laptop or desktop
LAPTOP = True if subprocess.call(
    "[ -d /proc/acpi/button/lid ] && true || false", shell=True) == 0 else False


# Color scheme
COLORS = {
    'background': '#1a1d1f00',
    'cwhite': '#ffffff',
    'cdark': '#1a1d1f',
    'cgray': '#34444c',
    'caquamarine': '#457c8a',
    'cblue': '#84b5cc',
    'cpurple': '#894bb3'
}

COLORS2 = {
    'background': '#1a1d1f00',
    'cwhite': '#ffffff',
    'cdark': '#1a1d1f',
    'cgray': '#34444c',
    'caquamarine': '#457c8a',
    'cblue': '#84b5cc',
    'cpurple': '#894bb3'
}


# Callbacks
CALLBACKS = {
    'htop': {"Button2": lazy.spawn("alacritty -e htop")},
    'pavucontrol': {"Button2": lazy.spawn("pavucontrol")}
}


#Function to show battery level only if it's a laptop
def laptopWidgets():
    if (LAPTOP):
        return (widgets.battery(COLORS['cpurple'], COLORS['cwhite'], COLORS['cwhite']))


# Bar
def qtileBar():
    return [
        Screen(
            bottom=bar.Bar(
                [
                    # Layout icon
                    widgets.layoutIcon(COLORS['background'], COLORS['cwhite']),

                    widgets.invisibleSeparator(COLORS['background']),

                    # Windows opened
                    widgets.windowCounter(),

                    widgets.invisibleSeparator(COLORS['background']),

                    # Desktop indicator
                    widgets.desktopIndicator(
                        COLORS['background'], COLORS['cpurple'], COLORS['cwhite'], COLORS['caquamarine']),

                    widgets.invisibleSeparator(COLORS['background']),

                    # System tray
                    widgets.systemTray(),

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
