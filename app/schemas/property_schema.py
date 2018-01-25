from app import ma
from app.models.property import Property

# Property Schema
class PropertySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ( 'name', 'description', 'city', 'room', 'owner_id')
