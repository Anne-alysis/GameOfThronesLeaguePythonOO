import csv
from typing import List, Dict

import pandas as pd
import yaml

import src.classes.Question as q
import src.classes.Response as r
import src.classes.Team as t

"""
This module handles all the reading in of configurations, raw responses, correct answers.  Some data cleaning as well.  
"""


def read_yaml(directory_path: str, yaml_path: str):
    """
    Reads in configuration file with all the various file paths for input and outputs.

    :param directory_path: base directory
    :param yaml_path: stub of yaml path
    :return: dictionary of file types to files
    """
    # read in file path stubs from yaml configuration
    with open(f"{directory_path}/{yaml_path}", 'r') as stream:
        file_stubs = yaml.safe_load(stream)

    return {key: f"{directory_path}/{value}" for (key, value) in file_stubs.items()}


def read_raw_input(full_file_paths: Dict[str, str]) -> (List[t.Team], List[q.Question]):
    """
    Workhorse for reading in raw files and reshaping.  Returns tuple of objects, without any correct
    answer information yet filled out.  Only what was available before the season began.

    :param full_file_paths: dictionary of files
    :return: list of Team objects and list of Question objects
    """
    raw_responses_df = pd.read_csv(full_file_paths['raw_responses_file']).drop(columns="Timestamp")

    questions_dict = get_questions_mapping(raw_responses_df)

    renamed_raw_response_df = rename_columns(raw_responses_df, questions_dict)

    # populate the list of Teams
    teams_class_list = [t.Team(renamed_raw_response_df.team_name[i],
                               renamed_raw_response_df.real_name[i],
                               renamed_raw_response_df.split_preference[i],
                               renamed_raw_response_df.pay_type[i], )
                        for i in range(renamed_raw_response_df.shape[0])]

    questions_class_list = [q.Question(number, full_text, get_response_for_question(renamed_raw_response_df, number))
                            for number, full_text in questions_dict.items()]

    write_answer_structure(full_file_paths["answer_structure_file"], questions_class_list)

    return teams_class_list, questions_class_list


def write_answer_structure(output_file_path: str, questions_class_list: List[q.Question]) -> None:
    """
    Writes the questions with numbers to an external file for week-by-week updates, based on events.

    :param output_file_path: where to write structure
    :param questions_class_list: question numbers, text, points, etc.
    :return: None
    """
    with open(output_file_path, 'w', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(["number", "simple_text", "points"])
        for question in questions_class_list:
            writer.writerow(list(question))
    return None


def rename_columns(df: pd.DataFrame, questions_dict: Dict[str, str]) -> pd.DataFrame:
    """
    Returns a dataframe with more standardized column names for the questions by numbering them with zero padding.

    :param df: uncleaned data frame
    :param questions_dict: mapping of column numbers to question text
    :return: df with cleaned columns
    """
    new_column_names = ["real_name", "team_name", "pay_type", "split_preference"] + list(questions_dict.keys())
    df.columns = new_column_names

    return df


def get_questions_mapping(df: pd.DataFrame) -> Dict[str, str]:
    """
    Returns a dictionary of question numbers to question text.

    :param df: raw data frame
    :return: dictionary mapping of numbers to text.
    """
    question_number_range = list(range(0, df.shape[1] - 4))
    numbered_question_names = ['Q{:02d}'.format(i) for i in question_number_range]
    question_text = list(df.columns[4:])

    return dict(zip(numbered_question_names, question_text))


def get_response_for_question(df: pd.DataFrame, question_number: str) -> List[r.Response]:
    """
    returns a list of Response objects for a given question and all team's response.

    :param df: cleaned initial response df
    :param question_number: number of question
    :return: list of Response objects
    """
    return [r.Response(df.team_name[i], question_number, df[question_number][i]) for i in range(df.shape[0])]


def read_correct_answers(input_file_path: str) -> Dict[str, str]:
    """
    Reads in correct answers and returns a dictionary of question numbers (keys) to text (values)
    :param input_file_path: filename for correct answers
    :return:
    """
    # read in correct answers and create dictionary lookup
    correct_answer_df = pd.read_excel(input_file_path)
    filtered_correct_df = correct_answer_df[correct_answer_df.include]
    return dict(zip(filtered_correct_df.question_number, filtered_correct_df.correct_answer))
