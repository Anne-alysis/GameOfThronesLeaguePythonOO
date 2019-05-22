
"""
This object holds all team information.  Initially, this includes their metadata and eventually gets
updated to hold their total score.

- team_name: name of the team
- real_name: full name of person who submitted form
- split_preference: whether the person wants winner-take-all or split the top 3 winners
- pay_type: free or paying team
- total_score: initially set to 0, will be updated throughout
"""


class Team:
    def __init__(self, team_name: str, real_name: str, split_preference: str, pay_type: str):
        self.team_name = team_name
        self.real_name = real_name
        self.split_preference = split_preference
        self.pay_type = pay_type
        self.total_score = 0

    def add_to_total_score(self, addition: int):
        """
        mechanism to update the score from 0 to the total for a given question

        :param addition: point value accrued for a given question (0 if incorrect)
        :return: updated score
        """
        self.total_score += addition

    def __str__(self):
        base_string = f"Team: {self.team_name}; team name: {self.real_name}; " \
            f"split preference: {self.split_preference}; pay type: {self.pay_type}"
        if self.total_score == 0:
            return base_string
        else:
            return f"{base_string}; total score: {self.total_score}"
