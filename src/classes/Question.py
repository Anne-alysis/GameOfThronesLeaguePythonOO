"""
This class holds the information for each individual question in the form.  This includes:
- question_number: number of the question (e.g, "QXX", where XX is the number)
- full_text: original full text from the form
- points: parsed point value from full_text
- simple_text: question text with points extracted
- list_of_responses: a list of Response objects for each Team
- correct_answer: a string of the answer for the given question

Note: correct answers are not known from the outset.  These will be updated week-over-week.
"""


class Question:

    def __init__(self, question_number: str, full_text: str, list_of_responses: list):
        self.question_number = question_number
        self.full_text = full_text
        self.points = self._get_points()
        self.simple_text = self._get_simple_text()
        self.list_of_responses = list_of_responses
        self.correct_answer = None

    def _get_points(self):
        """
        Extracts points values from the question's full text

        :return: question's point value
        """
        if "(" in self.full_text:
            temp = self.full_text.split("(")[1]
            return int(temp.split(" ")[0])
        else:
            return 0

    def _get_simple_text(self):
        """
        Cleans up the original text question by removing the point value and
        rearranging the character named after the point value, if applicable

        :return: cleaned question
        """
        character_to_save = f"[{self.full_text.split('[')[1]}" if "[" in self.full_text else ""

        return (self.full_text.split("(")[0] + character_to_save).strip()

    def set_correct_answer(self, answer: str):
        """
        Sets the correct answer for the given question.

        :param answer: correct answer text
        """
        self.correct_answer = answer
        return None

    def __iter__(self):
        return iter([self.question_number, self.simple_text, self.points])

    def __str__(self):
        return f"{self.question_number}: {self.simple_text}; {self.points} points"
