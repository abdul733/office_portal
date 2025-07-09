from app import create_app
from app.database import db
from sqlalchemy import text


app = create_app()

with app.app_context():
    result = db.session.execute(text('SELECT * FROM employee')).fetchall()
    for row in result:
        print(row)
