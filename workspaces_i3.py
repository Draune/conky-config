import i3ipc
i3 = i3ipc.Connection()

# Current workspace
current_ws_file = open("/tmp/conky_current_ws", "w")

workspaces = i3.get_workspaces()
for ws in workspaces:
    if ws.focused:
        current_ws_file.write(f"{ws.num}")

current_ws_file.close()

# Windows in each workspace
ws_files_prefix = "/tmp/conky_ws"
ws_files = []

# if you want to change the number of workspaces, change this variable
nb_workspaces=6

for i in range(1, nb_workspaces+1):
    ws_files.append(open(ws_files_prefix+str(i), "w"))
    # ws_files[i-1].write(f"{i}:")

icons_list = [["discord", ""],
              ["emacs", ""],
              ["firefox",""],
              ["xonsh", ""],
              ["gdb", ""],
              ["setting", ""],
              ["signal", "󰻞"],
              ["", ""]] # default

name_conky_window = "conky (debian)"

tree = i3.get_tree()
for window in tree.leaves():
    window_name = window.name.lower()
    num_workspace = window.workspace().num
    if (num_workspace > nb_workspaces or num_workspace < 0 or name_conky_window in window_name):
        continue

    for icon in icons_list:
        if icon[0] in window_name:
            if window.focused:
                ws_files[num_workspace-1].write(""+icon[1])
            else:
                ws_files[num_workspace-1].write(""+icon[1])
            break

for f in ws_files:
    f.close()
