import asyncio
from typing import List

from fetch_data import fetch_users_data, fetch_posts_data


async def async_mock_loader():
	await init_models()
	
	users_data: List[dict]
	posts_data: List[dict]
	
	users_data, posts_data = await asyncio.gather(
		fetch_users_data(),
		fetch_posts_data(),
	)
	
	async with Session() as session:
		await create_users(session, users_data)
		await create_posts(session, posts_data)
		await session.close()


def mock_loader():
	asyncio.run(async_main())
