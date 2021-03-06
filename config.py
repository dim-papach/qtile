# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
myBrowser = "firefox" # My browser of choice
myFileManager="pcmanfm"

keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod], "slash",
             lazy.spawn("rofi -show drun"),
             desc='Run Launcher'
             ),
         Key(["mod1"], "Tab",
             lazy.spawn("rofi -show window"),
             desc='Run Launcher'
             ),
         Key([mod], "f",
             lazy.spawn(myFileManager),
             desc='File Manager'
             ),
         Key([mod], "b",
             lazy.spawn(myBrowser),
             desc='Browser'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod], "t",
             lazy.spawn("systemctl suspend"),
             desc='Suspend'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key(["control", "shift"], "e",
             lazy.spawn("emacsclient -c -a emacs"),
             desc='Doom Emacs'
             ),
         Key(["mod1"], "Shift_L" ,
             lazy.widget['keyboardlayout'].next_keyboard()
             ),
         Key([mod, "shift"], "s",
             lazy.spawn("gnome-screenshot -a"),
             desc='Screenshot'
             ),
    ###XF86 KEYS
        Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
        Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
        Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),
        Key([], "XF86MonBrightnessDown",lazy.spawn("brightnessctl set 10%-")),
        Key([], "XF86MonBrightnessUp",lazy.spawn("brightnessctl set 10%+")),
        Key([], "XF86AudioPlay",lazy.spawn("playerctl play-pause")),
        Key([], "XF86AudioNext",lazy.spawn("playerctl next")),
        Key([], "XF86AudioPrev",lazy.spawn("playerctl previous")),
         ### Switch focus to specific monitor
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),

    ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),

    ### Treetab controls
          Key([mod, "shift"], "h",
             lazy.layout.move_left(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.move_right(),
             desc='Move down a section in treetab'
             ),

    ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),

    ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),

    # Emacs programs launched using the key chord CTRL+e followed by 'key'
         KeyChord(["control"],"e", [
             Key([], "e",
                 lazy.spawn("emacsclient -c -a 'emacs'"),
                 desc='Launch Emacs'
                 ),
             Key([], "b",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
                 desc='Launch ibuffer inside Emacs'
                 ),
             Key([], "d",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
                 desc='Launch dired inside Emacs'
                 ),
             Key([], "i",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),
                 desc='Launch erc inside Emacs'
                 ),
             Key([], "m",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(mu4e)'"),
                 desc='Launch mu4e inside Emacs'
                 ),
             Key([], "n",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
                 desc='Launch elfeed inside Emacs'
                 ),
             Key([], "s",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
                 desc='Launch the eshell inside Emacs'
                 ),
             Key([], "v",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
                 desc='Launch vterm inside Emacs'
                 ),


         ]),
]

