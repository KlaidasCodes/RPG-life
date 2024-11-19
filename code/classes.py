class Human:
    def __init__(self, name, age, password, sex):
        self.name = name
        self.age = age
        self.skills = {}
        self.password = password
        self.total_exp = 0
        self.sex = sex

    def add_skill(self, skill, exp=0, level=1):
        self.skills[skill.skill] = {"exp": skill.exp, "level": skill.level}

    def update_total_exp(self):
        for skill in self.skills:
            self.total_exp += self.skills[skill]
        return self.total_exp

    def display_as_dict(self):
        pass


class Skill:
    def __init__(self, skill, level=0, exp=0):
        self.skill = skill # the skill name like reading
        self.level = level
        self.exp = exp

    def add_exp(self, amount=1):
        self.exp += amount
        return self.exp

    def add_level(self, amount=1):
        self.level += amount
        return self.level

    def _change_skill_name(self, new_name):
        self.skill = new_name
