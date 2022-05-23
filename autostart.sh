#!/bin/sh
setxkbmap -option "grp:alt_shift_toggle" "us,gr"
picom --config ~/.config/picom/picom.conf --experimental-backends --vsync &
dunst -conf ~/.config/dunst/dunstrc &
nm-applet &
blueberry-tray &
/usr/bin/emacs --daemon &
