# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orders.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='orders.proto',
  package='orders',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0corders.proto\x12\x06orders\"V\n\x13OrderDetailResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nproduct_id\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\t\x12\x10\n\x08quantity\x18\x04 \x01(\x05\"O\n\rOrderResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x32\n\rorder_details\x18\x02 \x03(\x0b\x32\x1b.orders.OrderDetailResponse\"\x1d\n\x0fGetOrderRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"O\n\x18\x43reateOrderDetailRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\"M\n\x12\x43reateOrderRequest\x12\x37\n\rorder_details\x18\x01 \x03(\x0b\x32 .orders.CreateOrderDetailRequest\"[\n\x18UpdateOrderDetailRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nproduct_id\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\t\x12\x10\n\x08quantity\x18\x04 \x01(\x05\"Y\n\x12UpdateOrderRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x37\n\rorder_details\x18\x02 \x03(\x0b\x32 .orders.UpdateOrderDetailRequest\" \n\x12\x44\x65leteOrderRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x16\n\x14OrderDeletedResponse2\x95\x02\n\x06orders\x12;\n\tget_order\x12\x17.orders.GetOrderRequest\x1a\x15.orders.OrderResponse\x12\x41\n\x0c\x63reate_order\x12\x1a.orders.CreateOrderRequest\x1a\x15.orders.OrderResponse\x12\x41\n\x0cupdate_order\x12\x1a.orders.UpdateOrderRequest\x1a\x15.orders.OrderResponse\x12H\n\x0c\x64\x65lete_order\x12\x1a.orders.DeleteOrderRequest\x1a\x1c.orders.OrderDeletedResponseb\x06proto3')
)




_ORDERDETAILRESPONSE = _descriptor.Descriptor(
  name='OrderDetailResponse',
  full_name='orders.OrderDetailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.OrderDetailResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product_id', full_name='orders.OrderDetailResponse.product_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='orders.OrderDetailResponse.price', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='orders.OrderDetailResponse.quantity', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=110,
)


_ORDERRESPONSE = _descriptor.Descriptor(
  name='OrderResponse',
  full_name='orders.OrderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.OrderResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_details', full_name='orders.OrderResponse.order_details', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=191,
)


_GETORDERREQUEST = _descriptor.Descriptor(
  name='GetOrderRequest',
  full_name='orders.GetOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.GetOrderRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=222,
)


_CREATEORDERDETAILREQUEST = _descriptor.Descriptor(
  name='CreateOrderDetailRequest',
  full_name='orders.CreateOrderDetailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='orders.CreateOrderDetailRequest.product_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='orders.CreateOrderDetailRequest.price', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='orders.CreateOrderDetailRequest.quantity', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=303,
)


_CREATEORDERREQUEST = _descriptor.Descriptor(
  name='CreateOrderRequest',
  full_name='orders.CreateOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_details', full_name='orders.CreateOrderRequest.order_details', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=382,
)


_UPDATEORDERDETAILREQUEST = _descriptor.Descriptor(
  name='UpdateOrderDetailRequest',
  full_name='orders.UpdateOrderDetailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.UpdateOrderDetailRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product_id', full_name='orders.UpdateOrderDetailRequest.product_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='orders.UpdateOrderDetailRequest.price', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='orders.UpdateOrderDetailRequest.quantity', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=384,
  serialized_end=475,
)


_UPDATEORDERREQUEST = _descriptor.Descriptor(
  name='UpdateOrderRequest',
  full_name='orders.UpdateOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.UpdateOrderRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_details', full_name='orders.UpdateOrderRequest.order_details', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=477,
  serialized_end=566,
)


_DELETEORDERREQUEST = _descriptor.Descriptor(
  name='DeleteOrderRequest',
  full_name='orders.DeleteOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.DeleteOrderRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=568,
  serialized_end=600,
)


_ORDERDELETEDRESPONSE = _descriptor.Descriptor(
  name='OrderDeletedResponse',
  full_name='orders.OrderDeletedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=602,
  serialized_end=624,
)

