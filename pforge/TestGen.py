from .TestExpr import *
from .params.DXGIFormats import *

def GenerateTestsCode(test_cases, prefix, macro):
    for test_case_param_args in test_cases:
        print(test_case_param_args)
        test_name_parts = list(pa.param.ToTestNamePart(pa.value) for pa in test_case_param_args)
        print(test_name_parts)
        test_name = "_".join(part for part in test_name_parts if part)
        print(test_name)

        test_args = list(pa.param.ToArg(pa.value) for pa in test_case_param_args)
        test_arg_list = ", ".join(test_args)

        yield f"{macro}({prefix}{test_name}, {test_arg_list});"
