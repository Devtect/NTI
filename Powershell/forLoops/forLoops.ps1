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
                                                    


$Numbers = @("1", "2", "3", "4") 
# Figure out how to use "null" so the index starts from 1
for ($i = 0; $i -lt 4; $i ++) {
    Write-Output ("Element: $i Value:" + $Numbers[$i])
}