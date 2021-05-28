import pytest
import re

from loguru import logger
from datetime import date
from test.conftest import does_not_raise
from trafaret.dataerror import DataError
from prozorro_sale.billing_service.data_calculator.config_validation import variables_from_field, \
    variables_from_date, variables_validator, constants_validator, rules_validator, exceptions_validator, \
    procedures_variable_validator, procedures_period_validator, procedures_validator, config_data_validator


class TestConfigValidation:

    # @logger.catch()
    # @pytest.mark.parametrize('arg, expected', [
    #     ('procedure.description', does_not_raise()),
    #     # ('procedure.abracadabra99999999999', pytest.raises(DataError)),
    # ])
    # async def test_variables_from_field(self, arg, expected):
    #     # assert variables_from_field.check(arg) == 'procedure.description'
    #
    #     with expected:
    #         value = variables_from_field.check(arg)
    #         assert value == 'procedure.description'


    # @logger.catch()
    # @pytest.mark.parametrize('arg, expected', [
    #     ({'str': [{'fromDate': date.today(), 'value': 1.0}]}, does_not_raise()),
    # ])
    # async def test_constants_validator(self, arg, expected):
    #     expected = {'str': [{'fromDate': date.today(), 'value': 1.0}]}
    #     with expected:
    #         value = await constants_validator.check(arg)
    #         assert value == expected

    @logger.catch()
    async def test_variables_from_field(self):
        variables_from_field.check('procedure.description')
        # variables_from_field.check('procedure.abracadabra99999999999')  # pytest.raises(errors.ProcedureNotFound)

        variables_from_date.check(date.today())

        variables_validator.check({'str': {'description': 'str', 'value': 'str'}})


        constants_validator.check({'str': [{'fromDate': date.today(), 'value': 1.0}]})
        constants_validator.check({'str': [{'fromDate': date.today(), 'value': 1}]})

        rules_validator.check([{'fromField': 'procedure.description'}])  # неперемешано
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str'}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str'}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1.0}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1.0, 'value': 'str'}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1.0, 'value': 1.0}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1.0, 'value': 1}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1.0, 'value': True}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1, 'value': 'str'}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1, 'value': 1.0}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1, 'value': 1}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1.0, 'bottom': 1, 'value': True}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1.0}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1.0, 'value': 'str'}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1.0, 'value': 1.0}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1.0, 'value': 1}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1.0, 'value': True}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1, 'value': 'str'}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1, 'value': 1.0}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1, 'value': 1}])
        rules_validator.check([{'fromField': 'procedure.description', 'description': 'str', 'mask': 'str', 'top': 1, 'bottom': 1, 'value': True}])

        exceptions_validator.check([{'procedures': ['str'], 'rules': [{'fromField': 'procedure.description'}]}])

        procedures_variable_validator.check({'description': 'str', 'value': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 'str', 'valueAddedTaxIncluded': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 'str', 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1.0})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1.0, 'valueAddedTaxIncluded': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1.0, 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1.0, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1, 'valueAddedTaxIncluded': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1, 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'minValue': 1, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'valueAddedTaxIncluded': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 'str', 'valueAddedTaxIncluded': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 'str', 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1.0})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1.0, 'valueAddedTaxIncluded': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1.0, 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1.0, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1, 'valueAddedTaxIncluded': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1, 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'minValue': 1, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'valueAddedTaxIncluded': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1.0, 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 'str', 'valueAddedTaxIncluded': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 'str', 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1.0})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1.0, 'valueAddedTaxIncluded': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1.0, 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1.0, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1, 'valueAddedTaxIncluded': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1, 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'minValue': 1, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'valueAddedTaxIncluded': 'str', 'purposeDescription': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'valueAddedTaxIncluded': 'str'})
        procedures_variable_validator.check({'description': 'str', 'value': 1, 'purposeDescription': 'str'})

        procedures_period_validator.check({'fromField': 'procedure.description', 'between': [{'bottom': 1.0, 'values': {'description': 'str', 'value': 1, 'purposeDescription': 'str'}}]})
        procedures_period_validator.check({'fromField': 'procedure.description', 'between': [{'bottom': 1, 'values': {'description': 'str', 'value': 1, 'purposeDescription': 'str'}}]})
        procedures_period_validator.check({'fromField': 'procedure.description', 'between': [{'top': 1.0, 'bottom': 1.0, 'values': {'description': 'str', 'value': 1, 'purposeDescription': 'str'}}]})
        procedures_period_validator.check({'fromField': 'procedure.description', 'between': [{'top': 1.0, 'bottom': 1, 'values': {'description': 'str', 'value': 1, 'purposeDescription': 'str'}}]})
        procedures_period_validator.check({'fromField': 'procedure.description', 'between': [{'top': 1, 'bottom': 1, 'values': {'description': 'str', 'value': 1, 'purposeDescription': 'str'}}]})
        procedures_period_validator.check({'fromField': 'procedure.description', 'between': [{'top': 1, 'bottom': 1.0, 'values': {'description': 'str', 'value': 1, 'purposeDescription': 'str'}}]})

        procedures_validator.check({'str': [{'fromDate': date.today(), 'variables': {'str': {'description': 'str', 'value': 'str'}}}]})  # procedures_variable_validator
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {'rules': {'switch': [{'period': {}}]}}}}]})  # rules is empty!!! second choice t.Dict
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {'rules': {'switch': [{'period': {}, 'rule': []}]}}}}]})  # rules is empty!!! second choice t.Dict
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {'rules': {'switch': [{'rule': [], 'values': {}}]}}}}]})  # rules is empty!!! second choice t.Dict
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {'rules': {'default': {}, 'switch': [{'period': {}}]}}}}]})  # rules is empty!!! second choice t.Dict
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {'rules': {'default': {}, 'switch': [{'period': {}, 'rule': []}]}}}}]})  # rules is empty!!! second choice t.Dict
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {'rules': {'default': {}, 'switch': [{'rule': [], 'values': {}}]}}}}]})  # rules is empty!!! second choice t.Dict
        # procedures_validator.check({'str': [{'fromDate': date.today(), 'rules': [], 'variables': {'str': {}}}]})  # rules is empty!!!

        config_data_validator.check({'variables': {}, 'procedures': {}, 'constants': {}, 'exceptions': []})  # empty values!!!
