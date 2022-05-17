import pytest

import giphpy.core


@pytest.mark.parametrize("func_kwargs, instance_api_key", [({"params": {"api_key": "123"}}, None), ({}, "123")])
def test__set_api_key_on_params(func_kwargs, instance_api_key):
    giphpy.core._set_api_key_on_params(func_kwargs, instance_api_key)
    assert func_kwargs["params"]["api_key"] == "123"


def test_handle_params_raises():
    with pytest.raises(ValueError):
        giphpy.core._handle_params(dict(params=dict()))


@pytest.mark.parametrize("v", list(range(11)))
def test__validate_weirdness(v):
    giphpy.core._validate_weirdness(v)


@pytest.mark.parametrize("v", [-1, 11])
def test__validate_weirdness_raise(v):
    with pytest.raises(ValueError):
        giphpy.core._validate_weirdness(v)
