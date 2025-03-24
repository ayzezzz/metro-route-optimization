# Driverless Metro Simulation (Route Optimization)

This project aims to develop a simulation that can find the **least transfer** and **fastest** routes in a metro network. **Graph data structure**, **BFS (Breadth-First Search)**, and **A* algorithm** are used for route optimization.

## 🚀 Project Objectives

- Model the metro network using a **graph data structure**.
- Find the least transfer route using the **BFS algorithm**.
- Determine the fastest route using the **A* algorithm**.
- Develop problem-solving skills for **real-world applications**.

## 🛠 Technologies and Libraries Used

- **Python 3**: The primary programming language for this project.
- **Collections (deque, defaultdict)**: Used for queue structures and data modeling in BFS.
- **Heapq**: Used for priority queue (min heap) management in the A* algorithm.

## 📌 Algorithm Workflow

### BFS (Finding the Least Transfer Route)
BFS is a **graph traversal algorithm** used to find the **shortest path**. In this project, it is applied to determine **the least transfer route**.

- **Queue (deque) is used**: The most prioritized station is processed first.
- **Visited stations are tracked**.
- **Neighboring stations are explored and added to the queue**.
- **The route is returned when the target station is reached**.

### A* (Finding the Fastest Route)
The A* algorithm is a **priority queue-based algorithm** used to find the shortest travel time between two points.

- **Min heap (heapq) is used**: The station with the lowest cost (shortest travel time) is processed first.
- **Visited stations are tracked**.
- **Total travel time is calculated to determine the fastest route**.

## 📝 Example Usage

A sample metro network has been created:

- **Red Line**: Kızılay ↔ Ulus ↔ Demetevler ↔ OSB
- **Blue Line**: AŞTİ ↔ Kızılay ↔ Sıhhiye ↔ Gar
- **Orange Line**: Batıkent ↔ Demetevler ↔ Gar ↔ Keçiören

Example scenarios:

1. **From AŞTİ to OSB**
   - Least transfer route: `AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB`
   - Fastest route (time): `AŞTİ -> Kızılay -> Demetevler -> OSB`

2. **From Batıkent to Keçiören**
   - Least transfer route: `Batıkent -> Demetevler -> Gar -> Keçiören`
   - Fastest route (time): `Batıkent -> Demetevler -> Gar -> Keçiören`

3. **From Keçiören to AŞTİ**
   - Least transfer route: `Keçiören -> Gar -> Kızılay -> AŞTİ`
   - Fastest route (time): `Keçiören -> Gar -> Kızılay -> AŞTİ`

## 📌 Future Enhancements

- **Support for larger metro networks**.
- **Improved user experience with UI and visualization**.
- **Integration with real-time traffic data**.

## 📂 Installation and Execution

1. Download and extract the project files.
2. Ensure Python 3 is installed.
3. Run the following command in the terminal or command prompt:

   ```bash
   python ZerrinAyaz_MetroSimulation.py
