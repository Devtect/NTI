# Solution to exercise nr1
<#$i = 1
do {
    Write-Host $i
    $i++
} while ($i -le 10)

# Solution to exercise nr2
$i = 1
do {
    Write-Host $i
    $i++
} while ($i -le 20)

# Solution to exercise nr3
$i = 1
$sum = 0
do {
    $sum += $i
    $i++
} while ($i -le 100)
write-host $sum

# Solution to exercise nr4
do {
    $num = Read-Host "Enter a number between 1 and 10:"
} until ([int]$num -ge 1 -and [int]$num -le 10)

Write-Host "You entered $num."
#>
$n1 = 0
$n2 = 1
$i = 1

do {
    Write-Host $n1
    $n3 = $n1 + $n2
    $n1 = $n2
    $n2 = $n3
    $i++
} while ($i -le 10)




