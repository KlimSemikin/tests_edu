import pytest

from framework.api_utils import ApiUtils
from tests import test_data


@pytest.fixture(scope="module")
def set_url():
    ApiUtils.set_url(test_data.base_url)
