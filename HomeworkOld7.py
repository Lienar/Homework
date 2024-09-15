import requests
import inspect
import unittest
import HomeworkOld7_test



allTest = unittest.TestSuite()
##allTest.addtest(unittest.makeSuite(homework40.TournamentTest))
##allTest.addtest(unittest.makeSuite(homework39.RunnerTest))

#allTest.addTest(unittest.TestLoader().loadTestsFromTestCase(HomeworkOld7_test.TournamentTest))
allTest.addTest(unittest.TestLoader().loadTestsFromTestCase(HomeworkOld7_test.RunnerTest_01))
allTest.addTest(unittest.TestLoader().loadTestsFromTestCase(HomeworkOld7_test.RunnerTest_02))
allTest.addTest(unittest.TestLoader().loadTestsFromTestCase(HomeworkOld7_test.RunnerTest_03))

#first = HomeworkOld7_test.Runner('Вося', 10)
#second = HomeworkOld7_test.Runner('Илья', 5)
#third = HomeworkOld7_test.Runner('Арсен', 10)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(allTest)


#
# t = Tournament(101, first, second)
# print(t.start())



