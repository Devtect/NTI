while ($userinput -ne "quit"){
    $userinput = Read-Host "Type 'yes' if you love powershell(type quit to exit)"

    if($userinput -eq "yes") {Write-Output "You are getting an A!"}
    elseif ($userinput -eq "no") {Write-Output "You are getting an F!"}
}
$userinput = $null