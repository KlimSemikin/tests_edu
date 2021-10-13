import pytest

from task_3_place_holder_api.place_holder_api import PlaceHolderApi
from task_3_place_holder_api.tests import test_data


@pytest.fixture(scope="module")
def set_url():
    PlaceHolderApi.set_url(test_data.base_url)
