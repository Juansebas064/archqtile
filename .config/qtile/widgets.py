# Libraries needed
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from libqtile.lazy import lazy


# Constant variables
SYMBOLS_FONT = 'Symbols Nerd Font'
SYMBOLS_SIZE = 32
ICON_SIZE = 20
FONT_SIZE = 16
WIDGETS_PADDING = 9


# Decorations for widgets
def decor(side):
    radius = {
        'left': [12,0,0,12],
        'right': [0,12,12,0],
        'both': 12
    }
    return (
        {"decorations": [
            RectDecoration(
                radius=radius[side],
                filled=True,
                use_widget_background=True,
                group=True,
            )
        ]}
    )


##################
# Widget's icons #
##################


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


# Text box
def text(background, foreground, text, side, callbacks: dict = {}):
    return (widget.TextBox(
        font=SYMBOLS_FONT,
        text=text,
        fontsize=ICON_SIZE,
        background=background,
        foreground=foreground,
        padding=0,
        mouse_callbacks=callbacks,
        **decor(side),
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
        fontsize=FONT_SIZE,
        show_zero=True,
        padding=10,
    )


# Virtual desktop indicator
def desktopIndicator(background, current_desktop, active_desktop, inactive_desktop):
    return (widget.GroupBox(
        font='Symbols Nerd Font',
        fontsize=22,
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
        padding=WIDGETS_PADDING,
        mouse_callbacks={
            "Button2": lazy.spawn("alacritty -e htop")
        },
        **decor('right'),
    ))


# System tray
def systemTray():
    return widget.Systray(padding=6)


# Battery level
def battery(background, foreground, lowForeground):
    return (widget.Battery(
        format='{percent:2.0%}',
        fontsize=FONT_SIZE,
        background=background,
        foreground=foreground,
        low_foreground=lowForeground,
        padding=WIDGETS_PADDING,
        update_interval=3,
    ))


# Volume level
def volume(background, foreground):
    return (widget.Volume(
        fontsize=FONT_SIZE,
        background=background,
        foreground=foreground,
        padding=WIDGETS_PADDING,
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
        padding=WIDGETS_PADDING,
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
        padding=WIDGETS_PADDING,
    ))
