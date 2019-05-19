import sys

import src.calculations.calculations as calc
import src.io.input_handling as ih
import src.io.output_handling as oh

# set directory path for all files
directory_path = "resources"
# set yaml path that includes specific file paths
yaml_path = "file_paths.yaml"


def main():
    week: int = 1 if len(sys.argv) == 1 else int(sys.argv[1])
    print(f"This is episode: {week}")

    print("Reading in configuration file paths... ")
    full_file_paths = ih.read_yaml(directory_path, yaml_path)

    # read in all data, instantiate list of classes for teams and responses
    print("Reading in raw input")
    team_class_list, questions_class_list = ih.read_raw_input(full_file_paths['raw_responses_file'])

    print("Reading in correct answers...")
    correct_answer_dict = ih.read_correct_answers(full_file_paths['correct_answer_file'])

    print("Scoring the responses...")
    calc.score_responses(correct_answer_dict, questions_class_list, team_class_list)

    print("Totalling scores and writing to disk... ")
    oh.extract_team_scores(team_class_list, full_file_paths["results_file"])


if __name__ == "__main__":
    main()
