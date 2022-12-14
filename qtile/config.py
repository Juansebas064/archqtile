# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import subprocess


LAPTOP = True if subprocess.call("[ -d /proc/acpi/button/lid ] && true || false",shell=True) == 0 else False
mrg=11


@hook.subscribe.startup_once
def autostart():
    processes = [
        ["/usr/lib/lxpolkit/lxpolkit"],
        ["nm-applet"],
        ["pacman", "-Qu"],
        ["picom"],
        ["xfce4-clipman"],
        ["nitrogen", "--restore"],
        ["volmeicon"]
    ]

    for p in processes:
        subprocess.Popen(p)


mod = "mod4"
terminal = guess_terminal() 


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Keybindings for open applications
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.spawn("firefox")),
    Key([mod], "t", lazy.spawn("telegram-desktop")),
    Key([mod], "e", lazy.spawn("thunar")),    
    Key([mod], "y", lazy.spawn("whatsapp-nativefier")),
    Key([mod], "v", lazy.spawn("code")),
    Key([mod], "c", lazy.spawn("xfce4-popup-clipman")),
    Key([mod], "g", lazy.spawn("gparted")),
    Key([mod], "i", lazy.spawn("idea")),
    Key([mod], "o", lazy.spawn("/home/juan/.joplin/Joplin.AppImage %u")),
    Key([mod], "z", lazy.spawn("volumeicon")),
    Key([mod], "d", lazy.spawn("discord")),
    Key([mod], "u", lazy.spawn("sh /home/juan/MinecraftServerSync.sh")),
    Key([], "Print", lazy.spawn("xfce4-screenshooter -f -c")),
    Key(["control"], "Print", lazy.spawn("xfce4-screenshooter -w -c")),
    Key(["shift"], "Print", lazy.spawn("xfce4-screenshooter -r -c")),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "1234567"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus_stack=["#397086", "#8f3d3d"], 
        border_focus = "#3f6e84",
        border_normal = "#6b6b6b",
        border_width=5,
        margin=mrg,
        ),
    layout.Max(margin=mrg),
    layout.Floating(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    #layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

if LAPTOP:
    screens = [
        Screen(
            bottom=bar.Bar(
                [
                    widget.CurrentLayoutIcon(scale=0.4),
                    widget.Battery(
                        discharge_char='-',
                        charge_char='+',
                        format='{char} {percent:2.0%} {watt:.2f}W',
                        low_foreground='#d95850',
                        foreground='#aa8deb'
                    ),
                    widget.WindowCount(padding=5,fmt='{} |'),
                    widget.WindowName(max_chars=40),
                    widget.Prompt(),
                    widget.GroupBox(highlight_method='block',),
                    widget.Spacer(),
                    widget.Memory(measure_mem='M',padding=10,foreground='#d95850'),
                    widget.TextBox("~"),
                    widget.Systray(padding=10,),
                    widget.TextBox(" ~ "),
                    widget.Clock(format="%d/%m/%Y  %H:%M - %A   "),
                ],
                40,
                background = "#1a1d1f",
                margin = [0,mrg,mrg,mrg],
            ),
        ),
    ]
else:
    screens = [
        Screen(
            bottom=bar.Bar(
                [
                widget.CurrentLayoutIcon(scale=0.4),
                widget.WindowCount(padding=5,fmt='{} |'),
                widget.WindowName(max_chars=40),
                widget.Prompt(),
                widget.GroupBox(highlight_method='block',),
                widget.Spacer(),
                widget.CheckUpdates(
                    distro='Arch',
                    initial_text='Checking updates...',
                    no_update_string='Up to date!',
                    execute='alacritty -e sudo pacman -Syyu',
                    colour_have_updates='#dfb120',
                    colour_no_updates='#3ca87b',
                    padding=10
                ),
                widget.TextBox("~"),
                widget.Memory(measure_mem='M',padding=10,foreground='#d95850'),
                widget.TextBox("~"),
                widget.Systray(padding=10,),
                widget.Clock(format="  ~   %d / %m / %Y   %H:%M  -  %A   "),
                ],
                40,
                background = "#1a1d1f",
                margin = [0,mrg,mrg,mrg],
            ),
        ),
    ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    
    border_focus = "#3f6e84",
    border_normal = "#6b6b6b",
    border_width=5,

    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
