
class User:
    MAX_GROUP_CNT = 5

    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name
        self.groups = []

    def join_group(self, group):
        if len(self.groups) >= self.MAX_GROUP_CNT:
            raise ValueError
        self.groups.append(group)


class Group:

    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name

