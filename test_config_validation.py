import pytest
import re

from datetime import date
from test.conftest import does_not_raise
from trafaret.dataerror import DataError
from prozorro_sale.billing_service.data_calculator.config_validation import variables_from_field, \
    variables_from_date, variables_validator, constants_validator, rules_validator, exceptions_validator, \
    procedures_variable_validator, procedures_period_validator, procedures_validator, config_data_validator


class TestConfigValidation:

    @pytest.mark.parametrize('arg, expected', [
        ('procedure.description', does_not_raise()),
        ('procedure.abracadabra99999999999', pytest.raises(DataError)),
    ])
    def test_variables_from_field(self, arg, expected):
        with expected:
            variables_from_field.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        (date.today(), does_not_raise())
    ])
    def test_variables_from_date(self, arg, expected):
        with expected:
            variables_from_date(arg)

    @pytest.mark.parametrize('arg, expected', [
        ({'str': [{'fromDate': date.today(), 'value': 1.0}]}, does_not_raise()),
        ({'str': [{'fromDate': date.today(), 'value': 1}]}, does_not_raise()),
    ])
    def test_constants_validator(self, arg, expected):
        with expected:
            constants_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([{'fromField': 'procedure.description'}], does_not_raise())
    ])
    def test_rules_validator_without_optionals_args(self, arg, expected):
        with expected:
            rules_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([], does_not_raise()),  # empty list!!! must failed!!!
        ([{'fromField': 'procedure.description', 'description': 'str'}], does_not_raise())
    ])
    def test_rules_validator_with_optional_description(self, arg, expected):
        with expected:
            rules_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str'}], does_not_raise())
    ])
    def test_rules_validator_with_optional_description_mask(self, arg, expected):
        with expected:
            rules_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0}], does_not_raise())
    ])
    def test_rules_validator_with_optional_description_mask_top_float(self, arg, expected):
        with expected:
            rules_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1}], does_not_raise())
    ])
    def test_rules_validator_with_optional_description_mask_top_int(self, arg, expected):
        with expected:
            rules_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1.0}], does_not_raise())
    ])
    def test_rules_validator_with_optional_description_mask_top_float_bottom_float(self, arg, expected):
        with expected:
            rules_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1}], does_not_raise())
    ])
    def test_rules_validator_with_optional_description_mask_top_float_bottom_int(self, arg, expected):
        with expected:
            rules_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1.0}], does_not_raise())
    ])
    def test_rules_validator_with_optional_description_mask_top_int_bottom_float(self, arg, expected):
        with expected:
            rules_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1}], does_not_raise())
    ])
    def test_rules_validator_with_optional_description_mask_top_int_bottom_int(self, arg, expected):
        with expected:
            rules_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1.0, 'value': 'str'}], does_not_raise()),
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1.0, 'value': 1.0}], does_not_raise()),
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1.0, 'value': 1}], does_not_raise()),
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1.0, 'value': True}], does_not_raise())
    ])
    def test_rules_validator_with_optional_description_mask_top_float_bottom_float_values(self, arg, expected):
        with expected:
            rules_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1, 'value': 'str'}], does_not_raise()),
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1, 'value': 1.0}], does_not_raise()),
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1, 'value': 1}], does_not_raise()),
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1, 'value': True}], does_not_raise())
    ])
    def test_rules_validator_with_optional_description_mask_top_float_bottom_int_values(self, arg, expected):
        with expected:
            rules_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1.0, 'value': 'str'}], does_not_raise()),
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1.0, 'value': 1.0}], does_not_raise()),
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1.0, 'value': 1}], does_not_raise()),
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1.0, 'value': True}], does_not_raise())
    ])
    def test_rules_validator_with_optional_description_mask_top_int_bottom_float_values(self, arg, expected):
        with expected:
            rules_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1, 'value': 'str'}], does_not_raise()),
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1, 'value': 1.0}], does_not_raise()),
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1, 'value': 1}], does_not_raise()),
        ([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1, 'value': True}], does_not_raise())
    ])
    def test_rules_validator_with_optional_description_mask_top_int_bottom_int_values(self, arg, expected):
        with expected:
            rules_validator.check(arg)

    @pytest.mark.parametrize('arg, expected', [
        ([{'procedures': ['str'], 'rules': [{'fromField': 'procedure.description'}]}], does_not_raise())
    ])
    def test_exceptions_validator(self, arg, expected):
        exceptions_validator.check(arg)



    #     procedures_variable_validator.check({'description': 'str', 'value': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 'str', 'valueAddedTaxIncluded': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 'str', 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1.0})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1.0, 'valueAddedTaxIncluded': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1.0, 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1.0, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1, 'valueAddedTaxIncluded': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1, 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'valueAddedTaxIncluded': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 'str', 'valueAddedTaxIncluded': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 'str', 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1.0})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1.0, 'valueAddedTaxIncluded': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1.0, 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1.0, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1, 'valueAddedTaxIncluded': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1, 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'valueAddedTaxIncluded': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 'str', 'valueAddedTaxIncluded': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 'str', 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1.0})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1.0, 'valueAddedTaxIncluded': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1.0, 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1.0, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1, 'valueAddedTaxIncluded': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1, 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'valueAddedTaxIncluded': 'str'})
    #     procedures_variable_validator.check({'description': 'str', 'value': 1, 'purposeDescription': 'str'})

    @pytest.mark.parametrize('arg, expected', [
        ({'fromField': 'procedure.description', 'between': [{'bottom': 1.0, 'values': {'description': 'str', 'value': 1, 'purposeDescription': 'str'}}]}, does_not_raise()),
        ({'fromField': 'procedure.description', 'between': [{'bottom': 1, 'values': {'description': 'str', 'value': 1, 'purposeDescription': 'str'}}]}, does_not_raise()),
    ])
    def test_procedures_period_validator_without_optionals_args(self, arg, expected):
        with expected:
            procedures_period_validator(arg)

    @pytest.mark.parametrize('arg, expected', [
        ({'fromField': 'procedure.description', 'between': [{'top': 1.0,'bottom': 1.0, 'values': {'description': 'str', 'value': 1, 'purposeDescription': 'str'}}]}, does_not_raise()),
        ({'fromField': 'procedure.description', 'between': [{'top': 1,'bottom': 1.0, 'values': {'description': 'str', 'value': 1, 'purposeDescription': 'str'}}]}, does_not_raise()),
        ({'fromField': 'procedure.description', 'between': [{'top': 1.0,'bottom': 1, 'values': {'description': 'str', 'value': 1, 'purposeDescription': 'str'}}]}, does_not_raise()),
        ({'fromField': 'procedure.description', 'between': [{'top': 1,'bottom': 1, 'values': {'description': 'str', 'value': 1, 'purposeDescription': 'str'}}]}, does_not_raise()),
    ])
    def test_procedures_period_validator_with_optional_top(self, arg, expected):
        with expected:
            procedures_period_validator(arg)

    # @pytest.mark.parametrize('arg, expected', [
    #     ({'str': [{'fromDate': date.today(), 'variables': {'str': {'description': 'str', 'value': 'str'}}}]}, does_not_raise()),
    # ])
    # def test_procedures_validator(self, arg, expected):
    #     with expected:
    #         procedures_period_validator(arg)

        procedures_validator.check({'str': [{'fromDate': date.today(), 'variables': {'str': {'description': 'str', 'value': 'str'}}}]})  # procedures_variable_validator
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'variables': {1: {'description': 'str', 'value': 'str'}}}]})  # procedures_variable_validator
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {'rules': {'switch': [{'period': {}}]}}}}]})  # rules is empty!!! second choice t.Dict
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {'rules': {'switch': [{'period': {}, 'rule': []}]}}}}]})  # rules is empty!!! second choice t.Dict
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {'rules': {'switch': [{'rule': [], 'values': {}}]}}}}]})  # rules is empty!!! second choice t.Dict
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {'rules': {'default': {}, 'switch': [{'period': {}}]}}}}]})  # rules is empty!!! second choice t.Dict
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {'rules': {'default': {}, 'switch': [{'period': {}, 'rule': []}]}}}}]})  # rules is empty!!! second choice t.Dict
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {'rules': {'default': {}, 'switch': [{'rule': [], 'values': {}}]}}}}]})  # rules is empty!!! second choice t.Dict
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {}}}]})  # rules is empty!!!
    #
    #     config_data_validator.check({'variables': {}, 'procedures': {}, 'constants': {}, 'exceptions': []})  # empty values!!!
