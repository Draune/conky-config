#!/bin/bash

killall conky

conky -c ~/.conky/net_down_panel &
conky -c ~/.conky/net_up_panel &
conky -c ~/.conky/time_panel &
conky -c ~/.conky/date_panel &
conky -c ~/.conky/cpu_panel &
conky -c ~/.conky/mem_panel &
conky -c ~/.conky/disk_panel &
conky -c ~/.conky/battery_panel &
conky -c ~/.conky/ws1_panel &
conky -c ~/.conky/ws2_panel &
conky -c ~/.conky/ws3_panel &
conky -c ~/.conky/ws4_panel &
conky -c ~/.conky/ws5_panel &
conky -c ~/.conky/ws6_panel &
# Reduced the number off visible workspaces since I never use more than 6
# conky -c ~/.conky/ws7_panel &
# conky -c ~/.conky/ws8_panel &
# conky -c ~/.conky/ws9_panel &
