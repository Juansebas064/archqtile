from libqtile import layout
from libqtile.config import Click, Drag, Group, Key, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import subprocess
import platform

from bar import qtileBar

hostname = platform.uname().node
MARGIN = 8


@hook.subscribe.startup_once
def autostart():
    processes = [
        ["/usr/lib/lxpolkit/lxpolkit"],
        ["nm-applet"],
        ["picom"],
        ["ulauncher", "--hide-window"],
        ["libinput-gestures-setup", "start"],
        ["xfce4-clipman"],
        ["nitrogen", "--restore"],
        ["blueman-applet"],
        ["setxkbmap", "-rules", "evdev", "-model", "evdev",
            "-layout", "us", "-variant", "altgr-intl"],
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
    Key([mod], "u", lazy.spawn("joplin")),
    # Key([mod], "u", lazy.spawn("/home/juan/.joplin/Joplin.AppImage %u")),
    Key([mod], "d", lazy.spawn("discord")),
    Key([mod], "u", lazy.spawn("sh /home/juan/MinecraftServerSync.sh")),
    Key([], "Print", lazy.spawn("xfce4-screenshooter -f -c")),
    Key(["control"], "Print", lazy.spawn("xfce4-screenshooter -w -c")),
    Key(["shift"], "Print", lazy.spawn("xfce4-screenshooter -r -c")),
    Key([mod], "r", lazy.spawn("ulauncher"), desc="Run ulauncher"),

    # Keybindings for media control
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "amixer -D default sset Master 2%+ unmute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "amixer -D default sset Master 2%- unmute")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D default sset Master toggle")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Keybindings for brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 2%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 2%-")),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "p", lazy.spawn("sh /home/juan/archqtile/scripts/dual-monitor.sh")),
    Key([mod], "o", lazy.spawn("sh /home/juan/archqtile/scripts/mirror.sh")),
    Key([mod], "up", lazy.to_screen(1), desc=""),
    Key([mod], "down", lazy.to_screen(0), desc=""),


    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod], "m", lazy.layout.grow(), desc="Grow window to the left"),
    Key([mod], "n", lazy.layout.shrink(), desc="Grow window to the right"),
    # Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    # Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "space", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "control"], "space", lazy.layout.set_ratio(
        0.5), desc="Default ratio"),

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

]


groups = [Group(f"{i+1}", label="") for i in range(6)]


#  

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
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadTall(
        # border_focus_stack=["#397086", "#8f3d3d"],
        border_focus="#3face4",
        border_normal="#111314",
        border_width=3,
        margin=MARGIN,
        single_border_width=0,
    ),
    layout.Max(margin=MARGIN),
]

widget_defaults = dict(
    font="Bitstream Vera Sans Mono Bold",
)
extension_defaults = widget_defaults.copy()

screens = qtileBar()


# Drag floating layouts.
# mouse = [
#     Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
#     Drag([mod], "Button3", lazy.window.set_size_floating(),
#          start=lazy.window.get_size()),
#     Click([mod], "Button2", lazy.window.bring_to_front()),
# ]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    border_focus="#3f6e84",
    border_normal="#6b6b6b",
    border_width=0,

    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class='system-config-printer'),
        Match(wm_class='ulauncher'),
        Match(wm_class='blueman-manager'),
        Match(wm_class='gcolor3'),
        Match(wm_class='pavucontrol'),
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
