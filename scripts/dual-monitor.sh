source=$(xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}')

if [ $source = 'HDMI-1' ]
then   
    xrandr --output eDP-1 --mode 1368x768 --pos 1368x0 --output HDMI-1 --auto --above eDP-1
    qtile cmd-obj -o cmd -f restart
    cp ~/archqtile/scripts/bg-saved.cfg ~/archqtile/.config/nitrogen
    nitrogen --restore
else
    xrandr -s 1368x768 --output HDMI-1 --off
    qtile cmd-obj -o cmd -f restart
    cp ~/archqtile/scripts/bg-saved.cfg ~/archqtile/.config/nitrogen
    nitrogen --restore
fi
