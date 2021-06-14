import pytest
import sys
import os
sys.path.insert(0,'../..')


def test_lambda_handler(event, context):
    if 'PIPELINE' in os.environ:
        pytest.main(["-x", "tests/unit/modules"])
    else:
        pytest.main(["-x", "modules"])


if __name__ == '__main__':
    test_lambda_handler({}, {})
