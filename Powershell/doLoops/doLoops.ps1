<#
do {
    operation
} while (condition)
#>

<#
do {
    operation
} until (condition)
#>

# condition check is completed at the end of the loop


# the check is completed at the beginning of the loop
while($i -lt 5) {
    $i++
}
Write-Output "Value of i: $i"

<# 
does not do the same thing, because $i is 
already less than 5 from the start of the code
#>
