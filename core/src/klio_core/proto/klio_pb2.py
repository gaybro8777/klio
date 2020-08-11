# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: klio.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='klio.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\nklio.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xdf\x03\n\x0bKlioMessage\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.KlioMessage.Metadata\x12\x1f\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x11.KlioMessage.Data\x12\x19\n\x07version\x18\x03 \x01(\x0e\x32\x08.Version\x1a\x8d\x01\n\x08Metadata\x12\x1c\n\ndownstream\x18\x01 \x03(\x0b\x32\x08.KlioJob\x12\x19\n\x07visited\x18\x02 \x03(\x0b\x32\x08.KlioJob\x12+\n\rjob_audit_log\x18\x03 \x03(\x0b\x32\x14.KlioJobAuditLogItem\x12\r\n\x05\x66orce\x18\x04 \x01(\x08\x12\x0c\n\x04ping\x18\x05 \x01(\x08\x1a,\n\x06V1Data\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x1a*\n\x06V2Data\x12\x0f\n\x07\x65lement\x18\x01 \x01(\x0c\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x1a\x80\x01\n\x04\x44\x61ta\x12\x13\n\tentity_id\x18\x01 \x01(\tH\x00\x12!\n\x02v1\x18\x03 \x01(\x0b\x32\x13.KlioMessage.V1DataH\x00\x12!\n\x02v2\x18\x04 \x01(\x0b\x32\x13.KlioMessage.V2DataH\x00\x42\x0e\n\x0c\x64\x61ta_versionJ\x04\x08\x02\x10\x03R\x07payload\"\x9b\x01\n\x07KlioJob\x12\x10\n\x08job_name\x18\x01 \x01(\t\x12\x13\n\x0bgcp_project\x18\x02 \x01(\t\x12!\n\x06inputs\x18\x03 \x03(\x0b\x32\x11.KlioJob.JobInput\x1a\x46\n\x08JobInput\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x14\n\x0csubscription\x18\x02 \x01(\t\x12\x15\n\rdata_location\x18\x03 \x01(\t\"`\n\x13KlioJobAuditLogItem\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x08klio_job\x18\x02 \x01(\x0b\x32\x08.KlioJob*&\n\x07Version\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02V1\x10\x01\x12\x06\n\x02V2\x10\x02\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_VERSION = _descriptor.EnumDescriptor(
  name='Version',
  full_name='Version',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=785,
  serialized_end=823,
)
_sym_db.RegisterEnumDescriptor(_VERSION)

Version = enum_type_wrapper.EnumTypeWrapper(_VERSION)
UNKNOWN = 0
V1 = 1
V2 = 2



_KLIOMESSAGE_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='KlioMessage.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='downstream', full_name='KlioMessage.Metadata.downstream', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visited', full_name='KlioMessage.Metadata.visited', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_audit_log', full_name='KlioMessage.Metadata.job_audit_log', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='force', full_name='KlioMessage.Metadata.force', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ping', full_name='KlioMessage.Metadata.ping', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=165,
  serialized_end=306,
)

_KLIOMESSAGE_V1DATA = _descriptor.Descriptor(
  name='V1Data',
  full_name='KlioMessage.V1Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='KlioMessage.V1Data.entity_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='KlioMessage.V1Data.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=308,
  serialized_end=352,
)

_KLIOMESSAGE_V2DATA = _descriptor.Descriptor(
  name='V2Data',
  full_name='KlioMessage.V2Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='element', full_name='KlioMessage.V2Data.element', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='KlioMessage.V2Data.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=354,
  serialized_end=396,
)

_KLIOMESSAGE_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='KlioMessage.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='KlioMessage.Data.entity_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v1', full_name='KlioMessage.Data.v1', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v2', full_name='KlioMessage.Data.v2', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='data_version', full_name='KlioMessage.Data.data_version',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=399,
  serialized_end=527,
)

_KLIOMESSAGE = _descriptor.Descriptor(
  name='KlioMessage',
  full_name='KlioMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='KlioMessage.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='KlioMessage.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='KlioMessage.version', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_KLIOMESSAGE_METADATA, _KLIOMESSAGE_V1DATA, _KLIOMESSAGE_V2DATA, _KLIOMESSAGE_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=527,
)


_KLIOJOB_JOBINPUT = _descriptor.Descriptor(
  name='JobInput',
  full_name='KlioJob.JobInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='KlioJob.JobInput.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscription', full_name='KlioJob.JobInput.subscription', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_location', full_name='KlioJob.JobInput.data_location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=615,
  serialized_end=685,
)

_KLIOJOB = _descriptor.Descriptor(
  name='KlioJob',
  full_name='KlioJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_name', full_name='KlioJob.job_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gcp_project', full_name='KlioJob.gcp_project', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='KlioJob.inputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_KLIOJOB_JOBINPUT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=530,
  serialized_end=685,
)


_KLIOJOBAUDITLOGITEM = _descriptor.Descriptor(
  name='KlioJobAuditLogItem',
  full_name='KlioJobAuditLogItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='KlioJobAuditLogItem.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='klio_job', full_name='KlioJobAuditLogItem.klio_job', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=687,
  serialized_end=783,
)

