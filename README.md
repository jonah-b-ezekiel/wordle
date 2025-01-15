# Wordle Solver

Welcome to the Wordle Solver! This project allows you to implement your own Wordle-solving strategy and test its effectiveness.

## How to Get Started

1. **Generate Data**  
   - Before playing or testing, run the `utils/generate_data` script to generate the necessary data files:  
     ```bash
     python utils/generate_data.py
     ```

2. **Implement Your Strategy**  
   - Edit the `get_guess` function in `guesser.py`.  

3. **Play the Solver**  
   - Run `play.py` to interactively play Wordle using your strategy:  
     ```bash
     python play.py
     ```

4. **Test Your Strategy**  
   - Run `test.py` to evaluate the average number of guesses your strategy takes to solve all possible Wordle answers:  
     ```bash
     python test.py
     ```

## Leaderboard

| Rank | Strategy Author     | Average Guesses |
|------|---------------------|-----------------|
| 1    | Jonah               | 3.48            |
| 2    |                     |                 |
| 3    |                     |                 |
