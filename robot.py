import time

class Robot:
    def __init__(self, start_position):
        self.position = start_position

    def get_position(self):
        return self.position

    def move_to(self, next_position):
        """
        Simulates motor actuation.
        In real hardware, motor commands will be sent here.
        """
        self.position = next_position
        print(f"➡ Robot moved to {self.position}")
        time.sleep(0.5)

    def follow_path(self, path):
        """
        Follows a given path step-by-step.
        """
        print("\n🚗 Robot starting movement...\n")
        for step in path[1:]:
            self.move_to(step)

    def stop(self):
        """
        Emergency stop logic (for future use).
        """
        print("⛔ Robot stopped due to obstacle")
