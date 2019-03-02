import os

import pytest


RUN_ALL_TESTS = os.environ.get('RUN_ALL', 'FALSE') == 'TRUE'
RUN_SANITY_TESTS = os.environ.get('RUN_SANITY', 'FALSE') == 'TRUE'


sanity = pytest.mark.skipif(
    not RUN_ALL_TESTS and not RUN_SANITY_TESTS,
    reason=(
        'Sanity tests skipped without `RUN_ALL` or `RUN_SANITY` set to'
        ' `TRUE`.'
    ),
)
