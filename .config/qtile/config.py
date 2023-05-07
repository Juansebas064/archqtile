from libqtile import layout
from libqtile.config import Click, Drag, Group, Key, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
from libqtile import qtile
import subprocess
import platform

from keybindings import keybindings
from bar import qtileBar


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


# This works when a window is assigned to a desktop and it's opened
@hook.subscribe.client_managed
def show_window(window):
    window.group.cmd_toscreen()


# Function to disable fullscreen when a popup dialog appears
@hook.subscribe.group_window_add
def dropdown_manager(group, window):
    if window.name in ["Enter name of file to save to…", 'Ulauncher - Application Launcher', 'Save As']:
        # Dropdown opened, disable full screen for windows in this group and save in function property
        all_group_windows: list() = qtile.select(
            [("group", group.name)]
        ).windows
        for group_window in all_group_windows:
            if group_window.info()["fullscreen"]:
                wid = group_window.info()["id"]
                qtile.select([("window", wid)]).cmd_disable_fullscreen()
                dropdown_manager.fullscreen_to_restore.append(wid)


hostname = platform.uname().node
MARGIN = 8
mod = "mod4"


keys = keybindings()


groups = [
    Group(name="1", label="󰈹", matches=[Match(wm_class=["firefox"])]),
    Group(name="2", label="", matches=[Match(wm_class=["code"])]),
    Group(name="3", label="󱞁", matches=[Match(wm_class=["joplin"])]),
    Group(name="4", label="", matches=[Match(wm_class=["telegram-desktop"]),
                                        Match(wm_class=["whatsapp-nativefier"])]),
    Group(name="5", label="󰋎", matches=[Match(wm_class=["discord"])]),
    Group(name="6", label="")
]


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
        Match(title='Enter name of file to save to…'),
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
