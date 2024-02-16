from models import db, User


def get_user_list() -> list[User]:
	return User.query.all()


def get_user_by_id(user_id: str) -> User:
	return User.query.get_or_404(
		user_id,
		f"user #{user_id} not found",
	)


def create_user(name: str, username: str, email: str) -> User:
	user = User(
		name = name,
		username = username,
		email = email
	)
	db.session.add(user)
	db.session.commit()
	return user


def delete_user(user: User) -> None:
	# 1й вариант
	# product = get_product_by_id(product_id)
	db.session.delete(user)
	db.session.commit()

# 2й вариант
# del_stmt = delete(Product).where(Product.id == product_id)
# db.session.execute(del_stmt)
# db.session.commit()
