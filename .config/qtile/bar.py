from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy


mrg=5

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
        4:'#894bb3',
        5:'#ffffff'
        }

def laptop_bar():
    return [
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


                widget.TextBox(
                    text="-",
                    padding=3,
                    foreground= bgcolors[0],
                    ),

                #System tray
                widget.Systray(padding=4),


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


                #Widget for battery level
                 widget.TextBox(
                    text=left,
                    background=bgcolors[0],
                    foreground=bgcolors[4],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),
                # widget.Battery(
                #     font=symbols_font,
                #     fontsize=13,
                #     full_char='',
                #     discharge_char='',
                #     charge_char='',
                #     format='{char}',
                #     low_foreground=bgcolors[0],
                #     foreground=bgcolors[0],
                #     background=bgcolors[4],
                #     update_interval=5,
                #     padding=5,
                # ),
                widget.BatteryIcon(
                    theme_path = '~/.icons/Colloid-teal-dark/status/24/',
                    scale=1,
                    background=bgcolors[4],
                ),
                widget.TextBox(
                    background=bgcolors[4],
                    foreground=bgcolors[4],
                    text='',
                    padding=0,
                ),
                widget.Battery(
                    format='{percent:2.0%}',
                    fontsize=laptop_fontsize,
                    low_foreground=bgcolors[0],
                    foreground=bgcolors[5],
                    background=bgcolors[4],
                    update_interval=5,
                    padding=4,
                ),

                 widget.TextBox(
                    text=right,
                    background=bgcolors[0],
                    foreground=bgcolors[4],
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
                    foreground=bgcolors[2],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    mouse_callbacks = {
                        "Button2": lazy.spawn("pavucontrol")
                    },
                    ),
                widget.Volume(
                    theme_path = '~/.icons/Colloid-teal-dark/status/24/',
                    background=bgcolors[2],
                    foreground=bgcolors[5],
                    padding=1,
                    fontsize = 19,
                    font=symbols_font,
                    update_interval=0.1,
                    mouse_callbacks = {
                        "Button2": lazy.spawn("pavucontrol")
                    },
                    ),
                widget.Volume(
                    font=symbols_font,
                    background = bgcolors[2],
                    foreground = bgcolors[5],
                    padding = 0,
                    mouse_callbacks = {
                        "Button2": lazy.spawn("pavucontrol")
                    },
                    ),
                widget.TextBox(
                    text=right,
                    background=bgcolors[0],
                    foreground=bgcolors[2],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    mouse_callbacks = {
                        "Button2": lazy.spawn("pavucontrol")
                    },
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
                    padding=6,
                    foreground=bgcolors[5],
                    background=bgcolors[1],
                ),
                widget.Clock(
                    format="%d/%m/%Y",
                    mouse_callbacks = {
                        "Button1": lazy.spawn("gsimplecal")
                    },
                    foreground=bgcolors[5],
                    background=bgcolors[1],
                    padding=5,
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
                ],
                22,
                background = bgcolors[0],
                margin = 0,
                border_color=bgcolors[0],
                border_width=6,
            ),
        ),
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


                #Widget for battery level
                 widget.TextBox(
                    text=left,
                    background=bgcolors[0],
                    foreground=bgcolors[4],
                    padding=0,
                    fontsize = size,
                    font=symbols_font,
                    ),
                # widget.Battery(
                #     font=symbols_font,
                #     fontsize=13,
                #     full_char='',
                #     discharge_char='',
                #     charge_char='',
                #     format='{char}',
                #     low_foreground=bgcolors[0],
                #     foreground=bgcolors[0],
                #     background=bgcolors[4],
                #     update_interval=5,
                #     padding=5,
                # ),
                widget.BatteryIcon(
                    theme_path = '~/.icons/Colloid-teal-dark/status/24/',
                    scale=1,
                    background=bgcolors[4],
                ),
                widget.TextBox(
                    background=bgcolors[4],
                    foreground=bgcolors[4],
                    text='',
                    padding=0,
                ),
                widget.Battery(
                    format='{percent:2.0%}',
                    fontsize=laptop_fontsize,
                    low_foreground=bgcolors[0],
                    foreground=bgcolors[5],
                    background=bgcolors[4],
                    update_interval=5,
                    padding=4,
                ),
                 widget.TextBox(
                    text=right,
                    background=bgcolors[0],
                    foreground=bgcolors[4],
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
                    mouse_callbacks = {
                        "Button2": lazy.spawn("pavucontrol")
                    },
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
                ],
                22,
                background = bgcolors[0],
                margin = 0,
                border_color=bgcolors[0],
                border_width=6,
            ),
        ),
    ]

def desktop_bar():
    return [

    ]
