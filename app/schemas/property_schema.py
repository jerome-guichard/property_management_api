from app import ma
# Property Schema
class PropertySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name', 'description','city','room','userid')