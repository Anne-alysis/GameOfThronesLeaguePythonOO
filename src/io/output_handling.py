from typing import List

import pandas as pd

import src.classes.Team as t


def extract_team_scores(team_class_list: List[t.Team], output_file_path: str) -> None:
    scored_df = pd.DataFrame([[team.team_name, team.total_score] for team in team_class_list],
                             columns=["Team", "Total Score"])
    scored_and_ranked_df = scored_df.assign(Rank=lambda x: x["Total Score"].rank(ascending=False, method="max")) \
        .sort_values(by="Rank")
    scored_and_ranked_df.to_csv(output_file_path)

    return None
