import os 

from peewee import * 


__all__ = ['Account']


dir_path = os.path.dirname(os.path.realpath(__file__))
db = SqliteDatabase(os.path.join(dir_path, 'microblog.db'))


class BaseModel(Model):
	class Meta:
		database = db


class Account(BaseModel):
	username = CharField(unique=True)
	token = CharField(unique=True)
	last_post_viewed = CharField(null=True)
	is_current = BooleanField(null=False, default=False)

	def exists(username):
		return Account.select().where(Account.username == username).exists()

	def count():
		return Account.select().count()

	def clear_current():
		for a in Account.select().where(Account.is_current):
			a.is_current = False
			a.save()

	def set_current(username):
		a = Account.get(Account.username == username)
		a.is_current = True
		a.save()

	def set_token(username, token):
		a = Account.get(Account.username == username)
		a.token = token
		a.save()

	def current_token():
		a = Account.get(Account.is_current)
		return a.token

	def current_username():
		a = Account.get(Account.is_current)
		return a.username



def create_tables():
	tables = [Account]
	db.create_tables(tables, True)