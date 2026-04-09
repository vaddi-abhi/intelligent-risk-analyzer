import networkx as nx

def build_graph(package, dependencies):
    graph = nx.DiGraph()

    for dep in dependencies:
        graph.add_edge(package, dep)

    return graph


def calculate_risk(vulnerabilities, license_name):
    risk = len(vulnerabilities) * 5

    if license_name and "GPL" in license_name.upper():
        risk += 10

    return risk