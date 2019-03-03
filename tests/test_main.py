import os
import sys

import django

import pytest

import pac  # noqa

from .helpers import sanity


@sanity
def test_environment_matches_expectations():
    current_env = os.getenv('CURRENTENV', None)

    assert current_env is not None, '"CURRENTENV" not set by test runner.'

    expected_django_version = current_env.split('-')[1]
    if expected_django_version == 'master':
        pytest.skip('Not testing for Django version on `master`')

    django_major_version = '.'.join(django.get_version().split('.')[:2])

    assert current_env == (
        f'py{sys.version_info.major}{sys.version_info.minor}-'
        f'{django_major_version}'
    )


@sanity
def test_django_runs(client):
    client.get('/spurious-url')
