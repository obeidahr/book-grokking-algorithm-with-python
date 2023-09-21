from collections import deque

def perName(name):
    return name[-1] == "m"

graph = {}
graph["maria"] = ["larina","zen","mom","jory"]
graph["larina"] = ["lemas","jod"]
graph["zen"] = ["zena","jod"]
graph["mom"] = ["larina"]
graph["jory"] = ["jod"]
graph["lemas"] = ["rem","jod"]
graph["jod"] = ["mom"]
graph["zena"] = []
graph["rem"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if perName(person):
                print('this is '+ person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


name = "maria"
search(name)