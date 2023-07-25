import allure
import pytest

from source.base.generator import Generator
from source.schemas.product_languages import ProductLanguages
from source.api.product_languages import update_product_languages
from source.base.validator import (assert_json_by_model, assert_status_code,
                                   assert_json_key_value, assert_json_equal_json)


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Product languages')
@allure.suite('Test put product languages')
@pytest.mark.smoke
@pytest.mark.xfail(reason='Product languages cannot be created')
class TestProductLanguagesUpdate:
    @allure.title('Test product languages update')
    @allure.description('Проверка успешного ответа [200] при обновлении языка продукта')
    def test_languages_update(self, create_delete_test_product_languages):
        id_test = create_delete_test_product_languages.json().get('id')

        payload = Generator.object(model=ProductLanguages, seed=2)
        response = update_product_languages(id_data=id_test, json=payload)
        payload['id'] = id_test

        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=ProductLanguages)
        assert_json_equal_json(response=response, json=payload)
        assert_json_key_value(response=response, json=payload, key='name')

