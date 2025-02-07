
import importlib
import sys
import os
import pforge
from pforge.TestExpr import TestDescriptor, FindTestDescriptor
from pforge.TestGen import GenerateTestsCode, GenerateList
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python tgen.py <test_plan_module> <output_dir>")
        sys.exit(1)

    test_plan_module = sys.argv[1]
    output_dir = sys.argv[2]
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Add the current directory to Python path
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    # Import the test plan module
    module_name = os.path.splitext(os.path.basename(test_plan_module))[0]
    if test_plan_module.startswith('pforge/plans/'):
        module_name = f"pforge.plans.{module_name}"
    testPlan = importlib.import_module(module_name)
    test_desc: TestDescriptor = FindTestDescriptor(testPlan)

    # Create output file path
    output_file = os.path.join(output_dir, f"{module_name.split('.')[-1]}_generated.cpp")
    
    with open(output_file, 'w') as f:
        for includeFile in test_desc.Cpp_IncludeFiles:
            f.write(f"#include \"{includeFile}\"\n")
        f.write("\n")
        test_desc.TestGen.UpdateId(0)
        test_cases = list(GenerateList(test_desc.TestGen))
        f.write("\n".join(GenerateTestsCode(test_cases, test_desc.Cpp_CaseNamePrefix, test_desc.Cpp_TestGeneratorMacro)))
        f.write("\n")
