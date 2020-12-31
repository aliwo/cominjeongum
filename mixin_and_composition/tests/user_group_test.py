import pytest

from mixin_and_composition.user_group import Group, User


def test_user_join_group():
    '''
    유저는 그룹에 가입할 수 있다.
    '''

    # given
    fred = User(1, 'fred')
    soccer_group = Group(1, 'soccer')

    # when
    fred.join_group(soccer_group)

    # then
    assert fred.groups[0] == soccer_group


def test_max_group_cnt():
    '''
    MAX_GROUP_CNT 를 초과하면 더 이상 가입할 수 없다.
    '''

    # given
    fred = User(1, 'fred')
    groups = [Group(i, str(i)) for i in range(1, User.MAX_GROUP_CNT+1)]
    for group in groups:
        fred.join_group(group)

    # when
    soccer_group = Group(1, 'soccer')

    # then
    with pytest.raises(ValueError):
        fred.join_group(soccer_group)

