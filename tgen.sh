#!/bin/bash

# Create CppTests directory if it doesn't exist
mkdir -p CppTests

# Generate tests for each test plan
for test_plan in pforge/plans/*.py; do
    base_name=$(basename "$test_plan")
    if [ -f "$test_plan" ] && [ "$base_name" != "__init__.py" ] && [ "$base_name" != "Demo.py" ]; then
        echo "Generating tests for $test_plan..."
        python pforge/TestGen.py "$test_plan" CppTests/TestSamples
    fi
done
