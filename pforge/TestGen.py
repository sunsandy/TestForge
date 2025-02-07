import importlib
import sys
import os
from TestExpr import *
from params.DXGIFormats import *

def ParamToNameSegment(param, value):
    """Convert parameter value to test case name segment"""
    if param.Name == "BlendOp":
        return None
    elif param.Name == "Format":
        # Remove the DXGIFormat prefix and convert to lowercase
        name = str(value)
        if name.startswith("DXGIFormat."):
            name = name[len("DXGIFormat."):]
        return name.lower()
    elif param.Name == "MSAA":
        return f"aa{str(value)}"
    elif param.Name == "Width":
        return f"w{str(value)}"
    elif param.Name == "Height":
        return f"h{str(value)}"
    elif param.Name == "UserParams":
        return f"{str(value)}"
    else:
        raise ValueError(f"Unknown parameter: {param.Name}")

def ParamToArg(param, value):
    """Convert parameter value to C++ argument"""
    if param.Name == "BlendOp":
        return value
    elif param.Name == "Format":
        return f"DXGI::{str(value).split('.')[-1]}"
    elif param.Name == "MSAA":
        return f"{str(value)}"
    elif param.Name == "Width":
        return f"{str(value)}"
    elif param.Name == "Height":
        return f"{str(value)}"
    elif param.Name == "UserParams":
        return f"{str(value)}"
    else:
        raise ValueError(f"Unknown parameter: {param.Name}")

def TestArgsToName(prefix, nameSegments):
    majorPart = "_".join(nameSegment for nameSegment in nameSegments if nameSegment is not None)
    return f"{prefix}_{majorPart}"

def TestArgsToArgList(args):
    return ", ".join(f"{arg}" for arg in args)

def GenerateTests(expr, prefix, macro):
    if not isinstance(expr, Expr):
        raise ValueError(f"expr must be an instance of Expr but got {type(expr)}")

    testNames = [TestArgsToName(prefix, testArgs) for testArgs in GenerateCommands(expr, ParamToNameSegment)]
    testArgLists = [TestArgsToArgList(testArgs) for testArgs in GenerateCommands(expr, ParamToArg)]
    return [f"{macro}({name}, {argList});" for name, argList in zip(testNames, testArgLists)]

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
        module_name = f"plans.{module_name}"
    testPlan = importlib.import_module(module_name)
    
    if not hasattr(testPlan, "Tests"):
        raise ValueError("TestPlan must have a Tests attribute.")
    
    # Create output file path
    output_file = os.path.join(output_dir, f"{module_name.split('.')[-1]}_generated.cpp")
    
    with open(output_file, 'w') as f:
        for includeFile in testPlan.Tests.Cpp_IncludeFiles:
            f.write(f"#include \"{includeFile}\"\n")
        f.write("\n")
        testPlan.Tests.TestGen.UpdateId(0)
        f.write("\n".join(GenerateTests(testPlan.Tests.TestGen, testPlan.Tests.Cpp_CaseNamePrefix, testPlan.Tests.Cpp_TestGeneratorMacro)))
        f.write("\n")
