# /usr/bin/bash
# cd /root/temp/git_repos/open-brush/bash
# ./delaunay.sh

if [ 1==1 ] 
then
    for i in {11..20}
    do
      filename=$(basename -- "$f")
      extension="${filename##*.}"
      filename="${filename%.*}"

      ########################################
      # convert JPG to OB JPG; vb_path is for path in VirtualBox
      ########################################
      # ssh root@localhost "python3 /root/temp/git_repos/open-brush/python_scripts/image_art.py drawImage /root/temp/to-delete/ffmpeg/gifs/simple_eye_blink/deconstructed/e001.jpg"
      ssh root@localhost "docker exec -i python3.8.10 bash '/root/delaunay.sh'"

      ########################################
      # tail log file until a "Brush rotation" output is found due to a brush.debug issued when drawImage is complete
      ########################################
      echo "blocking on search for 'Brush rotation' (debug.brush) on logfile: /c/Users/Admin/AppData/LocalLow/Icosa/Open Brush/Player.log"
      ( tail -f -n0 "/c/Users/Admin/AppData/LocalLow/Icosa/Open Brush/Player.log" & ) | grep -q "Brush rotation"

      ########################################
      # bring OpenBrush.exe window in FOCUS to FRONT and take SCREENSHOT
      ########################################
      cmd_string="C:\temp\git_repos\open-brush\powershell\take_ob_screenshot.ps1 C:\temp\to-delete\ffmpeg\gifs\\hal_head\\$i.JPG"
      powershell.exe $cmd_string

    done
else
    echo "Error: "
fi

