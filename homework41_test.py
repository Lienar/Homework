import requests
import inspect
import unittest

is_frozen = True
is_main_test_done = False

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    participant.distance = 0
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):

    @unittest.skipIf((is_frozen == False), "Тесты в этом кейсе заморожены")
    def test_walk(self):
        test_walker = Runner("test_walker")
        for i in range (10):
            test_walker.walk()
        self.assertEqual(test_walker.distance, 50)


    @unittest.skipIf((is_frozen == False), "Тесты в этом кейсе заморожены")
    def test_run(self):
        print('self.is_main_test_done_run =', is_main_test_done)
        test_runner = Runner("test_runner")
        for i in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    @unittest.skipIf((is_frozen == False), "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        test_comp_runner = Runner("test_comp_runner")
        test_comp_walker = Runner("test_comp_walker")
        for i in range(10):
            test_comp_runner.run()
            test_comp_walker.walk()
        self.assertNotEqual(test_comp_runner.distance, test_comp_walker.distance)


class TournamentTest(unittest.TestCase):
    all_results = {}
    subjectGroup1 = []
    subjectGroup2 = []
    subjectGroup3 = []
    subjectControlGroup = []

    def setUp(self):
        Ysaien = Runner('Усейн', 10)
        Andrey = Runner('Андрей', 9)
        Nik = Runner('Ник', 3)

        self.subjectGroup1 = [Ysaien, Nik]
        self.subjectGroup2 = [Andrey, Nik]
        self.subjectGroup3 = [Ysaien, Andrey, Nik]
        self.subjectControlGroup = [Nik]

    @classmethod
    def setUpClass(self):

        self.setUp(self)

        tournament1 = Tournament(90, *self.subjectGroup1)
        tournament2 = Tournament(90, *self.subjectGroup2)
        tournament3 = Tournament(90, *self.subjectGroup3)

        self.all_results[f'test1'] = tournament1.start()
        self.all_results[f'test2'] = tournament2.start()
        self.all_results[f'test3'] = tournament3.start()

    @classmethod
    def tearDownClass(self):
        print (" ")
        for i in range (0, len(self.all_results)):
            print(self.all_results[f'test{i+1}'])

    @unittest.skipIf((is_frozen == True), "Тесты в этом кейсе заморожены")
    def testTournament1(self):
        self.assertTrue(self.all_results[f'test1'][len(self.all_results[f'test1'])] == self.subjectControlGroup[0].name)

    @unittest.skipIf((is_frozen == True), "Тесты в этом кейсе заморожены")
    def testTournament2(self):
        self.assertTrue(self.all_results[f'test2'][len(self.all_results[f'test2'])] == self.subjectControlGroup[0].name)

    @unittest.skipIf((is_frozen == True), "Тесты в этом кейсе заморожены")
    def testTournament3(self):
        self.assertTrue(self.all_results[f'test3'][len(self.all_results[f'test3'])] == self.subjectControlGroup[0].name)


if __name__ == "__main__":
    unittest.main()