from pydantic import BaseModel
from typing import Optional

class Observation(BaseModel):
    cpu_load: float
    active_servers: int
    cost_incurred: float
    is_crashed: bool

class Action(BaseModel):
    action_id: int  # 0: No Action, 1: Add Server, 2: Remove Server

class Reward(BaseModel):
    value: float
    explanation: str
