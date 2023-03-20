
def test_simple_user(simple_user):
    assert simple_user.email == 'test@test.com'
    assert simple_user.is_admin is False


def test_admin_user(admin_user):
    assert admin_user.email == 'test_admin@test.com'
    assert admin_user.is_admin is True
