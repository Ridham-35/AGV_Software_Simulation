import time
from queue import PriorityQueue

# =========================
# SIMULATED MAP (SENSORS)
# =========================
# 0 = free space, 1 = obstacle
grid_map = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)


# =========================
# PATH PLANNING (A*)
# =========================
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = PriorityQueue()
    pq.put((0, start))

    came_from = {}
    cost_so_far = {start: 0}

    while not pq.empty():
        _, current = pq.get()

        if current == goal:
            break

        x, y = current
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = cost_so_far[current] + 1
                if (nx, ny) not in cost_so_far:
                    cost_so_far[(nx, ny)] = new_cost
                    priority = new_cost + abs(goal[0]-nx) + abs(goal[1]-ny)
                    pq.put((priority, (nx, ny)))
                    came_from[(nx, ny)] = current

    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = came_from[cur]
    path.append(start)
    path.reverse()

    return path


# =========================
# ROBOT CONTROL + ACTUATION
# =========================
def move_robot(grid, path, goal):
    print("\n🚗 Robot starting movement...\n")
    current_position = path[0]

    for step in path[1:]:
        # Simulate obstacle appearing dynamically
        if step == (2, 2):
            print("⚠ Obstacle detected at (2,2)")
            grid[2][2] = 1

            print("🔁 Replanning path...\n")
            new_path = astar(grid, current_position, goal)
            move_robot(grid, new_path, goal)
            return

        print(f"➡ Robot moved to {step}")
        current_position = step
        time.sleep(0.5)

    print("\n✅ Destination reached successfully!")


# =========================
# MAIN DEMO
# =========================
if __name__ == "__main__":
    print("\n===== AGV SOFTWARE SIMULATION DEMO =====")
    print("Start Position:", start)
    print("Goal Position:", goal)

    print("\n🧠 Planning initial path...")
    path = astar(grid_map, start, goal)

    print("\n📍 Planned Path:")
    print(path)

    move_robot(grid_map, path, goal)
