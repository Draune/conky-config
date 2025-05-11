import i3ipc
# Connexion à i3
i3 = i3ipc.Connection()

current_ws = open("/tmp/conky_current_ws", "w")

ws_file = "/tmp/conky_ws"
ws = []


for i in range(1, 10):
    ws.append(open(ws_file+str(i), "w"))
    ws[i-1].write(f"{i}:")

workspaces = i3.get_workspaces()
for ws_ in workspaces:
    if ws_.focused:
        current_ws.write(f"{ws_.num}")

tree = i3.get_tree()
char = ""
for window in tree.leaves():
    if "discord" in window.name.lower():
        char = " "
    elif "emacs" in window.name.lower():
        char = " "
    elif "firefox" in window.name.lower():
        char = " "
    elif "conky" in window.name.lower():
        char = ""
    else:
        char = " "
    window_workspace = window.workspace().num
    if window_workspace  < 10:
        ws[window_workspace-1].write(char)

current_ws.close()
for f in ws:
    f.close()
