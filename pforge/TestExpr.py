import itertools
from dataclasses import dataclass
from typing import List
from abc import abstractmethod

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

    def __add__(self, other: 'Expr'):
        if isinstance(self, Union):
            return Union(*self._exprs, other)
        return Union(self, other)

    def __mul__(self, other: 'Expr'):
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
    def __init__(self, name, values):
        super().__init__(name)
        self._values = values

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
        validBranches = [validBranch for validBranch in self._exprs if validBranch.ContainsId(filterId)]
        ret = Union(*(b.FilterByContainsIdAndValue(filterId, valueIndex) for b in validBranches))
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
                    filteredExprs.append(e.FilterByContainsIdAndValue(filterId, valueIndex))
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

def GenerateCommands(expr: Expr, paramGen):
    if (isinstance(expr, Param)):
        yield from (paramGen(expr, value) for value in expr._values)
    elif (isinstance(expr, Union)):
        yield from itertools.chain.from_iterable(GenerateCommands(e, paramGen) for e in expr._exprs)
    elif (isinstance(expr, Cross)):
        yield from itertools.product(*(GenerateCommands(e, paramGen) for e in expr._exprs))

@dataclass
class TestDescriptor:
    # Test description
    SuiteName: str
    TestGen: Expr

    # C++ code generation
    Cpp_IncludeFiles: List[str]
    Cpp_TestGeneratorMacro: str
    Cpp_CaseNamePrefix: str

# Explicitly export classes and functions
__all__ = ['Expr', 'Param', 'Union', 'Cross', 'TestDescriptor', 'GenerateCommands']
