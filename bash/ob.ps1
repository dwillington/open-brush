# Write-Host ">>$($args[0])"
$Parameters = [uri]::EscapeDataString($args[0])
# $Parameters = [System.Net.WebUtility]::UrlEncode($args[0])
Invoke-WebRequest -UseBasicParsing -Method Post -Uri "http://localhost:40074/api/v1" -Body $Parameters
