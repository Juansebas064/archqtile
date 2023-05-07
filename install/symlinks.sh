cd ~
rm -r ~/.fonts ~/.icons ~/.themes 
rm -r ~/.config/{alacritty,gtk-2.0,gtk-3.0,nitrogen,nvim,picom,qtile,Thunar,xfce4,ulauncher, libinput-gestures.conf}


ln -s ~/archqtile/.config/alacritty/ ~/.config/
ln -s ~/archqtile/.config/gtk-2.0/ ~/.config/
ln -s ~/archqtile/.config/gtk-3.0/ ~/.config
ln -s ~/archqtile/.config/nitrogen ~/.config
ln -s ~/archqtile/.config/nvim ~/.config
ln -s ~/archqtile/.config/picom/ ~/.config
ln -s ~/archqtile/.config/qtile/ ~/.config
ln -s ~/archqtile/.config/Thunar/ ~/.config
ln -s ~/archqtile/.config/xfce4/ ~/.config/
ln -s ~/archqtile/.config/ulauncher ~/.config
ln -s ~/archqtile/.config/libinput-gestures.conf ~/.config

ln -s ~/archqtile/.fonts/ ~
ln -s ~/archqtile/.icons/ ~
ln -s ~/archqtile/.themes/ ~

sudo cp ~/archqtile/30-touchpad.conf /etc/X11/xorg.conf.d/
#sudo cp ~/archqtile/20-intel.conf /etc/X11/xorg.conf.d/
sudo cp ~/archqtile/lightdm.conf /etc/lightdm/ 
sudo cp ~/archqtile/lightdm-webkit2-greeter.conf /etc/lightdm/
sudo mkdir /usr/share/backgrounds/ 
sudo cp ~/archqtile/login.jpg /usr/share/backgrounds/

cp -r ~/archqtile/.local/ ~

