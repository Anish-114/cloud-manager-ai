import random
from .models import Observation, Action, Reward

class CloudManagerEnv:
    def __init__(self):
        self.max_load_encountered = 0.0
        self.reset()

    def reset(self) -> Observation:
        """SAB KUCH RESET: 1555 servers ko turant 1 par lata hai."""
        self.cpu_load = 40.0
        self.servers = 1 # Yahan force reset hai
        self.total_cost = 0.0
        self.steps = 0
        self.max_load_encountered = 40.0
        return self.state()

    def state(self) -> Observation:
        return Observation(
            cpu_load=round(self.cpu_load, 2),
            active_servers=self.servers,
            cost_incurred=round(self.total_cost, 2),
            is_crashed=(self.cpu_load > 98.0)
        )

    def step(self, action: Action):
        self.steps += 1
        
        # 1. Action Logic with MAX 10 LIMIT
        if action.action_id == 1 and self.servers < 10: 
            self.servers += 1
        elif action.action_id == 2 and self.servers > 1:
            self.servers -= 1
            
        # SAFETY: Agar pichle session se servers 10 se zyada bache hain
        if self.servers > 10:
            self.servers = 1

        # 2. Physics: Servers badhne par load kam hona chahiye
        traffic_noise = random.uniform(-5, 15)
        base_load = (self.cpu_load + traffic_noise)
        # Proper scaling formula
        self.cpu_load = max(10, min(100, base_load / (self.servers * 0.5 + 0.5)))
        
        self.total_cost += (self.servers * 0.15) 
        self.max_load_encountered = max(self.max_load_encountered, self.cpu_load)

        # 3. Reward
        if 40 <= self.cpu_load <= 75:
            reward_val, msg = 1.0, "Optimized"
        elif self.cpu_load > 90:
            reward_val, msg = -2.5, "Overload!"
        else:
            reward_val, msg = 0.3, "Inefficient"

        done = self.steps >= 100 or self.cpu_load > 99.0
        return self.state(), Reward(value=reward_val, explanation=msg), done, {"max_load": self.max_load_encountered}
