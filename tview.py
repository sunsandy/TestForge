from flask import Flask, render_template, jsonify, g
import json
import importlib.util
import sys
from pathlib import Path
import os
from pforge.TestExpr import Param, Cross, Union, TestDescriptor, FindTestDescriptor, PVPair
from pforge.TestGen import GenerateList, GenerateTestsCode

os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_DEBUG'] = '1'

app = Flask(__name__, template_folder='pforge_view/templates')


class TestLoader:
    def __init__(self):
        self.loaded_modules = {}
        
    def load_module(self, module_name, file_path):
        """Load a Python module from file path"""
        if module_name in self.loaded_modules:
            return self.loaded_modules[module_name]
            
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        self.loaded_modules[module_name] = module
        return module

    def load_test_modules(self, test_file):
        """Load all required modules for a test file"""
        # Load the test file
        test_module_name = Path(test_file).stem
        test_module = self.load_module(test_module_name, test_file)
        test_desc: TestDescriptor = FindTestDescriptor(test_module)
        test_desc.GenExpr.UpdateId(0)
        return test_module

class ParamView:
    def __init__(self, name, values, doc=None, expr_id=None):
        self.name = name
        self.values = values
        self.doc = doc
        self.id = expr_id
    
    def to_dict(self):
        return {
            'type': 'param',
            'id': self.id,
            'name': self.name,
            'values': self.values,
            'doc': self.doc
        }

class CrossView:
    def __init__(self, items, doc=None, expr_id=None):
        self.items = items if isinstance(items, list) else [items]
        self.doc = doc
        self.id = expr_id
    
    def to_dict(self):
        return {
            'type': 'cross',
            'id': self.id,
            'items': [item.to_dict() for item in self.items],
            'doc': self.doc
        }
 
class UnionView:
    def __init__(self, items, doc=None, expr_id=None):
        self.items = items
        self.doc = doc
        self.id = expr_id
    
    def to_dict(self):
        return {
            'type': 'union',
            'id': self.id,
            'items': [item.to_dict() for item in self.items],
            'doc': self.doc
        }

def convert_test_expr(expr):
    """Convert TestExpr objects to our viewer objects"""
    if expr is None:
        return None
        
    exprId = expr.ID
    doc = getattr(expr, '_doc', None)

    if isinstance(expr, Param):
        values = [str(v) for v in expr._values]
        print(f"Converting Param: name={expr._name}, values={values}, id={exprId}")
        return ParamView(expr._name, values, doc, exprId)
    elif isinstance(expr, Cross):
        exprs = list(expr._exprs)
        print(f"Converting Cross with {len(exprs)} expressions, id={exprId}")
        converted_exprs = [convert_test_expr(e) for e in exprs]
        return CrossView(converted_exprs, doc, exprId)
    elif isinstance(expr, Union):
        converted_items = [convert_test_expr(item) for item in expr._exprs]
        return UnionView(converted_items, doc, exprId)
    else:
        print(f"Warning: Unknown expression type: {type(expr)}")
        return None

# Global test loader instance
test_loader = TestLoader()
current_test_file = "pforge/plans/RbeSpNumWo.py"  # Default test file

@app.route('/')
def index():
    return render_template('TestPlanViewer.html')

@app.route('/api/expression')
def get_expression():
    try:
        print("\n=== Debug Information ===")
        print(f"Loading test file: {current_test_file}")
        
        # Load the test module and get its Tests object
        test_module = test_loader.load_test_modules(current_test_file)
        expr = FindTestDescriptor(test_module).GenExpr
        
        print(f"Tests object type: {type(expr)}")
        print(f"Tests object content: {expr}")
        
        print("\nConverting expression...")
        converted = convert_test_expr(expr)
        print(f"Converted expression type: {type(converted)}")
        print(f"Converted expression content: {converted.__dict__}")
        
        print("\nConverting to dict...")
        result = converted.to_dict()
        print("Final result:", json.dumps(result, indent=2))
        return jsonify(result)
    except Exception as e:
        import traceback
        print(f"Error in get_expression: {str(e)}")
        print("Traceback:")
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

