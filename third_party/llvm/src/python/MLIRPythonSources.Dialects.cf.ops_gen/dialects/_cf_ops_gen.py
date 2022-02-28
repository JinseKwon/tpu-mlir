
# Autogenerated by mlir-tblgen; don't manually edit.

from ._ods_common import _cext as _ods_cext
from ._ods_common import extend_opview_class as _ods_extend_opview_class, segmented_accessor as _ods_segmented_accessor, equally_sized_accessor as _ods_equally_sized_accessor, get_default_loc_context as _ods_get_default_loc_context, get_op_result_or_value as _get_op_result_or_value, get_op_results_or_values as _get_op_results_or_values
_ods_ir = _ods_cext.ir

try:
  from . import _cf_ops_ext as _ods_ext_module
except ImportError:
  _ods_ext_module = None

import builtins


@_ods_cext.register_dialect
class _Dialect(_ods_ir.Dialect):
  DIALECT_NAMESPACE = "cf"
  pass


@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class AssertOp(_ods_ir.OpView):
  OPERATION_NAME = "cf.assert"

  _ODS_REGIONS = (0, True)

  def __init__(self, arg, msg, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(arg))
    attributes["msg"] = msg
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def arg(self):
    return self.operation.operands[0]

  @builtins.property
  def msg(self):
    return _ods_ir.StringAttr(self.operation.attributes["msg"])

  @msg.setter
  def msg(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["msg"] = value

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class BranchOp(_ods_ir.OpView):
  OPERATION_NAME = "cf.br"

  _ODS_REGIONS = (0, True)

  def __init__(self, destOperands, dest, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.extend(_get_op_results_or_values(destOperands))
    _ods_successors = []
    _ods_successors.append(dest)
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def destOperands(self):
    _ods_variadic_group_length = len(self.operation.operands) - 1 + 1
    return self.operation.operands[0:0 + _ods_variadic_group_length]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CondBranchOp(_ods_ir.OpView):
  OPERATION_NAME = "cf.cond_br"

  _ODS_OPERAND_SEGMENTS = [1,-1,-1,]

  _ODS_REGIONS = (0, True)

  def __init__(self, condition, trueDestOperands, falseDestOperands, trueDest, falseDest, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(condition))
    operands.append(_get_op_results_or_values(trueDestOperands))
    operands.append(_get_op_results_or_values(falseDestOperands))
    _ods_successors = []
    _ods_successors.append(trueDest)
    _ods_successors.append(falseDest)
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def condition(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 0)
    return operand_range[0]

  @builtins.property
  def trueDestOperands(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 1)
    return operand_range

  @builtins.property
  def falseDestOperands(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 2)
    return operand_range

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class SwitchOp(_ods_ir.OpView):
  OPERATION_NAME = "cf.switch"

  _ODS_OPERAND_SEGMENTS = [1,-1,-1,]

  _ODS_REGIONS = (0, True)

  def __init__(self, flag, defaultOperands, caseOperands, case_values, case_operand_segments, defaultDestination, caseDestinations, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(flag))
    operands.append(_get_op_results_or_values(defaultOperands))
    operands.append(_get_op_results_or_values(caseOperands))
    if case_values is not None: attributes["case_values"] = case_values
    attributes["case_operand_segments"] = case_operand_segments
    _ods_successors = []
    _ods_successors.append(defaultDestination)
    _ods_successors.extend(caseDestinations)
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def flag(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 0)
    return operand_range[0]

  @builtins.property
  def defaultOperands(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 1)
    return operand_range

  @builtins.property
  def caseOperands(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 2)
    return operand_range

  @builtins.property
  def case_values(self):
    if "case_values" not in self.operation.attributes:
      return None
    return _ods_ir.DenseIntElementsAttr(self.operation.attributes["case_values"])

  @case_values.setter
  def case_values(self, value):
    if value is not None:
      self.operation.attributes["case_values"] = value
    elif "case_values" in self.operation.attributes:
      del self.operation.attributes["case_values"]

  @case_values.deleter
  def case_values(self):
    del self.operation.attributes["case_values"]

  @builtins.property
  def case_operand_segments(self):
    return _ods_ir.DenseIntElementsAttr(self.operation.attributes["case_operand_segments"])

  @case_operand_segments.setter
  def case_operand_segments(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["case_operand_segments"] = value
