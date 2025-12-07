# 1. Water Container Balancer

A Python program that models interconnected water containers. When containers are connected, their water levels equalize across the entire connected structure. Adding water to any container triggers redistribution across its group.

# 2. The Problem

You have multiple containers that may or may not be connected. When two containers connect, they form a shared system where the water level must be identical everywhere. Disconnecting splits the system, and each resulting part equalizes independently.

This project simulates that behavior programmatically.

# 3. How the System Works

Each container stores some water. Containers can be connected or disconnected at any moment. Whenever the structure changes—by adding water, connecting, or disconnecting—the system identifies all containers in the same connected component and redistributes water equally among them.

# 4. Data Structure and Algorithm

The containers form an undirected graph, where each container keeps a set of neighbors. This structure allows fast lookups and prevents duplicates. When redistribution is needed, a graph traversal (using a simple stack for DFS) gathers all containers in the connected component. Their water values are summed, divided evenly, and assigned back to every container in that group.
This ensures automatic balancing in a minimal and efficient way.

# 5. Running the Code

Run the program using the command python containers.py. The script will run the test scenarios.
