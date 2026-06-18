

import networkx as nx
import matplotlib.pyplot as plt


def create_dependency_graph(
    package_name,
    dependencies
):

    graph = nx.DiGraph()

    graph.add_node(package_name)

    for dep in dependencies:

        graph.add_node(dep)

        graph.add_edge(
            package_name,
            dep
        )

    plt.figure(figsize=(8, 6))

    nx.draw(
        graph,
        with_labels=True
    )

    filename = (
        f"reports/{package_name}_graph.png"
    )

    plt.savefig(filename)

    plt.close()

    return filename
