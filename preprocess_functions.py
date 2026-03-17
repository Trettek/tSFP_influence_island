import pandas as pd
import numpy as np
import os

# -----------
# basic loads
# -----------

def load_actions(folder_path):
    
    actions_path = os.path.join(folder_path, "actions.csv")
    actions_df = pd.read_csv(actions_path)

    actions_dict = {}

    for _, row in actions_df.iterrows():
        action = row["action"]
        min_val = int(row["min"])
        max_val = int(row["max"])

        actions_dict[action] = np.arange(min_val, max_val + 1)

    return actions_dict


def load_rounds(folder_path):

    rounds_path = os.path.join(folder_path, "rounds.csv")
    round_df = pd.read_csv(rounds_path)

    round_map = {}

    for r in round_df["round"].unique():
        
        sub = round_df[round_df["round"] == r].sort_values("trial")

        trials_list = []

        for _, row in sub.iterrows():

            if pd.isna(row["convince_low"]):
                conv = None
            else:
                conv = (
                    int(row["convince_low"]),
                    int(row["convince_high"])
                )

            win = (
                int(row["win_lower"]),
                int(row["win_upper"])
            )

            trials_list.append({
                "conv": conv,
                "win": win
            })

        round_map[r] = trials_list

    return round_map


def load_vs_limit(folder_path):
    df = pd.read_csv(os.path.join(folder_path, "convince.csv"))
    return int(df["n_convince"].iloc[0])


# ----------------------
# probability assumptions
# ----------------------

def generate_uniform_action_probs(actions):
    return {
        k: [1 / len(v)] * len(v)
        for k, v in actions.items()
    }


def default_p_convince():
    return 0.5


# load in game config from .csvs   
def load_game_config(folder_path):

    # TODO: make probability assumptions mutable 

    actions = load_actions(folder_path)
    round_map = load_rounds(folder_path)
    vs_limit = load_vs_limit(folder_path)

    action_probs = generate_uniform_action_probs(actions)
    p_convince = default_p_convince()

    return actions, action_probs, round_map, vs_limit, p_convince
