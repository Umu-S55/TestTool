import calculation
import pytest

# release_name = 'lesson'
#
is_release=True

class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        # self.cal = calculation.Cal()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        # del self.cal

    def test_add_num_and_double(self):
        cal = calculation.Cal()
        assert cal.add_num_and_double(1,1) == 4

    @pytest.mark.skip(reason='skip!')
    @pytest.mark.skipif(is_release==True,reason='skip!')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            cal = calculation.Cal()
            cal.add_num_and_double('1', '1')


#
#     # @unittest.skip('skip!')
#     @unittest.skipIf(release_name=='lesson2', 'skip!')
#     def test_add_num_and_double(self):
#         self.assertEqual(
#             self.cal.add_num_and_double(1, 1), 4)
#

#
# if __name__ == '__main__':
#     unittest.main()