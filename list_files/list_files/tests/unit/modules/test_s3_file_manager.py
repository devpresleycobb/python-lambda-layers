from layer import s3_file_manager
import pytest


@pytest.fixture
def bucket_name():
    return 'pc-releases'


def test_list_files(bucket_name):
    res = s3_file_manager.list_files(bucket_name)
    for file in res:
        assert False
        break
