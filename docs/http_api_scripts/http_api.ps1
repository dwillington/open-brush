if($args.Count -eq 0) {
  Write-Output "usage e.g.: http_api.ps1 london_maps.txt "
  return
}

$file_name=$args[0]

ForEach ($line in Get-Content $file_name) {
  if ($line) { # NOT EMPTY
    # Write-Output $line
    Invoke-WebRequest $line | Out-Null
  } 
  # break
}
