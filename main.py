import sys

import src.calculations.calculations as calc
import src.io.input_handling as ih
import src.io.output_handling as oh

# set directory path for all files
directory_path = "resources"


def main():
    week: int = 1 if len(sys.argv) == 1 else int(sys.argv[1])
    print(f"This is episode: {week}")

    full_file_paths = ih.read_yaml(directory_path, "file_paths.yaml")

    # read in all data, instantiate list of classes for teams and responses
    team_class_list, questions_class_list = ih.read_raw_input(full_file_paths['raw_responses_file'])

    correct_answer_dict = ih.read_correct_answers(full_file_paths['correct_answer_file'])

    calc.do_calculations(correct_answer_dict, questions_class_list, team_class_list)

    oh.extract_final_scores(team_class_list, full_file_paths["results_file"])


if __name__ == "__main__":
    main()
