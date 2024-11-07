from flask import Flask


from flask import Flask
from prisma import Prisma, register

db = Prisma()
db.connect()
register(db)
app = Flask(__name__)



if __name__ == "__main__":
  app.run(debug=True, port=5000, host='0.0.0.0')