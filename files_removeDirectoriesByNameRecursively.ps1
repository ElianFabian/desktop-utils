# files_removeDirectoriesByNameRecursively.ps1

# https://stackoverflow.com/questions/3648142/how-can-i-recursively-delete-folder-with-a-specific-name-with-powershell

echo ''

$foldername = Read-Host 'Introduce the foldername you want to delete recursively: '

Get-Childitem -Include $foldername -Recurse -force | Remove-Item -Force -Recurse

echo ''