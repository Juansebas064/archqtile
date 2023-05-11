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
    'cred': '#b82e66',
    'cdark_blue': '#1f2851',
    'cgray': '#1d262a',
    'cblue': '#1762a6',
    'corange': '#d96348',
    'cpurple': '#7a0b4f',
    'cgreen': '#3d8a6d'
}


# Callbacks for widgets
CALLBACKS = {
    'htop': {"Button2": lazy.spawn("alacritty -e htop")},
    'pavucontrol': {"Button2": lazy.spawn("pavucontrol")}
}


# Function to show battery level only if it's a laptop
def helperBatteryWidget():
    if (LAPTOP):
        return (widgets.text(COLORS['cgreen'], COLORS['background'], 'h', 'left'))
    else:
        return (widgets.text(COLORS['background'], COLORS['background'], '', 'right'))


def batteryWidget():
    if (LAPTOP):
        return (widgets.battery(COLORS['cgreen'], COLORS['cwhite'], COLORS['cwhite'], 'right'))
    else:
        return (widgets.text(COLORS['background'], COLORS['background'], '', 'right'))


def batteryIconWidget():
    if (LAPTOP):
        return (widgets.batteryIcon(COLORS['cgreen'], COLORS['cwhite'], 'left'))
    else:
        return (widgets.text(COLORS['background'], COLORS['background'], '', 'both'))


# Bar
def qtileBar():
    return [
        Screen(
            bottom=bar.Bar(
                [
                    widgets.invisibleSeparator(COLORS['background']),

                    # Battery (only for laptop)
                    helperBatteryWidget(),
                    batteryIconWidget(),
                    batteryWidget(),

                    widgets.invisibleSeparator(COLORS['background']),

                    # System tray
                    widgets.systemTray(),

                    widgets.text(
                        COLORS['background'], COLORS['cwhite'], '     ', 'both'),

                    # widgets.invisibleSeparator(COLORS['background']),

                    # Window name
                    widgets.windowName(),

                    # Spacer
                    widgets.spacer(),

                    # Layout icon
                    widgets.layoutIcon(COLORS['background'], COLORS['cwhite']),

                    ####
                    # Desktop indicator
                    widgets.text(
                        COLORS['corange'], COLORS['background'], 'h', 'left'),
                    widgets.desktopIndicator(
                        COLORS['corange'], COLORS['cwhite'], COLORS['cdark_blue'], COLORS['cblack']),
                    widgets.text(
                        COLORS['corange'], COLORS['background'], 'h', 'right'),
                    ####

                    # Windows opened
                    widgets.windowCounter(),
                    widgets.text(
                        COLORS['background'], COLORS['cwhite'], '󱂬', 'left'),

                    # Spacer
                    widgets.spacer(),

                    widgets.invisibleSeparator(COLORS['background']),

                    # RAM usage
                    widgets.text(
                        COLORS['cred'], COLORS['cwhite'], '  󱕍', 'left', CALLBACKS['htop']),

                    widgets.RAMUsage(COLORS['cred'], COLORS['cwhite']),

                    widgets.invisibleSeparator(COLORS['background']),

                    # Volume level
                    widgets.text(COLORS['cblue'], COLORS['background'], 'L', 'left'),
                    widgets.volumeIcon(COLORS['cblue'], COLORS['cwhite']),
                    widgets.volume(COLORS['cblue'], COLORS['cwhite']),

                    widgets.invisibleSeparator(COLORS['background']),

                    # Date
                    widgets.date(COLORS['cpurple'], COLORS['cwhite']),

                    # widgets.invisibleSeparator(COLORS['background']),

                    # Clock
                    widgets.clock(COLORS['cgreen'], COLORS['cblack']),
                ],
                25,
                background=COLORS['background'],
                margin=[2, 0, 4, 0],
                border_color=COLORS['background'],
                border_width=0,
            ),
        ),
    ]
