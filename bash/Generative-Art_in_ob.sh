# /usr/bin/bash
# cd /root/temp/git_repos/open-brush/bash
# ./Generative-Art_in_ob.sh

function sendCommand {
  host_name=localhost
  curl --get --data-urlencode "$1" \
    -v http://$host_name:40074/api/v1
}

brushes=("Ink" "Light" "VelvetInk" "Icing" "Highlighter" "ShinyHull" "Spikes" "Highlighter")
# brushes=("Ink")

# script=Line_Walker
# script=Circular
# script=Line_Grid
# script=Magnetic_Flow
# script=Mosaic_Circles
script=Parallel_Lines

for str in ${brushes[@]}; do
  sendCommand "brush.type=$str"

  ssh root@localhost "cd /root/temp/git_repos/open-brush/python_scripts/Generative-Art && python3 $script.py >/dev/null 2>&1"
  
  # continue;

  ########################################
  # tail log file until a "Brush rotation" output is found due to a brush.debug issued when drawImage is complete
  ########################################
  echo "blocking on search for 'Brush rotation' (debug.brush) on logfile: /c/Users/Admin/AppData/LocalLow/Icosa/Open Brush/Player.log"
  ( tail -f -n0 "/c/Users/Admin/AppData/LocalLow/Icosa/Open Brush/Player.log" & ) | grep -q "Brush rotation"

  JPG_folder_name="C:/Users/Admin/Downloads/to_delete/open_brush/$script"
  if [ ! -d $JPG_folder_name ]; then
    mkdir -p $JPG_folder_name;
  fi
  file_num=$(echo $RANDOM | base64 | head -c 20; echo)

  ########################################
  # bring OpenBrush.exe window in FOCUS to FRONT and take SCREENSHOT
  ########################################
  cmd_string="C:\temp\git_repos\open-brush\powershell\take_ob_screenshot.ps1 ${JPG_folder_name}/${script}_${file_num}.JPG"
  powershell.exe $cmd_string

done
