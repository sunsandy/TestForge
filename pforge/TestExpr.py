import dataclasses
import itertools
import typing
import types
from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum

class Expr:
    def __init__(self, name):
        self._name = name
        self._doc = ""
        self._id = None

    @property
    def ID(self):
        return self._id

    def GetDoc(self):
        return self._doc

    def Doc(self, doc):
        self._doc = doc
        return self

    def __add__(self, other: "Expr"):
        if isinstance(self, Union):
            return Union(*self._exprs, other)
        return Union(self, other)

    def __mul__(self, other: "Expr"):
        if isinstance(self, Cross):
            return Cross(*self._exprs, other)
        return Cross(self, other)

    @abstractmethod
    def FilterByContainsIdAndValue(self, id, value):
        pass

    @abstractmethod
    def ContainsId(self, id):
        pass

    @abstractmethod
    def UpdateId(self, newId):
        pass


class Param(Expr):
    def __init__(self, name, values, ToName=None, ToArg=None, ToDisplay=None, AllToDisplay=None):
        super().__init__(name)
        self._values = values
        self._ToName = ToName
        self._ToArg = ToArg
        self._ToDisplay = ToDisplay
        self._AllToDisplay = AllToDisplay

        if self._ToArg is None:
            self._ToArg = lambda x: str(x)

        if self._ToDisplay is None:
            self._ToDisplay = lambda x: str(x)

        if self._ToName is None:
            self._ToName = self._default_ToName

    def _default_ToName(self, value):
        if isinstance(value, Enum):
            return value.name.lower()
        return str(value).lower()

    def ToDisplay(self, value):
        if self._fnAllToDisplay is not None:
            return self._AllToDisplay(value)
        return self._ToDisplay(value)

    def ToTestNamePart(self, value):
        return self._ToName(value)

    def ToArg(self, value):
        return self._ToArg(value)

    @property
    def Values(self):
        return self._values

    @property
    def Name(self):
        return self._name

    def FilterByContainsIdAndValue(self, filterId, valueIndex):
        if self.ContainsId(filterId) and valueIndex is not None:
            print(self._values)
            print(valueIndex)
            return Param(self._name, [self._values[valueIndex]])
        return self

    def ContainsId(self, filterId):
        return self._id == filterId

    def UpdateId(self, newId):
        self._id = newId
        return newId + 1


class Union(Expr):
    def __init__(self, *exprs):
        super().__init__("Union")
        self._exprs = exprs

    def __iter__(self):
        return iter(self._exprs)

    def FilterByContainsIdAndValue(self, filterId, valueIndex):
        validBranches = [
            validBranch
            for validBranch in self._exprs
            if validBranch.ContainsId(filterId)
        ]
        ret = Union(
            *(b.FilterByContainsIdAndValue(filterId, valueIndex) for b in validBranches)
        )
        return ret

    def ContainsId(self, filterId):
        return any(e.ContainsId(filterId) for e in self._exprs)

    def UpdateId(self, newId):
        self._id = newId
        nextId = newId + 1
        for i, e in enumerate(self._exprs):
            nextId = e.UpdateId(nextId)
        return nextId


class Cross(Expr):
    def __init__(self, *exprs):
        super().__init__("Cross")
        self._exprs = exprs

    def __iter__(self):
        return itertools.product(*(e for e in self._exprs))

    def ContainsId(self, filterId):
        ret = any(e.ContainsId(filterId) for e in self._exprs)
        return ret

    def FilterByContainsIdAndValue(self, filterId, valueIndex):
        if self.ContainsId(filterId):
            filteredExprs = []
            for e in self._exprs:
                if e.ContainsId(filterId):
                    filteredExprs.append(
                        e.FilterByContainsIdAndValue(filterId, valueIndex)
                    )
                else:
                    filteredExprs.append(e)
            ret = Cross(*filteredExprs)
            return ret
        return self

    def UpdateId(self, newId):
        self._id = newId
        nextId = newId + 1
        for i, e in enumerate(self._exprs):
            nextId = e.UpdateId(nextId)
        return nextId

def FindTestDescriptor(module: types.ModuleType):
    test_desc_objects = [obj for obj in module.__dict__.values() if isinstance(obj, TestDescriptor)]
    if len(test_desc_objects) != 1:
        raise ValueError("TestPlan must have exactly one TestDescriptor object.")
    return test_desc_objects[0]

@dataclasses.dataclass
class PVPair:
    param: Param
    value: typing.Any

def GenerateList(expr: typing.Union[Param, Union, Cross, types.ModuleType]):
    if isinstance(expr, Param):
        yield from (PVPair(expr, value) for value in expr._values)
    elif isinstance(expr, Union):
        yield from itertools.chain.from_iterable(
            GenerateList(e) for e in expr._exprs
        )
    elif isinstance(expr, Cross):
        yield from itertools.product(
            *(GenerateList(e) for e in expr._exprs)
        )
    elif isinstance(expr, typing.ModuleType):
        test_desc: TestDescriptor = FindTestDescriptor(expr)
        yield from GenerateList(test_desc.TestGen)


@dataclass
class TestDescriptor:
    # Test description
    SuiteName: str
    TestGen: Expr

    # C++ code generation
    Cpp_IncludeFiles: typing.List[str]
    Cpp_TestGeneratorMacro: str
    Cpp_CaseNamePrefix: str

# Explicitly export classes and functions
__all__ = ["Expr", "Param", "Union", "Cross", "TestDescriptor", "GenerateList"]