_KLIOMESSAGE_METADATA.fields_by_name['downstream'].message_type = _KLIOJOB
_KLIOMESSAGE_METADATA.fields_by_name['visited'].message_type = _KLIOJOB
_KLIOMESSAGE_METADATA.fields_by_name['job_audit_log'].message_type = _KLIOJOBAUDITLOGITEM
_KLIOMESSAGE_METADATA.containing_type = _KLIOMESSAGE
_KLIOMESSAGE_V1DATA.containing_type = _KLIOMESSAGE
_KLIOMESSAGE_V2DATA.containing_type = _KLIOMESSAGE
_KLIOMESSAGE_DATA.fields_by_name['v1'].message_type = _KLIOMESSAGE_V1DATA
_KLIOMESSAGE_DATA.fields_by_name['v2'].message_type = _KLIOMESSAGE_V2DATA
_KLIOMESSAGE_DATA.containing_type = _KLIOMESSAGE
_KLIOMESSAGE_DATA.oneofs_by_name['data_version'].fields.append(
  _KLIOMESSAGE_DATA.fields_by_name['entity_id'])
_KLIOMESSAGE_DATA.fields_by_name['entity_id'].containing_oneof = _KLIOMESSAGE_DATA.oneofs_by_name['data_version']
_KLIOMESSAGE_DATA.oneofs_by_name['data_version'].fields.append(
  _KLIOMESSAGE_DATA.fields_by_name['v1'])
_KLIOMESSAGE_DATA.fields_by_name['v1'].containing_oneof = _KLIOMESSAGE_DATA.oneofs_by_name['data_version']
_KLIOMESSAGE_DATA.oneofs_by_name['data_version'].fields.append(
  _KLIOMESSAGE_DATA.fields_by_name['v2'])
_KLIOMESSAGE_DATA.fields_by_name['v2'].containing_oneof = _KLIOMESSAGE_DATA.oneofs_by_name['data_version']
_KLIOMESSAGE.fields_by_name['metadata'].message_type = _KLIOMESSAGE_METADATA
_KLIOMESSAGE.fields_by_name['data'].message_type = _KLIOMESSAGE_DATA
_KLIOMESSAGE.fields_by_name['version'].enum_type = _VERSION
_KLIOJOB_JOBINPUT.containing_type = _KLIOJOB
_KLIOJOB.fields_by_name['inputs'].message_type = _KLIOJOB_JOBINPUT
_KLIOJOBAUDITLOGITEM.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_KLIOJOBAUDITLOGITEM.fields_by_name['klio_job'].message_type = _KLIOJOB
DESCRIPTOR.message_types_by_name['KlioMessage'] = _KLIOMESSAGE
DESCRIPTOR.message_types_by_name['KlioJob'] = _KLIOJOB
DESCRIPTOR.message_types_by_name['KlioJobAuditLogItem'] = _KLIOJOBAUDITLOGITEM
DESCRIPTOR.enum_types_by_name['Version'] = _VERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KlioMessage = _reflection.GeneratedProtocolMessageType('KlioMessage', (_message.Message,), {

  'Metadata' : _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
    'DESCRIPTOR' : _KLIOMESSAGE_METADATA,
    '__module__' : 'klio_pb2'
    # @@protoc_insertion_point(class_scope:KlioMessage.Metadata)
    })
  ,

  'V1Data' : _reflection.GeneratedProtocolMessageType('V1Data', (_message.Message,), {
    'DESCRIPTOR' : _KLIOMESSAGE_V1DATA,
    '__module__' : 'klio_pb2'
    # @@protoc_insertion_point(class_scope:KlioMessage.V1Data)
    })
  ,

  'V2Data' : _reflection.GeneratedProtocolMessageType('V2Data', (_message.Message,), {
    'DESCRIPTOR' : _KLIOMESSAGE_V2DATA,
    '__module__' : 'klio_pb2'
    # @@protoc_insertion_point(class_scope:KlioMessage.V2Data)
    })
  ,

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _KLIOMESSAGE_DATA,
    '__module__' : 'klio_pb2'
    # @@protoc_insertion_point(class_scope:KlioMessage.Data)
    })
  ,
  'DESCRIPTOR' : _KLIOMESSAGE,
  '__module__' : 'klio_pb2'
  # @@protoc_insertion_point(class_scope:KlioMessage)
  })
_sym_db.RegisterMessage(KlioMessage)
_sym_db.RegisterMessage(KlioMessage.Metadata)
_sym_db.RegisterMessage(KlioMessage.V1Data)
_sym_db.RegisterMessage(KlioMessage.V2Data)
_sym_db.RegisterMessage(KlioMessage.Data)

KlioJob = _reflection.GeneratedProtocolMessageType('KlioJob', (_message.Message,), {

  'JobInput' : _reflection.GeneratedProtocolMessageType('JobInput', (_message.Message,), {
    'DESCRIPTOR' : _KLIOJOB_JOBINPUT,
    '__module__' : 'klio_pb2'
    # @@protoc_insertion_point(class_scope:KlioJob.JobInput)
    })
  ,
  'DESCRIPTOR' : _KLIOJOB,
  '__module__' : 'klio_pb2'
  # @@protoc_insertion_point(class_scope:KlioJob)
  })
_sym_db.RegisterMessage(KlioJob)
_sym_db.RegisterMessage(KlioJob.JobInput)

KlioJobAuditLogItem = _reflection.GeneratedProtocolMessageType('KlioJobAuditLogItem', (_message.Message,), {
  'DESCRIPTOR' : _KLIOJOBAUDITLOGITEM,
  '__module__' : 'klio_pb2'
  # @@protoc_insertion_point(class_scope:KlioJobAuditLogItem)
  })
_sym_db.RegisterMessage(KlioJobAuditLogItem)


# @@protoc_insertion_point(module_scope)
