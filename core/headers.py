from user_agents import user_agent 

import random

headers = { 
    "User-Agents": random.choice(user_agent)
}