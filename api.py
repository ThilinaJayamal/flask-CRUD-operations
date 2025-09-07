from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api,reqparse,fields,marshal_with,abort

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
api = Api(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary key is required
    name = db.Column(db.String(100), nullable=False)  # name should be string
    email = db.Column(db.String(120), unique=True, nullable=False)  # email unique

    def __repr__(self):
        return f"<User id={self.id} name={self.name} email={self.email}>"

user_args = reqparse.RequestParser()
user_args.add_argument('name',type=str, required=True, help='Name cannot be blank')
user_args.add_argument('email',type=str, required=True, help='Email cannot be blank')

userFields = {
    'id':fields.Integer,
    'name':fields.String,
    'email':fields.String
}

class Users(Resource):

    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users, 200
    
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args["name"],email=args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201
    
class User(Resource):

    @marshal_with(userFields)
    def get(self,id):
        user = UserModel.query.filter_by(id=id).first()
        if(not user):
            abort(404, message="User not found")   
        return user, 200
    
    @marshal_with(userFields)
    def patch(self,id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if(not user):
            abort(404, message="User not found")
        user.email = args["email"]
        user.name = args["name"]
        db.session.commit()   
        return user, 200
    
    @marshal_with(userFields)
    def delete(self,id):
        user = UserModel.query.filter_by(id=id).first()
        if(not user):
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()   
        
        users = UserModel.query.all()
        return users
    
    
api.add_resource(Users,'/api/users/')
api.add_resource(User,"/api/users/<int:id>")

@app.route("/")
def home():
    return "<h1>Hello, Flask!</h1>"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
