
class GroupBehavior:
    MAX_GROUP_CNT = 5

    def __init__(self, user):
        self.user = user
        self.groups = []

    def join_group(self, group):
        if len(self.groups) >= self.MAX_GROUP_CNT:
            raise ValueError
        self.groups.append(group)


class User:

    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name
        self.group_behavior = GroupBehavior(self)

    @property
    def groups(self):
        return self.group_behavior.groups

    def join_group(self, group):
        self.group_behavior.join_group(group)


class Group:

    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name

