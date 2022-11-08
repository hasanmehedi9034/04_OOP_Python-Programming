import shutil
 
with open("center_align.txt", "r") as f:
  lines = f.readlines()
  
for line in lines:
  print(line.center(shutil.get_terminal_size().columns))
        