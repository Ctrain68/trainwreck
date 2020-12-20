from main import db
from sqlalchemy.orm import backref
from models.ProfileImages import ProfileImages
from models.Equipment import Equipment
from models.EquipmentOrder import EquipmentOrder

class Profile(db.Model):
    __tablename__ = 'profiles'

    profileid =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    account_active = db.Column(db.Boolean(), default = True)
    equipment = db.relationship("Equipment", backref="profile", lazy='dynamic')
    equipment_order = db.relationship("EquipmentOrder", backref="profile")
    admin = db.Column(db.Boolean(), default = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    profile_image = db.relationship("ProfileImages", backref="profile", uselist=False)
    equipment = db.relationship("Equipment", cascade="all, delete")
    
    
    def __repr__(self):
        return f"<Profile {self.username}>"    
