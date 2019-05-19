class Question:
    def __init__(self, question_number: str, full_text: str, list_of_responses: list):
        self.question_number = question_number
        self.full_text = full_text
        self.points = self._get_points()
        self.simple_text = self._get_simple_text()
        self.list_of_responses = list_of_responses
        self.correct_answer = None

    def _get_points(self):
        if "(" in self.full_text:
            temp = self.full_text.split("(")[1]
            return int(temp.split(" ")[0])
        else:
            return 0

    def _get_simple_text(self):
        character_to_save = f"[{self.full_text.split('[')[1]}" if "[" in self.full_text else ""

        return (self.full_text.split("(")[0] + character_to_save).strip()

    def set_correct_answer(self, answer: str):
        self.correct_answer = answer
        return None

    def __iter__(self):
        return iter([self.question_number, self.simple_text, self.points])

    def __str__(self):
        return f"{self.question_number}: {self.simple_text}; {self.points} points"
