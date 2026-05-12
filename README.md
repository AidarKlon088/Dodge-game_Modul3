#  AI Dodge Learning (Q-Learning Game)

This project is a simple AI game built with Python where an agent learns to dodge obstacles using **Reinforcement Learning (Q-Learning)**.

---

##  Demo

The AI learns how to survive longer by avoiding collisions with falling blocks.

A demo video is available in the `templates/` folder.

---

##  How it works

The AI uses **Q-Learning**:

- It observes the current state (position difference between player and obstacle)
- Chooses an action:
  - left
  - right
  - stay
- Receives a reward:
  -  -100 if collision happens
  -  positive reward for surviving
- Updates its Q-table over time

---

##  Tech Stack

- Python 
- Pygame 
- Matplotlib 

---

## Project Structure


Module3 Ai/
│
├── train.py # Main AI training game
├── requirements.txt # Dependencies
├── templates/
│ ├── index.html # Simple HTML page
│ └── video.mp4 # Demo video


---

##  How to run

### 1. Install dependencies

```bash
pip install -r requirements.txt
2. Run the game
python train.py
Learning Process

The AI improves over time:

At first: random movement 
Later: learns to dodge better 
Finally: survives longer and stabilizes 
 Goal

Reach 50+ dodges without collision and see the PRIZE animation 🏆

 Notes
This is a basic reinforcement learning project
Uses simple Q-table (not neural network)
Good for understanding RL fundamentals
