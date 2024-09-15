import os

import requests
import inspect
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='a', filename='runner_tests.log', encoding='utf8',
                    format="%(asctime)s | %(levelname)s | %(message)s")

class Runner:
    speed = 1
    name = 'Вася'
    def __init__(self, name, speed=5):
        #if isinstance(name, str):
        self.name = name
        #else:
        #    raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        #if speed > 0:
        self.speed = speed
        #else:
        #    raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += abs(self.speed) * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

first = Runner(8, 10)
second = Runner('Илья', -5)
third = Runner('Арсен', 10)

class RunnerTest_01(unittest.TestCase):

    def test_walk(self):
        runner = first
        try:
            if runner.speed > 0:
                for i in range(10):
                    runner.walk()
                    # self.assertEqual(self.runner.distance, 50)
                logging.info(f"'test_walk' выполнен успешн {runner.name}")
            else:
                raise TypeError(f'Скорость не может быть отрицательной, сейчас {runner.speed}')
        except:
            logging.warning(f"Неверный тип данных для объекта first {runner.name} test_walk")

    def test_run(self):
        runner = first
        try:
            if isinstance(runner.name, str):
                for i in range(10):
                    runner.run()
                    # self.assertEqual(self.runner.distance, 100)
                logging.info(f"'test_run' выполнен успешн {runner.name}")
            else:
                raise TypeError(f'Имя может быть только строкой, передано {type(runner.name)}')
        except:
            logging.warning(f"Неверный тип данных для объекта Runner {runner.name} test_run")

class RunnerTest_02(unittest.TestCase):

    def test_walk(self):
        runner = second
        try:
            if runner.speed > 0:
                for i in range(10):
                    runner.walk()
                    # self.assertEqual(self.runner.distance, 50)
                logging.info(f"'test_walk' выполнен успешн {runner.name}")
            else:
                raise TypeError(f'Скорость не может быть отрицательной, сейчас {runner.speed}')
        except:
            logging.warning(f"Неверный тип данных для объекта second {runner.name} test_walk")

    def test_run(self):
        runner = second
        try:
            if isinstance(runner.name, str):
                for i in range(10):
                        runner.run()
                    # self.assertEqual(self.runner.distance, 100)
                logging.info(f"'test_run' выполнен успешн {runner.name}")
            else:
                raise TypeError(f'Имя может быть только строкой, передано {type(runner.name)}')
        except:
            logging.warning(f"Неверный тип данных для объекта Runner {runner.name} test_run")

class RunnerTest_03(unittest.TestCase):

    def test_walk(self):
        runner = third
        try:
            if runner.speed > 0:
                for i in range(10):
                    runner.walk()
                    # self.assertEqual(self.runner.distance, 50)
                logging.info(f"'test_walk' выполнен успешн {runner.name}")
            else:
                raise TypeError(f'Скорость не может быть отрицательной, сейчас {runner.speed}')
        except:
            logging.warning(f"Неверный тип данных для объекта third {runner} test_walk")

    def test_run(self):
        runner = third
        try:
            if isinstance(runner.name, str):
                for i in range(10):
                        runner.run()
                    # self.assertEqual(self.runner.distance, 100)
                logging.info(f"'test_run' выполнен успешн {runner.name}")
            else:
                raise TypeError(f'Имя может быть только строкой, передано {type(runner.name)}')
        except:
            logging.warning(f"Неверный тип данных для объекта Runner {runner.name}")

if __name__ == "__main__":
    unittest.main()

import os
import unittest

