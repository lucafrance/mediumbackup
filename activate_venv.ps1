# Move to the folder where the script is located
# https://stackoverflow.com/a/4724421
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
cd $dir

# Activate the Python virtual environment
./venv/Scripts/Activate.ps1