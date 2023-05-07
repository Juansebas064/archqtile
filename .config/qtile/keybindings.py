# Libraries needed
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.config import Key

# Variables for meta key and terminal
mod = "mod4"
terminal = guess_terminal()

def keybindings(): 
    return [
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
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Fullscreen a window"),
    # Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    # Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "space", lazy.layout.set_ratio(
        0.5), lazy.layout.normalize(), desc="Default ratio"),

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