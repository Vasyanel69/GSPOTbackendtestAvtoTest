import allure
import pytest

from source.api.payments.payments import get_services_list
from source.base.validator import (assert_status_code, assert_json_by_model)
from source.schemas.payments.external_payments_services_schema import External_Payments


@allure.epic('Payments')
@allure.feature('External Payments')
@allure.story('Services')
@allure.suite('Test get services')
@pytest.mark.smoke
class TestPaymentsGetList:

    @allure.title('Test external payments services list')
    @allure.description('Проверка успешного ответа [200] при запросе списка сервисов оплаты')
    def test_external_payments_services_positive_get(self):
        response = get_services_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=External_Payments)