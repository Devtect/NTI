$MyArray = @("Reaper", "Warrior", "Paladin")
for ($i = 0; $i -lt $MyArray.Count; $i ++) {
    echo ("Element $i value: " + $MyArray[$i])
}