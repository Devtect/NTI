# Solution to 1
for ($i=1; $i -le 10; $i++) {
    Write-Output $i
}

# Solution to 2
for ($i=1; $i -le 20; $i++) {
    if ($i % 2 -eq 0) {
        Write-Output $i
    }
}

# Solution to 3
$files = Get-ChildItem -Path "C:\Users\user\Documents"
for ($i=0; $i -lt $files.Count; $i++) {
    Write-Output $files[$i].Name
}

# Solution to 4
$files = Get-ChildItem -Path "C:\Users\user\Downloads" -Filter "*.pdf"
$dest = "C:\Users\user\Documents\Pdfs"
for ($i=0; $i -lt $files.Count; $i++) {
    Copy-Item $files[$i].FullName $dest
}

# Solution to 5
$names = "jason", "james", "francis", "veronica"
for ($i=0; $i -lt $names.Count; $i++) {
    $names[$i] = $names[$i].ToUpper()
}
Write-Output $names