_ORDERRESPONSE.fields_by_name['order_details'].message_type = _ORDERDETAILRESPONSE
_CREATEORDERREQUEST.fields_by_name['order_details'].message_type = _CREATEORDERDETAILREQUEST
_UPDATEORDERREQUEST.fields_by_name['order_details'].message_type = _UPDATEORDERDETAILREQUEST
DESCRIPTOR.message_types_by_name['OrderDetailResponse'] = _ORDERDETAILRESPONSE
DESCRIPTOR.message_types_by_name['OrderResponse'] = _ORDERRESPONSE
DESCRIPTOR.message_types_by_name['GetOrderRequest'] = _GETORDERREQUEST
DESCRIPTOR.message_types_by_name['CreateOrderDetailRequest'] = _CREATEORDERDETAILREQUEST
DESCRIPTOR.message_types_by_name['CreateOrderRequest'] = _CREATEORDERREQUEST
DESCRIPTOR.message_types_by_name['UpdateOrderDetailRequest'] = _UPDATEORDERDETAILREQUEST
DESCRIPTOR.message_types_by_name['UpdateOrderRequest'] = _UPDATEORDERREQUEST
DESCRIPTOR.message_types_by_name['DeleteOrderRequest'] = _DELETEORDERREQUEST
DESCRIPTOR.message_types_by_name['OrderDeletedResponse'] = _ORDERDELETEDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderDetailResponse = _reflection.GeneratedProtocolMessageType('OrderDetailResponse', (_message.Message,), dict(
  DESCRIPTOR = _ORDERDETAILRESPONSE,
  __module__ = 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.OrderDetailResponse)
  ))
_sym_db.RegisterMessage(OrderDetailResponse)

OrderResponse = _reflection.GeneratedProtocolMessageType('OrderResponse', (_message.Message,), dict(
  DESCRIPTOR = _ORDERRESPONSE,
  __module__ = 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.OrderResponse)
  ))
_sym_db.RegisterMessage(OrderResponse)

GetOrderRequest = _reflection.GeneratedProtocolMessageType('GetOrderRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETORDERREQUEST,
  __module__ = 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.GetOrderRequest)
  ))
_sym_db.RegisterMessage(GetOrderRequest)

CreateOrderDetailRequest = _reflection.GeneratedProtocolMessageType('CreateOrderDetailRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEORDERDETAILREQUEST,
  __module__ = 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.CreateOrderDetailRequest)
  ))
_sym_db.RegisterMessage(CreateOrderDetailRequest)

CreateOrderRequest = _reflection.GeneratedProtocolMessageType('CreateOrderRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEORDERREQUEST,
  __module__ = 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.CreateOrderRequest)
  ))
_sym_db.RegisterMessage(CreateOrderRequest)

UpdateOrderDetailRequest = _reflection.GeneratedProtocolMessageType('UpdateOrderDetailRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEORDERDETAILREQUEST,
  __module__ = 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.UpdateOrderDetailRequest)
  ))
_sym_db.RegisterMessage(UpdateOrderDetailRequest)

UpdateOrderRequest = _reflection.GeneratedProtocolMessageType('UpdateOrderRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEORDERREQUEST,
  __module__ = 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.UpdateOrderRequest)
  ))
_sym_db.RegisterMessage(UpdateOrderRequest)

DeleteOrderRequest = _reflection.GeneratedProtocolMessageType('DeleteOrderRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEORDERREQUEST,
  __module__ = 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.DeleteOrderRequest)
  ))
_sym_db.RegisterMessage(DeleteOrderRequest)

OrderDeletedResponse = _reflection.GeneratedProtocolMessageType('OrderDeletedResponse', (_message.Message,), dict(
  DESCRIPTOR = _ORDERDELETEDRESPONSE,
  __module__ = 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.OrderDeletedResponse)
  ))
_sym_db.RegisterMessage(OrderDeletedResponse)



_ORDERS = _descriptor.ServiceDescriptor(
  name='orders',
  full_name='orders.orders',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=627,
  serialized_end=904,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_order',
    full_name='orders.orders.get_order',
    index=0,
    containing_service=None,
    input_type=_GETORDERREQUEST,
    output_type=_ORDERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='create_order',
    full_name='orders.orders.create_order',
    index=1,
    containing_service=None,
    input_type=_CREATEORDERREQUEST,
    output_type=_ORDERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='update_order',
    full_name='orders.orders.update_order',
    index=2,
    containing_service=None,
    input_type=_UPDATEORDERREQUEST,
    output_type=_ORDERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='delete_order',
    full_name='orders.orders.delete_order',
    index=3,
    containing_service=None,
    input_type=_DELETEORDERREQUEST,
    output_type=_ORDERDELETEDRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORDERS)

DESCRIPTOR.services_by_name['orders'] = _ORDERS

# @@protoc_insertion_point(module_scope)