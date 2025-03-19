#!/bin/bash
echo "Building the application..."

echo "Creating virtual environment..."
python3 -m venv venv

source venv/bin/activate

echo "Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Build completed successfully!"

