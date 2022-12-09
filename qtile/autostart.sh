function run {
	if ! pgrep $1 ;
	then
		$@&
	fi
}

run nm-applet &
run volumeicon &
run xfce4-clipman &

