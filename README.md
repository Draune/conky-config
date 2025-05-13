# My conky config

## Screenshots

![desktop_image_with_conky](https://github.com/Draune/conky-config/blob/master/screenshots/desktop_and_conky.png)

![conky_image](https://github.com/Draune/conky-config/blob/master/screenshots/conky.png)

## Scripts for workspaces

To use the script for workspace for another X server wm you need to change `workspaces_i3.py` to `workspaces.py` in `ws1_panel`.

If you want to use more than 6 workspaces, change the script's `nb_workspaces` variable.

For i3 users who are not on debian, you'll probably want to change the `name_conky_window` variable so it will not display the conkys window in the workspaces.

## Requirements

You will need 'Cousine Nerd Font' and 'Symbols Nerd font Mono' installed in your /usr/share/fonts (just unzip them there and do `fc-cache -fv`).

You will also need i3ipc or  wmctrl:

``` shell
# for i3 wm
pip install i3ipc

# for non other wm
sudo apt install wmctrl
```

## Install

To launch it, simply run (backup your .conky before):

``` shell
git clone https://github.com/Draune/conky-config.git ~/.conky
~/.conky/launch_conky.sh
```
