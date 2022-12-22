# /usr/bin/bash
# cd /root/temp/git_repos/open-brush/bash
# ./delaunay.sh

fs_image="/root/temp/tmp/background.jpg"
python_scripts_folder="/root/temp/git_repos/generative_art/python_scripts/"

delaunay_cmds=(
"delaunay.py -n 1000 -i ${fs_image}"
# "delaunay.py -n 500 -i ${fs_image} --lines --linecolor 000000"
)

triangular_cmds=(
"-m triangler --sample POISSON_DISK -p 1536 ${fs_image} "
)

if [ 1==1 ] 
then
    filename=$(basename -- "$f")
    extension="${filename##*.}"
    filename="${filename%.*}"

    # for cmd in "${delaunay_cmds[@]}"; do
      # sh -c "cd ${python_scripts_folder}/delaunay; python ${cmd}"
    # done

    # for cmd in "${triangular_cmds[@]}"; do
      # sh -c "cd ${python_scripts_folder}/triangler; python ${cmd}"
    # done

    for i in {1..10}
    do
      # cmd="cd ${python_scripts_folder}/delaunay;python ${delaunay_cmds[0]}"
      cmd="cd ${python_scripts_folder}/triangler;python ${triangular_cmds[0]}"
      sh -c "$cmd"
      
      # tail log file until a "Brush rotation" output is found due to a brush.debug issued

      # echo "blocking on search for 'Brush rotation' (debug.brush) on logfile: /mnt/c/Users/Admin/AppData/LocalLow/Icosa/Open Brush/Player.log"
      # ( tail -f -n0 "/mnt/c/Users/Admin/AppData/LocalLow/Icosa/Open Brush/Player.log" & ) | grep -q "Brush rotation"
      
      sleep 70s

      ########################################
      # bring OpenBrush.exe window in FOCUS to FRONT and take SCREENSHOT
      ########################################
      JPG_folder_name="C:/temp/to-delete/ffmpeg/gifs/fs"
      # cmd_string="C:\temp\git_repos\open-brush\powershell\take_ob_screenshot.ps1 ${JPG_folder_name}/fs_${i}.JPG"

      # WSL UBUNTU WSL UBUNTU WSL UBUNTU WSL UBUNTU WSL UBUNTU WSL UBUNTU WSL UBUNTU WSL UBUNTU WSL UBUNTU 
      "/mnt/c/Windows/System32/WindowsPowerShell/v1.0//powershell.exe" "C:\temp\git_repos\open-brush\powershell\take_ob_screenshot.ps1 ${JPG_folder_name}/fs_${i}.JPG"

    done


else
    echo "Error: "
fi

