# Libraries needed

from libqtile import widget
from libqtile.lazy import lazy


# Constant variables
LEFT = ""
RIGHT = ""
SYMBOLS_FONT = 'MesloLGS NF'
SYMBOLS_SIZE = 22
FONT_SIZE = 16


##################
# Widget's icons #
##################


# RAM
def RAMIcon(background, foreground):
    return (widget.TextBox(
        font=SYMBOLS_FONT,
        text='',
        fontsize=19,
        background=background,
        foreground=foreground,
        padding=6,
    ))


# Battery
def batteryIcon(background):
    return (widget.BatteryIcon(
        theme_path='~/.icons/Colloid-teal-dark/status/24/',
        background=background,
        scale=1,
    ))


###########
# Widgets #
###########


# Spacer
def spacer():
    return widget.Spacer()


# Invisible separator
def invisibleSeparator(foreground):
    return (widget.TextBox(
        text=".",
        foreground=foreground,
        padding=0,
    ))


# Bubble left
def bubbleLeft(background, foreground, callbacks: dict = {}):
    return (widget.TextBox(
        font=SYMBOLS_FONT,
        text=LEFT,
        fontsize=SYMBOLS_SIZE,
        background=background,
        foreground=foreground,
        padding=0,
        mouse_callbacks=callbacks,
    ))


# Bubble right
def bubbleRight(background, foreground, callbacks: dict = {}):
    return (widget.TextBox(
        font=SYMBOLS_FONT,
        text=RIGHT,
        fontsize=SYMBOLS_SIZE,
        background=background,
        foreground=foreground,
        padding=0,
        mouse_callbacks=callbacks,
    ))


# Layout icon
def layoutIcon(background, foreground):
    return (widget.CurrentLayoutIcon(
        background=background,
        foreground=foreground,
        padding=7,
        scale=0.8,
    ))


# Opened windows counter
def windowCounter():
    return widget.WindowCount(
        show_zero=True,
        padding=10,
    )


# Virtual desktop indicator
def desktopIndicator(background, current_desktop, active_desktop, inactive_desktop):
    return (widget.GroupBox(
        fontsize=FONT_SIZE,
        highlight_method='text',
        this_current_screen_border=current_desktop,     # Current desktop
        active=active_desktop,                          # Active desktop
        inactive=inactive_desktop,                      # Empty desktop
        background=background,
        borderwidth=2,
        padding=1,
    ))


# RAM usage
def RAMUsage(background, foreground):
    return (widget.Memory(
        format='{MemUsed:.1f}{mm}',
        fontsize=FONT_SIZE,
        measure_mem='G',
        background=background,
        foreground=foreground,
        padding=4,
        mouse_callbacks={
            "Button2": lazy.spawn("alacritty -e htop")
        }
    ))


# System tray
def systemTray():
    return widget.Systray(padding=4)


# Battery level
def battery(background, foreground, lowForeground):
    return (widget.Battery(
        format='{percent:2.0%}',
        fontsize=FONT_SIZE,
        background=background,
        foreground=foreground,
        low_foreground=lowForeground,
        padding=4,
        update_interval=3,
    ))


# Volume level
def volume(background, foreground):
    return (widget.Volume(
        fontsize=FONT_SIZE,
        background=background,
        foreground=foreground,
        padding=0,
        mouse_callbacks={
            "Button2": lazy.spawn("pavucontrol")
        },
    ))


# Date
def date(background, foreground):
    return (widget.Clock(
        format="%d/%m/%Y",
        fontsize=FONT_SIZE,
        background=background,
        foreground=foreground,
        padding=4,
        mouse_callbacks={
            "Button1": lazy.spawn("gsimplecal")
        },
    ))


# Clock
def clock(background, foreground):
    return (widget.Clock(
        format="%H:%M",
        fontsize=FONT_SIZE,
        background=background,
        foreground=foreground,
        padding=5,
    ))
