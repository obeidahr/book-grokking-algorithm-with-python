#For each of these algorithms, say whether it’s a greedy algorithm or not.
#8.3 Quicksort not greedy
#8.4 Breadth-first search is greedy
#8.5 Dijkstra’s algorithm is greedy

states_needed = set(['mt', 'wa', 'or', "id", "nv","ut","ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)