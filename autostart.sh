#!/bin/sh
xinput --map-to-output 'ELAN2514:00 04F3:2B0E' eDP &
xinput --map-to-output 'ELAN2514:00 04F3:2B0E Stylus Pen (0)' eDP &
xinput --map-to-output 'ELAN2514:00 04F3:2B0E Stylus Eraser (0)' eDP &
picom --config ~/.config/picom/picom.conf --experimental-backends --vsync &
dunst -conf ~/.config/dunst/dunstrc &
nm-applet &
blueberry-tray &
/usr/bin/emacs --daemon &
setxkbmap -layout "us,gr" -option "grp:alt_shift_toggle"
