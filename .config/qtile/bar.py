# Libraries needed
from libqtile import bar
from libqtile.lazy import lazy
from libqtile.config import Screen
import subprocess
import widgets
from libqtile import qtile


# Verify if the host is a laptop or desktop
LAPTOP = True if subprocess.call(
    "[ -d /proc/acpi/button/lid ] && true || false", shell=True) == 0 else False


# Color scheme
COLORS = {
    'background': '#1a1d1f00',
    'cwhite': '#ffffff',
    'cblack': '#000000',
    'cred': '#bd3752',
    'cdark_blue': '#1f2851',
    'cgray': '#1d262a',
    'cblue': '#3572a5',
    'corange': '#ffa030',
    'cpurple': '#894bb3'
}


# Callbacks for widgets
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
                        COLORS['cred'], COLORS['cwhite'], COLORS['cdark_blue'], COLORS['cblack']),
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
                        COLORS['corange'], COLORS['cblack'], '  󰍛', 'left', CALLBACKS['htop']),

                    widgets.RAMUsage(COLORS['corange'], COLORS['cblack']),

                    widgets.invisibleSeparator(COLORS['background']),

                    # Volume level
                    widgets.volume(COLORS['cblue'], COLORS['cwhite']),

                    # widgets.invisibleSeparator(COLORS['background']),

                    # Date
                    widgets.date(COLORS['cgray'], COLORS['cwhite']),

                    # widgets.invisibleSeparator(COLORS['background']),

                    # Clock
                    widgets.clock(COLORS['cwhite'], COLORS['cblack']),
                ],
                25,
                background=COLORS['background'],
                margin=[2, 0, 4, 0],
                border_color=COLORS['background'],
                border_width=0,
            ),
        ),
    ]
