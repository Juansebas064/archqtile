from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import subprocess
import platform

hostname = platform.uname().node

LAPTOP = True if subprocess.call("[ -d /proc/acpi/button/lid ] && true || false",shell=True) == 0 else False
mrg=11


@hook.subscribe.startup_once
def autostart():
    processes = [
        ["/usr/lib/lxpolkit/lxpolkit"],
        ["nm-applet"],
        ["picom"], 
        ["ulauncher", "--hide-window"], 
        ["xfce4-clipman"],
        ["nitrogen", "--restore"],
        ["blueman-applet"],
        ["setxkbmap", "-rules", "evdev", "-model", "evdev", "-layout", "us", "-variant", "altgr-intl"],
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
    Key([mod], "d", lazy.spawn("discord")),
    Key([mod], "u", lazy.spawn("sh /home/juan/MinecraftServerSync.sh")),
    Key([], "Print", lazy.spawn("xfce4-screenshooter -f -c")),
    Key(["control"], "Print", lazy.spawn("xfce4-screenshooter -w -c")),
    Key(["shift"], "Print", lazy.spawn("xfce4-screenshooter -r -c")),
    # Key([mod], "r", lazy.spawn("ulauncher"), desc="Spawn ulauncher"),

    # Keybindings for media control
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D default sset Master 2%+ unmute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D default sset Master 2%- unmute")),
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
    #Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod], "m", lazy.layout.grow(), desc="Grow window to the left"),
    Key([mod], "n", lazy.layout.shrink(), desc="Grow window to the right"),
    #Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    #Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "space", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "control"], "space", lazy.layout.set_ratio(0.5), desc="Default ratio"),

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

groups = [Group(f"{i+1}", label="") for i in range(6)]

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
    layout.MonadTall(
        # border_focus_stack=["#397086", "#8f3d3d"], 
        border_focus = "#3f6e84",
        border_normal = "#6b6b6b",
        border_width=5,
        margin=mrg,
        single_border_width = 0,
        ),
    layout.Max(margin=mrg),
]

widget_defaults = dict(
    font="Bitstream Vera Sans Mono Bold",
    fontsize=15,
)
extension_defaults = widget_defaults.copy()

left = ""
right = ""
symbols_font = 'MesloLGS NF'
size=22
laptop_fontsize = 16

bgcolors = {
        0:'#1a1d1f',
        1:'#34444c',
        2:'#457c8a',
        3:'#84b5cc',
        4:'#cfd8dc',
        5:'#ffffff'
        }

