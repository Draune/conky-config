import i3ipc
# Connexion à i3
i3 = i3ipc.Connection()

current_ws_file = open("/tmp/conky_current_ws", "w")

ws_files_prefix = "/tmp/conky_ws"
ws_files = []


for i in range(1, 10):
    ws_files.append(open(ws_files_prefix+str(i), "w"))
    ws_files[i-1].write(f"{i}:")

workspaces = i3.get_workspaces()
for ws in workspaces:
    if ws.focused:
        current_ws_file.write(f"{ws.num}")

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
        ws_files[window_workspace-1].write(char)

current_ws_file.close()
for f in ws_files:
    f.close()
