# Syntax
<#
for (variable = value; condition for counting; increase/decease value) {
    command to repeat 
}
#>

$MyArray = @("Reaper", "Warrior", "Paladin")
for ($i = 0; $i -lt $MyArray.Count ++; $i ++) {
    echo ("Element $i value: " + $MyArray[$i])
}