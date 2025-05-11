import subprocess

# Current workspace
current_ws_file = open("/tmp/conky_current_ws", "w")

output = subprocess.check_output(["wmctrl", "-d"]).decode()
output = output.split("\n")
for line in output:
    line = line.split()
    if line[1] == "*":
        current_ws_file.write(str(int(line[0])+1))
        break

current_ws_file.close()

# Windows in each workspace
ws_files_prefix = "/tmp/conky_ws"
ws_files = []

# if you want to change the number of workspaces, change this variable
nb_workspaces=9

for i in range(1, nb_workspaces+1):
    ws_files.append(open(ws_files_prefix+str(i), "w"))
    ws_files[i-1].write(f"{i}:")

icons_list = [["discord", ""],
              ["emacs", ""],
              ["firefox",""],
              ["", ""]] # default

output = subprocess.check_output(["wmctrl", "-l"]).decode()
output = output.split("\n")
for line in output:
    if line.strip() == "":
        break
    window_name = line.lower()
    line = line.split()
    num_workspace = int(line[1])
    if (num_workspace > nb_workspaces or num_workspace < 0):
        continue

    for icon in icons_list:
        if icon[0] in window_name:
            ws_files[num_workspace].write(" "+icon[1])
            break


for f in ws_files:
    f.close()
