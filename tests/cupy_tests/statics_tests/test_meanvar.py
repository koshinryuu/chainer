import unittest

from cupy import testing


@testing.gpu
class TestMeanVar(unittest.TestCase):

    _multiprocess_can_split_ = True

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_mean_all(self, xpy, dtype):
        a = testing.shaped_arange((2, 3), xpy, dtype)
        return a.mean()

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_mean_axis(self, xpy, dtype):
        a = testing.shaped_arange((2, 3, 4), xpy, dtype)
        return a.mean(axis=1)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_var_all(self, xpy, dtype):
        a = testing.shaped_arange((2, 3), xpy, dtype)
        return a.var()

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_var_axis(self, xpy, dtype):
        a = testing.shaped_arange((2, 3, 4), xpy, dtype)
        return a.var(axis=1)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_std_all(self, xpy, dtype):
        a = testing.shaped_arange((2, 3), xpy, dtype)
        return a.std()

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_std_axis(self, xpy, dtype):
        a = testing.shaped_arange((2, 3, 4), xpy, dtype)
        return a.std(axis=1)
