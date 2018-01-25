from app import ma

# Schema for DB (structure of endpoints responses)
class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('firstname', 'lastname','birthday')
