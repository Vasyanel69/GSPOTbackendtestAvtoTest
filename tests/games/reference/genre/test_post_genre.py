import allure
import pytest

from source.base.generator import Generator
from source.enums.data import Cases
from source.schemas.genre_schema import Genre
from source.api.genre import create_genre, delete_genre
from source.base.validator import assert_json_by_model, assert_json_key_value, assert_status_code


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Genre')
@allure.suite('Test post genre')
@pytest.mark.smoke
class TestGenreCreate:

    @allure.title(f'{Cases.GAMES["TG74"]["id"]}-Test genre create')
    @allure.description('Проверка успешного ответа [201] при создании жанра')
    @allure.testcase(name=Cases.GAMES["TG74"]["name"], url=Cases.GAMES["TG74"]["link"])
    def test_genre_create(self, delete_created_data):
        payload = Generator.object(model=Genre)
        response = create_genre(json=payload)

        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Genre)
        assert_json_key_value(response=response, json=payload, key='name')

        id_data = response.json().get('id')
        delete_created_data(api=delete_genre, id_data=id_data)
