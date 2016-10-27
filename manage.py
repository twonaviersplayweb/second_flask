from flask.ext.script import Manager, Shell
from app import create_app
from flask.ext.migrate import Migrate, MigrateCommand
from app import db
from app.models import User, Role, Post

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post)
manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
