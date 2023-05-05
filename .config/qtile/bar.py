# Libraries needed
from libqtile import bar
from libqtile.lazy import lazy
from libqtile.config import Screen
import widgets


# Constants
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


# Laptop bar
def laptopBar():
    return [
        Screen(
            bottom=bar.Bar(
                [
                    # Layout icon
                    widgets.layoutIcon(COLORS['background'], COLORS['cwhite']),

                    # Windows opened
                    widgets.windowCounter(),

                    # Desktop indicator
                    widgets.desktopIndicator(
                        COLORS['background'], COLORS['cpurple'], COLORS['cwhite'], COLORS['caquamarine']),

                    widgets.invisibleSeparator(COLORS['background']),

                    # RAM usage
                    # widgets.bubbleLeft(COLORS['background'], COLORS['cblue'], CALLBACKS['htop']),
                    widgets.RAMUsage(COLORS['cblue'], COLORS['cdark']),

                    widgets.invisibleSeparator(COLORS['background']),

                    # System tray
                    widgets.systemTray(),

                    # Spacer
                    widgets.spacer(),

                    # Battery level
                    widgets.battery(COLORS['cpurple'],
                                    COLORS['cwhite'], COLORS['cwhite']),

                    widgets.invisibleSeparator(COLORS['background']),

                    # Volume level
                    widgets.volume(COLORS['caquamarine'], COLORS['cwhite']),

                    widgets.invisibleSeparator(COLORS['background']),

                    # Date
                    widgets.date(COLORS['cgray'], COLORS['cwhite']),

                    widgets.invisibleSeparator(COLORS['background']),

                    # Clock
                    widgets.clock(COLORS['cwhite'], COLORS['cdark']),
                ],
                22,
                background=COLORS['background'],
                margin=0,
                border_color=COLORS['background'],
                border_width=6,
            ),
        ),
    ]


# Desktop bar
def desktopBar():
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

                    # widgets.invisibleSeparator(COLORS['background']),

                    # RAM usage
                    # widgets.bubbleLeft(COLORS['background'], COLORS['cblue'], CALLBACKS['htop']),
                    widgets.text(COLORS['cblue'], COLORS['cdark'], CALLBACKS['htop'],'󰍛'),
                    widgets.invisibleSeparator(COLORS['background']),

                    widgets.RAMUsage(COLORS['cblue'], COLORS['cdark']),

                    widgets.invisibleSeparator(COLORS['background']),

                    # Volume level
                    widgets.bubbleLeft(COLORS['cblue'], COLORS['caquamarine'], CALLBACKS['htop']),
                    widgets.volume(COLORS['caquamarine'], COLORS['cwhite']),

                    # widgets.invisibleSeparator(COLORS['background']),

                    # Date
                    widgets.bubbleLeft(COLORS['caquamarine'], COLORS['cgray'], CALLBACKS['htop']),
                    widgets.date(COLORS['cgray'], COLORS['cwhite']),

                    # widgets.invisibleSeparator(COLORS['background']),

                    # Clock
                    widgets.bubbleLeft(COLORS['cgray'], COLORS['cwhite'], CALLBACKS['htop']),
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
