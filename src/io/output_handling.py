from typing import List

import pandas as pd

import src.classes.Team as t


def extract_team_scores(team_class_list: List[t.Team], output_file_path: str) -> None:
    """
    Converts the list of Team classes into a dataframe for ranking and writes the output to a csv.

    :param team_class_list: list of Team with a total_score updated
    :param output_file_path: file to write the results to.
    :return: None
    """
    scored_df = pd.DataFrame([[team.team_name, team.total_score] for team in team_class_list],
                             columns=["Team", "Total Score"])
    
    scored_and_ranked_df = scored_df \
        .assign(Rank=lambda x: x["Total Score"].rank(ascending=False, method="max")) \
        .sort_values(by="Rank")

    scored_and_ranked_df.to_csv(output_file_path)

    return None
