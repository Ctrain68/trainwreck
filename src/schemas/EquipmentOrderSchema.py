from main import ma
from models.EquipmentOrder import EquipmentOrder
from marshmallow.validate import Length

class EquipmentOrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EquipmentOrder
    order_return_date_estimate = ma.DateTime(required = False)
    order_actual_return_date = ma.DateTime(required = False)
    order_active = ma.Boolean(required=True, default=True)



equipment_order_schema = EquipmentOrderSchema()
equipment_orders_schema = EquipmentOrderSchema(many=True)