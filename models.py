import db as db


class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    # relationship in one
    pets = db.relationship('Pet', backref='owner')  # pet.owner
    # pets = db.relationship('Pet', backref='owner', lazy='subquery')

    def __repr__(self):
        return f'<Pet Owner {self.name}>'


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    # foreign key in many
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    def __repr__(self):
        return f'<Pet {self.name}, {self.species}>'

# # work without setting lazy
# from app import app
# from models import db, Pet, Owner
# with app.app_context():
#     pets = Pet.query.filter_by(owner_id=1).first()
#     owner = Owner.query.filter_by(id=1).first()
#     pets_list = owner.pets
# pets_list

# with app.app_context():
#     owners = Owner.query.all()
#     owner = owners[0]
#     pets = owner.pets
# pets
#  ==============================================================
# # set lay="subquery" make owner.pets work
# # otherwise raise orm_exc.DetachedInstanceError
# from app import app
# from models import db, Owner
# with app.app_context():
#     owners = Owner.query.all()
#     owner = owners[0]
# owner.pets
