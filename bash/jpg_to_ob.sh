# /usr/bin/bash
# cd /root/temp/git_repos/open-brush/bash
# ./jpg_to_ob.sh
# loop over JPG images deconstructed from GIF
  # /c/temp/to-delete/ffmpeg/gifs/subject/deconstructed/$i.JPG
  # cmd_string="C:\temp\git_repos\open-brush\powershell\take_ob_screenshot.ps1"

subject=pacman

if [ -d "/c/temp/to-delete/ffmpeg/gifs/$subject/deconstructed" ] 
then
    # for f in "/c/temp/to-delete/ffmpeg/gifs/$subject/deconstructed/*.jpg";
    for f in `ls /c/temp/to-delete/ffmpeg/gifs/$subject/deconstructed/*.jpg | sort -g`;
    do
      filename=$(basename -- "$f")
      extension="${filename##*.}"
      filename="${filename%.*}"

      ########################################
      # convert JPG to OB JPG; vb_path is for path in VirtualBox
      ########################################
      vb_path="${f/\/c/\/root}"
      echo "converting $vb_path to OB JPG"
      # ssh root@localhost "python3 /root/temp/git_repos/open-brush/python_scripts/image_art.py drawImage /root/temp/to-delete/ffmpeg/gifs/simple_eye_blink/deconstructed/e001.jpg"
      ssh root@localhost "python3 /root/temp/git_repos/open-brush/python_scripts/image_art.py drawImage $vb_path"
      # call python_scripts/image_art.py drawImage() "$vb_path"


      ########################################
      # tail log file until a "Brush rotation" output is found due to a brush.debug issued when drawImage is complete
      ########################################
      echo "blocking on search for 'Brush rotation' (debug.brush) on logfile: /c/Users/Admin/AppData/LocalLow/Icosa/Open Brush/Player.log"
      ( tail -f -n0 "/c/Users/Admin/AppData/LocalLow/Icosa/Open Brush/Player.log" & ) | grep -q "Brush rotation"

      ########################################
      # bring OpenBrush.exe window in FOCUS to FRONT and take SCREENSHOT
      ########################################
      cmd_string="C:\temp\git_repos\open-brush\powershell\take_ob_screenshot.ps1 C:\temp\to-delete\ffmpeg\gifs\\$subject\ob\\$filename.JPG"
      powershell.exe $cmd_string


    done
else
    echo "Error: Directory /c/temp/to-delete/ffmpeg/gifs/$subject/deconstructed does not exist."
fi

