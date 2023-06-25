from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.models.user import User


async def add_user(user_id: int,
                   first_name: str,
                   last_name: str,
                   username: str,
                   status: str,
                   native_language: str,
                   language_to_learn: str,
                   words: str):
    try:
        user = User(user_id=user_id,
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    status=status,
                    native_language=native_language,
                    language_to_learn=language_to_learn,
                    words=words
                    )
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def select_all_users():
    return await User.query.gino.all()


async def count_users():
    return await db.func.count(User.user_id).gino.scalar()


async def select_user(user_id):
    return await User.query.where(User.user_id == user_id).gino.first()


async def update_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()


async def update_to_learn(user_id, language_to_learn):
    user = await select_user(user_id)
    await user.update(language_to_learn=language_to_learn).apply()


async def update_native(user_id, native_language):
    user = await select_user(user_id)
    await user.update(native_language=native_language).apply()


async def update_words(user_id, words):
    user = await select_user(user_id)
    if words != '':
        words = user.words + ', ' + words

    if len(words) >= 200:
        words = words[-200:]
        first_space_index = words.find(' ')

        if not first_space_index:
            words = ''
        else:
            if first_space_index != 0:
                words = words[first_space_index:]

    await user.update(words=words).apply()
