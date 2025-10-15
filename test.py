import json
import matplotlib.pyplot as plt

# Load the JSON file
with open('test_trajectories.json', 'r') as f:
    trajectories = json.load(f)

# Plot lactate and actions for each episode
for ep_idx, traj in enumerate(trajectories):
    lactate = [state[4] for state in traj['states']]  # Lactate is index 4
    actions = traj['actions']
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(lactate, marker='o')
    plt.title(f'Episode {ep_idx+1} - Lactate')
    plt.xlabel('Time step')
    plt.ylabel('Lactate (mmol/L)')
    plt.subplot(1, 2, 2)
    plt.plot(actions, marker='x', color='orange')
    plt.title(f'Episode {ep_idx+1} - Actions')
    plt.xlabel('Time step')
    plt.ylabel('Action index')
    plt.tight_layout()
    plt.show()