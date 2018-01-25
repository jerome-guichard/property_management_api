from app import ma
from app.models.user import User

# Schema for DB (structure of endpoints responses)
class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        model = User
        fields = ('firstname', 'lastname','birthday','email')    