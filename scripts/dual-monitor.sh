source=$(xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}')

if [ $source = 'HDMI1' ]
then   
    xrandr --output eDP1 --mode 1368x768 --pos 1368x0 --output HDMI1 --auto --above eDP1
    cp ~/archqtile/scripts/bg-saved.cfg ~/archqtile/.config/nitrogen/
    qtile cmd-obj -o cmd -f restart
    nitrogen --restore
else
    xrandr -s 1368x768 --output HDMI1 --off
    qtile cmd-obj -o cmd -f restart
    nitrogen --set-auto ~/archqtile/snow.jpg
fi
