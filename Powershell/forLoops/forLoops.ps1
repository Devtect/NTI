# Syntax
<#
for (variable = value; condition for counting; increase/decease value) {
    command to repeat 
}
#>
$MyArray = @("benji", "oliver", "kaihan", "piotr")
for ($i = 0; $i -lt $MyArray.Count; $i ++){
    Write-Output ("Element: $i Value:" + $MyArray[$i])
}
                                                    


                                                    