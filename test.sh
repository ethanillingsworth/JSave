echo "Installing modules"

python3 -m pip install pytest
poetry install

echo "Running Tests"

python3 -m pytest