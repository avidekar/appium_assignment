import unittest
from test_login import Login
from test_functionality import APList


tc_login = unittest.TestLoader().loadTestsFromTestCase(Login)
tc_functional = unittest.TestLoader().loadTestsFromTestCase(APList)

# sanity test plan for the app
# sanity_test_suite = unittest.TestSuite([tc_login])
# unittest.TextTestRunner(verbosity=2).run(sanity_test_suite)

# functional test plan for the app
functional_test_suite = unittest.TestSuite([tc_functional])
unittest.TextTestRunner(verbosity=2).run(functional_test_suite)

# master test suite combination of both
# master_test_suite = unittest.TestSuite([tc_login, tc_functional])
# unittest.TextTestRunner().run(master_test_suite)
