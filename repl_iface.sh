IFACE=$(ip route | grep '^default' | awk '{print $5}')

if grep -q "\b$IFACE\b" ~/.conky/net_down_panel; then
    exit
fi

sed -i "s/\(downspeedgraph \|downspeedf \|upspeedgraph \|upspeedf \)[a-zA-Z0-9]\+/\1$IFACE/g" ~/.conky/net_down_panel
sed -i "s/\(downspeedgraph \|downspeedf \|upspeedgraph \|upspeedf \)[a-zA-Z0-9]\+/\1$IFACE/g" ~/.conky/net_up_panel
