# My conky config

## Screenshots

![desktop_image_with_conky](https://github.com/Draune/conky-config/blob/master/screenshots/desktop_and_conky.png)

![conky_image](https://github.com/Draune/conky-config/blob/master/screenshots/conky.png)

## Requirements

You will need 'Cousine Nerd Font' and 'Symbols Nerd font Mono' installed in your /usr/share/fonts (just unzip them there and do `fc-cache -fv`).

You will also need wmctrl:

``` shell
sudo apt install wmctrl
```

## Install

To launch it, simply run (backup your .conky before):

``` shell
git clone https://github.com/Draune/conky-config.git ~/.conky
~/.conky/launch_conky.sh
```
