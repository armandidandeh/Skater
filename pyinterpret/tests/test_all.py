import unittest


def run_tests():
    testsuite = unittest.TestLoader().discover('.', pattern="test_*.py")
    import pdb
    pdb.set_trace()
    unittest.TextTestRunner(verbosity=2).run(testsuite)


if __name__ == '__main__':
    run_tests()
