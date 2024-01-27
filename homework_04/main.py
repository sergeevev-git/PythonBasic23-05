"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from typing import List
from models import Base, User, Post, async_session, async_engine
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data

from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(session: AsyncSession, username: str, email: str | None =
None) -> User:
	user = User(username = username, email = email)
	print(user)
	session.add(user)
	await session.commit()
	print("saved user")
	# await session.refresh()
	print("user details:", user)
	return user


async def create_users(
		session: AsyncSession,
		users: list
) -> list[User]:
	added_users = [
		User(
			id = user.id,
			name = user.name,
			username = user.username,
			email = user.email
		)
		for user in users
	]
	session.add_all(added_users)
	await session.commit()
	print("saved users:", added_users)
	return added_users


async def create_post(session: AsyncSession, title: str, user_id: int) -> Post:
	post = Post(
		title = title,
		user_id = user_id,
	)
	session.add(post)
	await session.commit()
	print(post)
	return post


async def create_posts(
		session: AsyncSession,
		posts: list
) -> list[Post]:
	added_posts = [
		Post(
			id = post.id,
			name = post.name,
			username = post.username,
			email = post.email
		)
		for post in posts
	]
	session.add_all(added_posts)
	await session.commit()
	print("saved posts:", added_posts)
	return added_posts


async def async_main():
	# Base.metadata.create_all(bind = Async_engine)
	users_data: List[dict]
	posts_data: List[dict]
	users_data, posts_data = await asyncio.gather(
		fetch_users_data(),
		fetch_posts_data(),
	)
	# print(users_data)
	# print(posts_data)
	async with async_session() as session:
		await create_users(session, users_data)
		await create_posts(session, posts_data)
	session.close()


# log.info("result: %s", res)
# log.info("Finish main")


def main():
	asyncio.run(async_main())


if __name__ == "__main__":
	main()
