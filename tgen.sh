#!/bin/bash

# Create CppTests directory if it doesn't exist
mkdir -p CppTests

# Generate tests for each test plan
for test_plan in pforge/plans/*.py; do
    if [ -f "$test_plan" ] && [ "$(basename "$test_plan")" != "__init__.py" ]; then
        echo "Generating tests for $test_plan..."
        python tgen.py "$test_plan" CppTests
    fi
done
