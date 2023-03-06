# Syntax
<#
for (variable = value; condition for counting; increase/decease value) {
    command to repeat 
}
#>
$MyArray = @("bmw", "lexus", "ferrai", "nissan")
for ($i = 0; $i -lt $MyArray.Count; $i ++){
    Write-Output ("Element: $i Value:" + $MyArray[$i])
}
                                                    


                                                    