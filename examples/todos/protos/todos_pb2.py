# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/todos.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12protos/todos.proto\x12\x05todos\x1a\x1cgoogle/protobuf/struct.proto\"\x18\n\nGetRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"h\n\x0bListRequest\x12(\n\x07\x66ilters\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\x12\x10\n\x08ordering\x18\x04 \x03(\t\"6\n\rCreateRequest\x12%\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"B\n\rUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12%\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x1b\n\rDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"5\n\x0cItemResponse\x12%\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"D\n\x0cListResponse\x12%\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\" \n\x0eResultResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x32\xa7\x02\n\x05Todos\x12\x36\n\tListTodos\x12\x12.todos.ListRequest\x1a\x13.todos.ListResponse\"\x00\x12\x39\n\nCreateTodo\x12\x14.todos.CreateRequest\x1a\x13.todos.ItemResponse\"\x00\x12\x33\n\x07GetTodo\x12\x11.todos.GetRequest\x1a\x13.todos.ItemResponse\"\x00\x12\x39\n\nUpdateTodo\x12\x14.todos.UpdateRequest\x1a\x13.todos.ItemResponse\"\x00\x12;\n\nDeleteTodo\x12\x14.todos.DeleteRequest\x1a\x15.todos.ResultResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.todos_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETREQUEST._serialized_start=59
  _GETREQUEST._serialized_end=83
  _LISTREQUEST._serialized_start=85
  _LISTREQUEST._serialized_end=189
  _CREATEREQUEST._serialized_start=191
  _CREATEREQUEST._serialized_end=245
  _UPDATEREQUEST._serialized_start=247
  _UPDATEREQUEST._serialized_end=313
  _DELETEREQUEST._serialized_start=315
  _DELETEREQUEST._serialized_end=342
  _ITEMRESPONSE._serialized_start=344
  _ITEMRESPONSE._serialized_end=397
  _LISTRESPONSE._serialized_start=399
  _LISTRESPONSE._serialized_end=467
  _RESULTRESPONSE._serialized_start=469
  _RESULTRESPONSE._serialized_end=501
  _TODOS._serialized_start=504
  _TODOS._serialized_end=799
# @@protoc_insertion_point(module_scope)
