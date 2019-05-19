import src.classes.Question as q
import src.classes.Team as t
from typing import Dict, List

"""
Note, each of these populating motions is a nested loop.  Must find a more efficient way
of population this information throughout the class instances.
"""


def score_responses(correct_answer_dict: Dict[str, str], questions_class_list: List[q.Question],
                    team_class_list: List[t.Team]) -> List[t.Team]:
    # populate the correct answers to the question instances
    [question.set_correct_answer(correct_answer_dict[question.question_number])
     for question in questions_class_list
     if question.question_number in correct_answer_dict.keys()]

    # populate is_correct boolean through each teams' responses
    [response.set_is_correct(question.correct_answer, question.points)
     for question in questions_class_list
     for response in question.list_of_responses
     if question.correct_answer is not None]

    # populate total score on team level
    [team.add_to_total_score(response.score)
     for team in team_class_list
     for question in questions_class_list
     for response in question.list_of_responses
     if question.correct_answer is not None and team.team_name == response.team]

    return team_class_list
