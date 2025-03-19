#!/bin/bash
echo "Running tests..."

if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found. Please create the virtual environment first by running build.sh."
    exit 1
fi

echo "Running unit and integration tests..."
pytest --maxfail=1 --disable-warnings -q

if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Some tests failed."
    exit 1
fi