if LAPTOP:
    screens = [
        Screen(
            bottom=bar.Bar(
                [

                #Layout icon
                widget.CurrentLayoutIcon(
                    scale=0.65,
                    background=bgcolors[0],
                    foreground="#ffffff",
                    padding=5,
                    ),

                #widget.WindowCount(show_zero=True,),

                widget.TextBox(
                    text="",
                    padding=0,
                    foreground=bgcolors[0],
                    ),


                #Widget for show virtual desktops
                widget.TextBox(
                    font=symbols_font,
                    text=left,
                    background=bgcolors[0],
                    foreground=bgcolors[1],
                    padding=0,
                    fontsize = size,
                    ),
                widget.GroupBox(
                    highlight_method='line',
                    fontsize=17,
                    this_current_screen_border = "#ffffff",
                    highlight_color = bgcolors[1],
                    borderwidth = 2,
                    active = "#ffffff",
                    background = bgcolors[1],
                    inactive = bgcolors[2],
                    padding=1,
                    ),
                widget.TextBox(
                    font = symbols_font,
                    text =right,
                    background = bgcolors[0],
                    foreground = bgcolors[1],
                    padding =0,
                    fontsize = size,
                    ),
                

                widget.TextBox(
                    text="-",
                    padding=0,
                    foreground= bgcolors[0],
                    ),


                #Widget for RAM usage
                widget.TextBox(
                    text=left,
                    background=bgcolors[0],
                    foreground=bgcolors[3],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),
                widget.TextBox(
                    text='',
                    background=bgcolors[3],
                    foreground=bgcolors[0],
                    padding=4,
                    fontsize = 19,
                    font=symbols_font,
                    ),
                widget.Memory(
                    fontsize=laptop_fontsize,
                    measure_mem='G',
                    format='{MemUsed:.1f}{mm}',
                    #format=' {MemUsed:.1f}{mm}/{MemTotal:.1f}{mm}',
                    padding=2,
                    foreground=bgcolors[0],
                    background=bgcolors[3],
                    ),
                 widget.TextBox(
                    text=right,
                    background=bgcolors[0],
                    foreground=bgcolors[3],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),     

                # #System tray
                # widget.WidgetBox(
                #     start_opened = True,
                #     font=symbols_font,
                #     fontsize=25,
                #     text_closed='  ',
                #     text_open='  ',
                #     padding=0,
                #     widgets=[
                #         #System tray
                #         widget.Systray(padding=4),
                #     ]
                # ),

                widget.TextBox(
                    text="-",
                    padding=3,
                    foreground= bgcolors[0],
                    ),

                #System tray
                widget.Systray(padding=4),


                widget.TextBox(
                    text="-",
                    padding=3,
                    foreground= bgcolors[0],
                    ),


                widget.Spacer(),

                
                #Widget for window name
                widget.WindowName(
                    empty_group_string = 'Desktop',
                    foreground=bgcolors[5],
                    background=bgcolors[0],
                    format='{name}',
                    width=bar.CALCULATED,
                    max_chars=25,
                    fontsize=laptop_fontsize,
                    ),              


                widget.Spacer(),
                #widget.Systray(padding=10),


                #Widget for battery level
                 widget.TextBox(
                    text=left,
                    background=bgcolors[0],
                    foreground='#aa8deb',
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),
                widget.Battery(
                    font=symbols_font,
                    fontsize=13,
                    full_char='',
                    discharge_char='',
                    charge_char='',
                    format='{char}',
                    low_foreground=bgcolors[0],
                    foreground=bgcolors[0],
                    background='#aa8deb',
                    update_interval=5,
                    padding=5,
                ),
                widget.Battery(
                    format='{percent:2.0%}',
                    fontsize=laptop_fontsize,
                    low_foreground=bgcolors[0],
                    foreground=bgcolors[0],
                    background='#aa8deb',
                    update_interval=5,
                    padding=1,
                ),
                 widget.TextBox(
                    text=right,
                    background=bgcolors[0],
                    foreground='#aa8deb',
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),


                widget.TextBox(
                    text="-",
                    padding=0,
                    foreground=bgcolors[0],
                    ),


               #Widget for volume level
                widget.TextBox(
                    text=left,
                    background=bgcolors[0],
                    foreground=bgcolors[3],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),
                widget.Volume(
                    fmt='墳',
                    background=bgcolors[3],
                    foreground=bgcolors[0],
                    padding=3,
                    fontsize = 20,
                    font=symbols_font,
                    update_interval=0.1,
                    ),
                widget.Volume(
                    background = bgcolors[3],
                    foreground = bgcolors[0],
                    padding = 3,
                    fontsize=laptop_fontsize,
                    ),
                widget.TextBox(
                    text=right,
                    background=bgcolors[0],
                    foreground=bgcolors[3],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ), 


                widget.TextBox(
                    text="-",
                    padding=0,
                    foreground=bgcolors[0],
                    ),


                #Widget for date
                widget.TextBox(
                    text=left,
                    background=bgcolors[0],
                    foreground=bgcolors[1],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                ),
                widget.TextBox(
                    text='',
                    font=symbols_font,
                    fontsize=19,
                    padding=4,
                    foreground=bgcolors[5],
                    background=bgcolors[1],
                ),
                widget.Clock(
                    format="%d/%m/%Y",
                    foreground=bgcolors[5],
                    background=bgcolors[1],
                    padding=3,
                    fontsize=laptop_fontsize,
                ),
                widget.TextBox(
                    text=right,
                    background=bgcolors[0],
                    foreground=bgcolors[1],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                ),

                
                widget.TextBox(
                    text="-",
                    padding=0,
                    foreground=bgcolors[0],
                ), 


               #Widget for clock
                widget.TextBox(
                    text=left,
                    background=bgcolors[0],
                    foreground=bgcolors[5],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),
                widget.TextBox(
                    text="",
                    background=bgcolors[5],
                    foreground=bgcolors[0],
                    padding=3,
                    fontsize = 21,
                    font=symbols_font,
                    ),
                widget.Clock(
                    #widget.Clock(format="  ~   %d / %m / %Y   %H:%M  -  %A   "),
                    format="%H:%M",
                    foreground=bgcolors[0],
                    background=bgcolors[5],
                    padding=3,
                    fontsize=laptop_fontsize,
                    ),
                widget.TextBox(
                    text=right,
                    background=bgcolors[0],
                    foreground=bgcolors[5],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),               


                widget.TextBox(
                    text="-",
                    padding=0,
                    foreground=bgcolors[0],
                    ),                


                #Arch Icon
                # widget.TextBox(
                #     text=left,
                #     font=symbols_font,
                #     foreground=bgcolors[5],
                #     background=bgcolors[0],
                #     padding=0,
                #     fontsize = size,
                #     ),
                # #Prompt
                # widget.Prompt(
                #         background=bgcolors[5],
                #         foreground=bgcolors[0],
                #         prompt='',
                #         padding=0,
                #         fontsize=15,
                #     ),
                # widget.TextBox(
                #     font=symbols_font,
                #     fontsize = 30,
                #     text='',
                #     background = bgcolors[5],
                #     foreground = bgcolors[0],
                #     padding = 0,
                #     ),
                # widget.TextBox(
                #     text=right,
                #     font=symbols_font,
                #     foreground=bgcolors[5],
                #     background=bgcolors[0],
                #     padding=0,
                #     fontsize = size,
                #     ),
                ],
                27,
                background = bgcolors[0],
                margin = [0,mrg,mrg,mrg],
                border_color=bgcolors[0],
                border_width=9,
            ),
        ),
    ]
