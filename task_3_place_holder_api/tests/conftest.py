import pytest

from framework.utils.api_utils import ApiUtils
from task_3_place_holder_api.tests import test_data


@pytest.fixture(scope="module")
def set_url():
    ApiUtils.set_url(test_data.base_url)
