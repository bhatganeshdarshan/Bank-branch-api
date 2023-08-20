from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
db = SQLAlchemy()
db.init_app(app)

class Branch(db.Model):
    __tablename__='branches'
    ifsc = db.Column(db.String(11), primary_key=True)
    bank_id = db.Column(db.BigInteger)
    branch = db.Column(db.String(74))
    address = db.Column(db.String(195))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    state = db.Column(db.String(26))
    bank_name=db.Column(db.String(50))

    def to_dict(self):
        dictionary={}
        for column in self.__table__.columns:
            dictionary[column.name]=getattr(self, column.name)
        return dictionary


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/all')
def get_all():
    result=db.session.execute(db.select(Branch).order_by(Branch.ifsc))
    all_branches=result.scalars().all()
    return jsonify(banks=[bank.to_dict() for bank in all_branches])

@app.route('/search')
def search_branch():
    query_loc=request.args.get("loc")
    result=db.session.execute(db.select(Branch).where(Branch.branch==query_loc.upper()))
    all_banks=result.scalars().all()
    if all_banks:
        return jsonify(banks=[bank.to_dict() for bank in all_banks])
    return jsonify(error={"error":"did not find any banks at that location !!"}),404

if __name__=="__main__":
    app.run(debug=True)