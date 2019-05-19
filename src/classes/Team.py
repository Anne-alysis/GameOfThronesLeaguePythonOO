class Team:
    def __init__(self, team_name: str, real_name: str, split_preference: str, pay_type: str):
        self.team_name = team_name
        self.real_name = real_name
        self.split_preference = split_preference
        self.pay_type = pay_type
        self.total_score = 0

    def add_to_total_score(self, addition: int):
        self.total_score += addition
        return None

    def __str__(self):
        return f"Team: {self.team_name}; teal name: {self.real_name}; " \
            f"split preference: {self.split_preference}; pay type: {self.pay_type}"
