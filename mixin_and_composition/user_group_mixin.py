
class UserGroupMixin:
    MAX_GROUP_CNT = 5

    def __init__(self):
        self.groups = []

    def join_group(self, group):
        if len(self.groups) >= self.MAX_GROUP_CNT:
            raise ValueError
        self.groups.append(group)


class User(UserGroupMixin):

    def __init__(self, id_, name):
        super(User, self).__init__()
        self.id_ = id_
        self.name = name



class Group:

    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name

