
import sys, os
import copy
from unittest import TestCase

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../tests")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "../")

from main import Main
from user import User
from collections import defaultdict

class MainTestCase(TestCase):
    def setUp(self):
        print("", end='\n\n')
        print("Running test cases", end="\n\n")
        self.main = Main()
        self.userGraph = defaultdict(list)
        self.userNodes = defaultdict()
        self.nodes = []
        self.users = [
            {
                "name":"UserA",
                "gender": "Female",
                "age": 25,
                "interests": ["Cricket"]
            },
            {
                "name": "UserB",
                "gender": "Male",
                "age": 27,
                "interests": ["Cricket", "Football", "Movies"]
            },
            {
                "name": "UserC",
                "gender": "Male",
                "age": 26,
                "interests": ["Movies", "Tennis", "Football", "Cricket"]
            },
            {
                "name": "UserD",
                "gender": "Female",
                "age": 24,
                "interests": ["Tennis", "Football", "Badminton"]
            },
            {
                "name": "UserE",
                "gender": "Female",
                "age": 32,
                "interests": ["Cricket", "Football", "Movies", "Badminton"]
            }
        ]

    def test_register_users(self):
        self.nodes = self.main.registerUsers(self.users)
        self.assertEqual(len(self.nodes), len(self.users))
        print("Register users test case executed successfully", end='\n\n')

    def test_build_graph(self):
        self.userGraph = self.main.buildGraph(self.nodes)
        self.assertEqual(len(self.userGraph), len(self.nodes))
        print("build graph test case executed successfully")

    def test_top_matches(self):
        self.nodes = self.main.registerUsers(self.users)
        self.userGraph = self.main.buildGraph(self.nodes)
        res = self.main.get_top_matches(self.userGraph, self.users[1]["name"], self.nodes, 2)
        print(res)
        print("top matches test case executed successfully")
