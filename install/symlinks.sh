cd ~
rm -r ~/.fonts ~/.icons ~/.themes 
rm -r ~/.config/{alacritty,gtk-2.0,gtk-3.0,nitrogen,nvim,picom,qtile,Thunar,xfce4}


ln -s ~/archqtile/.config/alacritty/ ~/.config/
ln -s ~/archqtile/.config/gtk-2.0/ ~/.config/
ln -s ~/archqtile/.config/gtk-3.0/ ~/.config
ln -s ~/archqtile/.config/nitrogen ~/.config
ln -s ~/archqtile/.config/nvim ~/.config
ln -s ~/archqtile/.config/picom/ ~/.config
ln -s ~/archqtile/.config/qtile/ ~/.config
ln -s ~/archqtile/.config/Thunar/ ~/.config
ln -s ~/archqtile/.config/xfce4/ ~/.config/

ln -s ~/archqtile/.fonts/ ~
ln -s ~/archqtile/.icons/ ~
ln -s ~/archqtile/.themes/ ~


