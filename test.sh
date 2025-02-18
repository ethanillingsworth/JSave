echo "Installing modules"

python3 -m pip install pytest
python3 -m pip install colorxs
python3 -m pip install cryptography

echo "Running Tests"

python3 -m pytest