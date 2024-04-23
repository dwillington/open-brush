
$file_name=$args[0]

ForEach ($line in Get-Content $file_name) {
  # Write-Output $line
  Invoke-WebRequest $line | Out-Null
  # break
}