############################################################################
# groups = [Group(i) for i in [                                            #
#     ("WWW",layout='monadtall'),                                          #
#     "CMD",                                                               #
#     "EDITOR1" ,                                                          #
#     "EDITOR2" ,                                                          #
#     "PDF",                                                               #
#     "FILES",                                                             #
#     "MUSIC",                                                             #
#     "CHAT",                                                              #
#     "GIT",                                                               #
# ]]                                                                       #
#                                                                          #
# for i, group in enumerate(groups):                                       #
#     actual_key = str(i + 1)                                              #
#     keys.extend([                                                        #
#         # Switch to workspace N                                          #
#         Key([mod], actual_key, lazy.group[group.name].toscreen()),       #
#         # Send window to workspace N                                     #
#         Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)) #
#     ])                                                                   #
############################################################################
group_names = [("WWW", {'layout': 'monadtall'}),
               ("TERM", {'layout': 'ratiotile'}),
               ("EDITOR1", {'layout': 'monadtall'}),
               ("EDITOR2", {'layout': 'monadtall'}),
               ("PDF", {'layout': 'treetab'}),
               ("FILES", {'layout': 'monadtall'}),
               ("MUSIC", {'layout': 'monadtall'}),
               ("CHAT", {'layout': 'monadtall'}),
               ("GIT", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = "1c1f24",
         active_bg = "c678dd",
         active_fg = "000000",
         inactive_bg = "a9a1e1",
         inactive_fg = "1c1f24",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus="#9ccfd8",
    border_normal="#31748f"
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

colors_morning = [["#161320"],#Flamingo 0
          ["#DDB6F2"], #Mauve 1
          ["#F5C2E7"], #Pink 2
          ["#E8A2AF"], #Maroon 3
          ["#F28FAD"], #Red 4
          ["#F8BD96"], #Peach 5
          ["#FAE3B0"], #Yellow 6
          ["#ABE9B3"], #Green 7
          ["#B5E8E0"], #Teal  8
          ["#96CDFB"], #Blue 9
          ]
colors_night = [["#161320"], #Black 0
          ["#1A1826"], #Black 1
          ["#1E1E2E"], #Black 2
          ["#302D41"], #Black 3
          ["#575268"], #Black 4
          ["#6E6C7E"], #Gray 0 5
          ["#988BA2"], #Gray 1 6
          ["#C3BAC6"], #Gray 2 7
          ["#D9E0EE"], #White 8
          ["#C9CBFF"], #Lavender 9
          ["#F5E0DC"],]#Rosewater 10

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize = 15,
    padding = 2,
    background=colors_night[4]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.Image(
                    filename = "~/.config/qtile/endeavouros-icon.png",
                    mouse_callbacks = {"Button1": lazy.spawn(".screenlayout/main_dualscreen.sh")},
                    scale = "False"
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.GroupBox(
                    active=colors_night[8],
                    rounded=False,
                    highlight_color=colors_night[5],
                    highlight_method="line",
                    borderwidth=0
                ),#!/usr/bin/env python3

                widget.WindowName(
                    # Make it transparent
                    foreground=colors_night[1]
                ),
                widget.TextBox(
                    text='???',
                    background=colors_night[4],
                    foreground=colors_morning[6],
                    padding=0,
                    fontsize=30
                ),
                widget.CurrentLayout(
                    foreground=colors_night[0],
                    background=colors_morning[6],
                ),
                widget.TextBox(
                    text='???',
                    foreground=colors_morning[4],
                    background=colors_morning[6],
                    padding=0,
                    fontsize=30
                ),
                widget.ThermalZone(
                    format="??? {temp}??C",
                    fgcolor_normal=colors_morning[0],
                    background=colors_morning[4],
                    zone="/sys/class/thermal/thermal_zone0/temp"
                ),
                widget.TextBox(
                    text='???',
                    foreground=colors_morning[7],                    background=colors_morning[4],                       padding=0,
                    fontsize=30
                ),
                widget.Memory(
                    format="???{MemUsed: .0f}{mm}",
                    background=colors_morning[7],
                    foreground=colors_morning[0],
                    interval=1.0
                ),
                widget.TextBox(
                    text='???',
                    background=colors_morning[7],
                    foreground=colors_morning[5],

                    padding=0,
                    fontsize=30
                ),
                widget.Net(
                    format="???  {down} ?????? {up}",
                    background=colors_morning[5],
                    foreground=colors_morning[0],
                    update_interval=1.0
                ),
                widget.TextBox(
                    text='???',
                    background=colors_morning[5],
                    foreground=colors_morning[8],
                    padding=0,
                    fontsize=30
                ),
                widget.TextBox(
                    text='???',
                    background=colors_morning[8],
                    foreground=colors_morning[0],
                    padding=7
                ),
                widget.Clock(
                    background=colors_morning[8],
                    foreground=colors_morning[0],
                    format="%H:%M - %d/%m/%Y",
                    update_interval=60.0
                ),
                widget.TextBox(
                    text='???',
                    foreground = colors_morning[4],
                    background = colors_morning[8],
                    padding = 0,
                    fontsize=30
                       ),
                widget.Volume(
                    foreground = colors_morning[0],
                    background = colors_morning[4],
                    fmt = '???? {}',
                    volume_app = 'pavucontrol',
                    mouse_callbacks = {
                    "Button2": lazy.spawn("pavucontrol"),
                       }),
                widget.TextBox(
                    text='???',
                    foreground = colors_night[7],
                    background = colors_morning[4],
                    padding = 0,
                    fontsize=30
                       ),
                widget.Backlight(
                    format = "??? {percent:2.0%}",
                    foreground = colors_night[0],
                    background = colors_night[7],
                    change_command = 'brightnessctl',
                    backlight_name = 'amdgpu_bl0',
                    mouse_callbacks = {
                    "Button1": lazy.spawn("brightnessctl s 0%"),
                    "Button2": lazy.spawn("brightnessctl s 50%"),
                    "Button3": lazy.spawn("brightnessctl s 100%"),
                    "Button4": lazy.spawn("brightnessctl s 5%+"),
                    "Button5": lazy.spawn("brightnessctl s 5%-"),
                                         },
                        ),

                widget.TextBox(
                    text='???',
                    background=colors_night[7],
                    foreground=colors_night[4],
                    padding=0,
                    fontsize=30
                ),
                widget.BatteryIcon(
                    format= "{percent:1.0%}"
                ),
                widget.Systray(),
                widget.Spacer(length = 2, background = colors_morning[0]),
                widget.KeyboardLayout(
                        background = colors_night[4],
                        foreground = colors_night[8],
                        configured_keyboards = ["us", "gr"],
                        update_interval = 1,
                        padding = 10
                       ),
        widget.QuickExit(
                    default_text="???",
                    fontsize=25,
                    foreground=colors_night[8],
                    timer_interval=0,
                    countdown_format="???"
                )
            ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[21:23]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=25),
                   wallpaper='~/Pictures/cloud-bg.png',
                   wallpaper_mode='stretch',
                    ),      
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=25),
                   wallpaper="/run/media/dp/Important/Wallpapers/wallpapers/os/arch-rainbow-1920x1080.png",
                   ),      
            ]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)
def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])
# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
