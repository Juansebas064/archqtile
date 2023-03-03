source=$(xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}')

if [ $source = 'HDMI1' ]
then   
    xrandr --output eDP1 --mode 1368x768 --pos 1368x0 --output HDMI1 --auto --above eDP1
    qtile cmd-obj -o cmd -f restart
    nitrogen --restore
else
    xrandr -s 1368x768 
    qtile cmd-obj -o cmd -f restart
    nitrogen --restore
fi

nitrogen --restore
#picom --experimental-backends &