@app.route('/api/load_test/<path:test_file>')
def load_test(test_file):
    """API endpoint to change the current test file"""
    global current_test_file
    try:
        if not os.path.exists(test_file):
            return jsonify({"error": f"Test file not found: {test_file}"}), 404
        current_test_file = test_file
        return jsonify({"message": f"Successfully loaded test file: {test_file}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/test_files')
def list_test_files():
    """API endpoint to list all test files in the current directory"""
    try:
        test_files = []
        for file in Path('.').glob('*.py'):
            if file.name.endswith('Tests.py'):
                test_files.append({
                    'name': file.name,
                    'path': str(file),
                    'active': file.name == current_test_file
                })
        return jsonify(test_files)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/test_descriptor')
def get_test_descriptor():
    try:
        print("\nGetting test descriptor...")
        test_module = test_loader.load_test_modules(current_test_file)
        test_desc: TestDescriptor = FindTestDescriptor(test_module)

        return jsonify({
            'suiteName': test_desc.SuiteName,
            'includeFiles': test_desc.Cpp_IncludeFiles,
            'testGeneratorMacro': test_desc.Cpp_TestGeneratorMacro,
            'caseNamePrefix': test_desc.Cpp_CaseNamePrefix
        })
    except Exception as e:
        print(f"Error in get_test_descriptor: {str(e)}")
        return jsonify({
            'suiteName': '',
            'includeFiles': [],
            'testGeneratorMacro': '',
            'caseNamePrefix': ''
        })

@app.route('/api/test_list')
def get_test_list():
    try:
        print("\n=== Generating Test List ===")
        # Load the test module
        print(f"Loading test file: {current_test_file}")
        test_module = test_loader.load_test_modules(current_test_file)
        test_desc: TestDescriptor = FindTestDescriptor(test_module)
        print(f"Test module loaded: {test_module}")
        print(f"Test descriptor: {test_desc}")
        
        test_cases = list(
            GenerateTestsCode(
                test_desc.get_test_list(),  # Get the Tests attribute from TestDescriptor
                test_desc.Cpp_CaseNamePrefix,
                test_desc.Cpp_TestGeneratorMacro
            )
        )
        # print(f"Generated test cases: {test_cases}")
        return jsonify(test_cases)
    except Exception as e:
        print(f"Error generating test list: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return jsonify([])

@app.route('/api/test_list/<int:expr_id>')
def get_filtered_test_list(expr_id):
    return get_filtered_test_list_by_value(expr_id, None)

@app.route('/api/test_list/<int:expr_id>/index/<int:value_index>')
def get_filtered_test_list_by_value(expr_id, value_index):
    try:
        print(f"\n=== Generating Filtered Test List for ID {expr_id} and value {value_index} ===")
        test_module = test_loader.load_test_modules(current_test_file)
        test_desc: TestDescriptor = FindTestDescriptor(test_module)
        print(f"Test module loaded: {test_module}")
        print(f"Tests object: {test_desc.GenExpr}")
        
        def need_discard(pv: PVPair):
            return pv.param.ID == expr_id and pv.value != pv.param.Values[value_index]

        filtered_test_cases = []
        for test_case_param_args in test_desc.get_test_list():
            if any(need_discard(pv) for pv in test_case_param_args):
                continue
            filtered_test_cases.append(test_case_param_args)
        
        if not filtered_test_cases:
            print(f"No expression found with ID {expr_id} and value {value_index}")
            return jsonify([])
        
        test_cases = list(
            GenerateTestsCode(filtered_test_cases, test_desc.Cpp_CaseNamePrefix, test_desc.Cpp_TestGeneratorMacro)
            )

        return jsonify(test_cases)
    except Exception as e:
        print(f"Error generating filtered test list: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)
    print("Starting Flask server...")
    app.run(debug=True, port=8900, host='0.0.0.0')  # Use default Flask port 