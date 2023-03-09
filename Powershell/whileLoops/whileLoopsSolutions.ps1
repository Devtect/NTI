# Solution number 1
$i = 1
while ($i -le 5) {
    Write-Output $i
    $i++
}

# Solution number 2
$word = ''
while ($word -ne 'quit') {
    $word = Read-Host "Enter a word (or 'quit' to exit)"
}
Write-Output "Exiting..."


# Solution number 3
$target = 7
$num = 0
while ($num -ne $target) {
    $num = Get-Random -Minimum 1 -Maximum 11
    Write-Output "Generated number: $num"
}
Write-Output "Match found!"

# Solution number 4
$i = 0
$sum = 0
while ($i -lt 10) {
    $i++
    if ($i % 2 -eq 0) {
        $sum += $i
    }
}
Write-Output "The sum of the first 10 even numbers is $sum"


# Solution number 5
$i = 0
$letters = 'a','b','c','d','e'
while ($i -lt 5) {
    Write-Output $letters[$i]
    $i++
}
