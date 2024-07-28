from sqlalchemy import select

from kaoz.models import UserDB


def test_create_user(session):
    user = UserDB(
        username='Allandarus',
        email='allandarus@kaoz.com',
        password='senha',
    )
    session.add(user)
    session.commit()
    result = session.scalar(
        select(UserDB).where(UserDB.email == 'allandarus@kaoz.com')
    )

    assert result.username == 'Allandarus'
