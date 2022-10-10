# https://community.idera.com/database-tools/powershell/powertips/b/tips/posts/bringing-window-in-the-foreground
function Show-Process($Process, [Switch]$Maximize)
{
  $sig = '
    [DllImport("user32.dll")] public static extern bool ShowWindowAsync(IntPtr hWnd, int nCmdShow);
    [DllImport("user32.dll")] public static extern int SetForegroundWindow(IntPtr hwnd);
  '
  
  if ($Maximize) { $Mode = 3 } else { $Mode = 4 } 
  $type = Add-Type -MemberDefinition $sig -Name WindowAPI -PassThru
  $hwnd = $process.MainWindowHandle
  $null = $type::ShowWindowAsync($hwnd, $Mode)
  $null = $type::SetForegroundWindow($hwnd) 

}

# https://gist.github.com/eonarheim/c75fedbf21fa4c06d49817b2f3082799
[Reflection.Assembly]::LoadWithPartialName("System.Drawing")
function screenshot([Drawing.Rectangle]$bounds, $path) {
  $bmp = New-Object Drawing.Bitmap $bounds.width, $bounds.height
  $graphics = [Drawing.Graphics]::FromImage($bmp)

  $graphics.CopyFromScreen($bounds.Location, [Drawing.Point]::Empty, $bounds.size)

  try {
    Write-Host $path
    $bmp.Save($path,[Drawing.Imaging.ImageFormat]::Jpeg)
  } catch {
    $_
  }

  $graphics.Dispose()
  $bmp.Dispose()
}

$OpenBrush = Get-Process OpenBrush
Show-Process -Process $OpenBrush

# $screens = [Windows.Forms.Screen]::AllScreens
# $width  = ($screens.Bounds.Right  | Measure-Object -Maximum).Maximum
# $height = ($screens.Bounds.Bottom | Measure-Object -Maximum).Maximum

# https://stackoverflow.com/questions/27791783/powershell-unable-to-find-type-system-windows-forms-keyeventhandler
# [void] [System.Reflection.Assembly]::LoadWithPartialName("System.Drawing") 
# [void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms") 
# $Screen = [System.Windows.Forms.SystemInformation]::VirtualScreen
# $Width = $Screen.Width
# $Height = $Screen.Height
# Write-Output $Width
# Write-Output $Height

$Width = 1920;
$Height = 1080;

# $Width = 2736;
# $Height = 1834;

$bounds = [Drawing.Rectangle]::FromLTRB(0, 0, $Width, $Height)

$screenshot_filename = "c:\temp\screenshot.JPG"
Write-Host $args[0]
# if ($args.Count > 0) {
if (!($args[0] -eq $null)) {
  $screenshot_filename = $args[0]
}
screenshot $bounds $screenshot_filename
