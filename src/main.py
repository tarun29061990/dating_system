from collections import defaultdict
from user import User
from constants import Constant
import uuid

class Main:
    def __init__(self):
        self.userGraph = defaultdict(list)
        self.userNodes = defaultdict()

    def registerUsers(self, users):
        nodes = []
        for user in users:
            u = User(uuid.uuid1(), user["name"], user["gender"], user["age"], user["interests"])
            self.userNodes[u.id] = u
            nodes.append(u)
        return self.userNodes

    def buildGraph(self, userNodes):
        users = []
        for key, value in enumerate(userNodes):
            users.append(userNodes[value])

        l = len(users)
        for i in range(l):
            user = users[i]
            gender = user.gender
            for j in range(l):
                user2 = users[j]
                if i != j:
                    if gender == Constant.Male.value:
                        if user2.gender == Constant.Female.value:
                            self.userGraph[user.id].append(users[j].id)
                    if gender == Constant.Female.value:
                        if user2.gender == Constant.Male.value:
                            self.userGraph[user.id].append(users[j].id)

        self.userGraph = self.sort_edges(self.userGraph, self.userNodes)
        return self.userGraph

    def sort_edges(self, graph, nodes):
        for key, value in enumerate(graph):
            user = nodes[value]
            edges = [nodes[node] for node in graph[value]]
            age = user.age
            interests = user.interests
            edges = sorted(edges, key=lambda x: (x.age-age))
            edges = sorted(edges, key=lambda x: (len(x.interests) - len(interests)))
            graph[value] = edges
        return graph

    def get_top_matches(self, graph, userName, nodes, limit):
        id = ""
        for key, value in enumerate(nodes):
            if nodes[value].name == userName:
                id = value

        edges = graph[id][:limit]

        res = []
        for edge in edges:
            res.append(edge.name)

        return res

users = [
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
m = Main()
n = m.registerUsers(users)
g = m.buildGraph(n)
print(m.get_top_matches(g, "UserB", n, 2))
