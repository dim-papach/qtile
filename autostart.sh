#!/bin/sh
picom --config ~/.config/picom/picom.conf --experimental-backends --vsync &
xfce4-power-manager --daemon &
dunst -conf ~/.config/dunst/dunstrc &
nm-applet &
blueberry-tray &
/usr/bin/emacs --daemon &
