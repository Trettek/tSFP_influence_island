## Background
"Influence Island" is a mini-game within The Sims Freeplay that rewards winning players with a set of exclusive in-game items.
Here, I model this mini-game as a finite sequential stochastic control problem, with the primary goal of finding the optimal set of user actions to win the full set of exclusive in-game items without spending in game currency. As a secondary goal, I create several models that account for variability in whether in-game currency is spent, whether certain non-optimal actions were taken, whether your goal is to win the full set of exclusive in-game items, or simply some of them, etc. Just for fun!

## Explanation (in progress)
The state at any moment is $S = (t,s,k)$ 
where $t = trial$, $s = score$, $k = \text{remaining uses on "convince" user action.}$

Available actions are defined as $a_1 = \text{small increase } U(1,20), a_2 = \text{large increase } U(20,45), a_3 = \text{very small increase } U(2,9), a_4 = \text{convince } U(2,9)$ 

Value function:

$$
V(t,s,k) =
\max_{a \in A}
\mathbb{E}[V(t, s, k)]
$$