else:
    screens = [
        Screen(
            bottom=bar.Bar(
                [

                #Layout icon
                widget.CurrentLayoutIcon(
                    scale=0.65,
                    background=bgcolors[0],
                    foreground="#ffffff",
                    padding=7,
                    ),


                widget.WindowCount(show_zero=True,),


                widget.TextBox(
                    text=".",
                    padding=0,
                    foreground=bgcolors[0],
                    ),


                #Widget for show virtual desktops
                widget.TextBox(
                    font=symbols_font,
                    text=left,
                    background=bgcolors[0],
                    foreground=bgcolors[1],
                    padding=0,
                    fontsize = size,
                    ),
                widget.GroupBox(
                    highlight_method='line',
                    fontsize=18,
                    this_current_screen_border = "#ffffff",
                    highlight_color = bgcolors[1],
                    borderwidth = 2,
                    active = "#ffffff",
                    background = bgcolors[1],
                    inactive = bgcolors[2],
                    padding=1,
                    ),
                widget.TextBox(
                    font = symbols_font,
                    text =right,
                    background = bgcolors[0],
                    foreground = bgcolors[1],
                    padding =0,
                    fontsize = size,
                    ),
                

                widget.TextBox(
                    text="-",
                    padding=3,
                    foreground= bgcolors[0],
                    ),


                #Widget for RAM usage
                widget.TextBox(
                    text=left,
                    background=bgcolors[0],
                    foreground=bgcolors[3],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),
                widget.TextBox(
                    text='󰍛',
                    background=bgcolors[3],
                    foreground=bgcolors[0],
                    padding=6,
                    fontsize = 19,
                    font=symbols_font,
                    ),
                widget.Memory(
                    measure_mem='G',
                    format='{MemUsed:.1f}{mm}',
                    #format=' {MemUsed:.1f}{mm}/{MemTotal:.1f}{mm}',
                    padding=4,
                    foreground=bgcolors[0],
                    background=bgcolors[3],
                    ),
                 widget.TextBox(
                    text=right,
                    background=bgcolors[0],
                    foreground=bgcolors[3],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),               


                widget.TextBox(
                    text="-",
                    padding=3,
                    foreground= bgcolors[0],
                    ),

                
                #System tray
                widget.WidgetBox(
                    font=symbols_font,
                    fontsize=25,
                    text_closed='󰁙 ',
                    text_open='󰁒 ',
                    padding=5,
                    widgets=[
                        #System tray
                        widget.Systray(padding=10),
                    ]
                ),


                widget.Spacer(),

                
                #Widget for window name
                widget.WindowName(
                    empty_group_string = 'Desktop',
                    foreground=bgcolors[5],
                    background=bgcolors[0],
                    format='{name}',
                    width=bar.CALCULATED,
                    max_chars=45,
                    ),      


                widget.Spacer(),
                #widget.Systray(padding=10),


               #Widget for volume level
                widget.TextBox(
                    text=left,
                    background=bgcolors[0],
                    foreground=bgcolors[2],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),
                widget.Volume(
                    fmt='󰕾',
                    background=bgcolors[2],
                    foreground=bgcolors[5],
                    padding=5,
                    fontsize = 19,
                    font=symbols_font,
                    update_interval=0.1,
                    ),
                widget.Volume(
                    font=symbols_font,
                    background = bgcolors[2],
                    foreground = bgcolors[5],
                    padding = 5,
                    ),
                widget.TextBox(
                    text=right,
                    background=bgcolors[0],
                    foreground=bgcolors[2],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ), 


                widget.TextBox(
                    text="-",
                    padding=3,
                    foreground=bgcolors[0],
                    ),


                #Widget for date
                widget.TextBox(
                    text=left,
                    background=bgcolors[0],
                    foreground=bgcolors[1],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                ),
                widget.TextBox(
                    text='󰃵',
                    font=symbols_font,
                    fontsize=19,
                    padding=7,
                    foreground=bgcolors[5],
                    background=bgcolors[1],
                ),
                widget.Clock(
                    format="%d/%m/%Y",
                    foreground=bgcolors[5],
                    background=bgcolors[1],
                    padding=4,
                ),
                widget.TextBox(
                    text=right,
                    background=bgcolors[0],
                    foreground=bgcolors[1],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                ),

                
                widget.TextBox(
                    text="-",
                    padding=3,
                    foreground=bgcolors[0],
                ), 


               #Widget for clock
                widget.TextBox(
                    text=left,
                    background=bgcolors[0],
                    foreground=bgcolors[3],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),
                widget.TextBox(
                    text="󰥔",
                    background=bgcolors[3],
                    foreground=bgcolors[0],
                    padding=7,
                    fontsize = 19,
                    font=symbols_font,
                    ),
                widget.Clock(
                    #widget.Clock(format="  ~   %d / %m / %Y   %H:%M  -  %A   "),
                    format="%H:%M",
                    foreground=bgcolors[0],
                    background=bgcolors[3],
                    padding=5,
                    ),
                widget.TextBox(
                    text=right,
                    background=bgcolors[0],
                    foreground=bgcolors[3],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),               


                widget.TextBox(
                    text="-",
                    padding=3,
                    foreground=bgcolors[0],
                    ),                



                #Arch Icon
                widget.TextBox(
                    text=left,
                    font=symbols_font,
                    foreground=bgcolors[4],
                    background=bgcolors[0],
                    padding=0,
                    fontsize = size,
                    ),
                #Prompt
                widget.Prompt(
                        background=bgcolors[4],
                        foreground=bgcolors[0],
                        prompt='Run: ',
                    ),
                widget.TextBox(
                    font=symbols_font,
                    fontsize = 30,
                    text='',
                    background = bgcolors[4],
                    foreground = bgcolors[0],
                    padding = 0,
                    ),
                widget.TextBox(
                    text=right,
                    font=symbols_font,
                    foreground=bgcolors[4],
                    background=bgcolors[0],
                    padding=0,
                    fontsize = size,
                    ),
                ],
                27,
                background = bgcolors[0],
                margin = [0,mrg,mrg,mrg],
                border_color=bgcolors[0],
                border_width=9,
            ),
        ),
    ]

# Drag floating layouts.
mouse = [
        #Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
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
