python setup.py sdist bdist_wheel
python -m twine upload dist/*
./scripts/clean.ps1