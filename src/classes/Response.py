"""
This class holds each individual response for a given question and a team.
- team: name of the team
- question_number: ID for each question (e.g., "QXX", where XX is the zero-padded question number)
- response: team's response text for the given question
- is_correct: initially None, this boolean will be populated as a question is available to be scored
- score: point value that will be added to total for a question; default is 0.

Note: Response objects are only used within the Question object as its 'list_of_responses'

"""


class Response:
    def __init__(self, team: str, question_number: str, response: str):
        self.team = team
        self.question_number = question_number
        self.response = response
        self.is_correct = None
        self.score = 0

    def set_is_correct(self, correct_answer: str, points: int):
        """
        Sets the boolean value for the `is_correct` instance variable, given a correct answer

        :param correct_answer: string for correct answer
        :param points: point value for the question
        :return: updates the instance variable `is_correct` and the `score`
        """
        self.is_correct = self.response in correct_answer
        self.score = self.is_correct * points
        return None

    def __str__(self):
        base_string = f"{self.team}'s response for question {self.question_number}: {self.response}"
        if self.is_correct is None:
            return base_string
        if self.is_correct is not None:
            return f"{base_string}; correct = {self.is_correct}; score = {self.score}"
