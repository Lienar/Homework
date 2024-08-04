import requests
import inspect
import unittest
import homework41_test



allTest = unittest.TestSuite()
##allTest.addtest(unittest.makeSuite(homework40.TournamentTest))
##allTest.addtest(unittest.makeSuite(homework39.RunnerTest))

allTest.addTest(unittest.TestLoader().loadTestsFromTestCase(homework41_test.TournamentTest))
allTest.addTest(unittest.TestLoader().loadTestsFromTestCase(homework41_test.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(allTest)