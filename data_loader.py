# data_loader.py
import tsplib95

def load_problem(problem_file):
    problem = tsplib95.load(problem_file)
    n_nodes = problem.dimension
    nodes = list(problem.get_nodes())
    node_coords = {node: problem.node_coords[node] for node in nodes}
    return n_nodes, nodes, node_coords, problem
