# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor, descriptor_pool as _descriptor_pool, \
    symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0emessages.proto\x12\x08messages\"\xa4\x01\n\x08Response\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.messages.ResponseStatus\x12\x34\n\x0eserviceMessage\x18\x02 \x01(\x0b\x32\x1c.messages.FromServiceMessage\x12\x38\n\x10\x63onnectorMessage\x18\x03 \x01(\x0b\x32\x1e.messages.FromConnectorMessage\"\xa3\x05\n\x14\x46romConnectorMessage\x12$\n\x08response\x18\x01 \x01(\x0b\x32\x12.messages.Response\x12:\n\x13gatewayTelemetryMsg\x18\x02 \x01(\x0b\x32\x1d.messages.GatewayTelemetryMsg\x12<\n\x14gatewayAttributesMsg\x18\x03 \x01(\x0b\x32\x1e.messages.GatewayAttributesMsg\x12\x32\n\x0fgatewayClaimMsg\x18\x04 \x01(\x0b\x32\x19.messages.GatewayClaimMsg\x12<\n\x14registerConnectorMsg\x18\x05 \x01(\x0b\x32\x1e.messages.RegisterConnectorMsg\x12@\n\x16unregisterConnectorMsg\x18\x06 \x01(\x0b\x32 .messages.UnregisterConnectorMsg\x12(\n\nconnectMsg\x18\x07 \x01(\x0b\x32\x14.messages.ConnectMsg\x12.\n\rdisconnectMsg\x18\x08 \x01(\x0b\x32\x17.messages.DisconnectMsg\x12>\n\x15gatewayRpcResponseMsg\x18\t \x01(\x0b\x32\x1f.messages.GatewayRpcResponseMsg\x12I\n\x1agatewayAttributeRequestMsg\x18\n \x01(\x0b\x32%.messages.GatewayAttributesRequestMsg\x12R\n\x1f\x63onnectorGetConnectedDevicesMsg\x18\x0b \x01(\x0b\x32).messages.ConnectorGetConnectedDevicesMsg\"\x9e\x04\n\x12\x46romServiceMessage\x12$\n\x08response\x18\x01 \x01(\x0b\x32\x12.messages.Response\x12\x46\n\x19\x63onnectorConfigurationMsg\x18\x02 \x01(\x0b\x32#.messages.ConnectorConfigurationMsg\x12^\n%gatewayAttributeUpdateNotificationMsg\x18\x03 \x01(\x0b\x32/.messages.GatewayAttributeUpdateNotificationMsg\x12J\n\x1bgatewayAttributeResponseMsg\x18\x04 \x01(\x0b\x32%.messages.GatewayAttributeResponseMsg\x12H\n\x1agatewayDeviceRpcRequestMsg\x18\x05 \x01(\x0b\x32$.messages.GatewayDeviceRpcRequestMsg\x12@\n\x16unregisterConnectorMsg\x18\x06 \x01(\x0b\x32 .messages.UnregisterConnectorMsg\x12\x62\n\'connectorGetConnectedDevicesResponseMsg\x18\x07 \x01(\x0b\x32\x31.messages.ConnectorGetConnectedDevicesResponseMsg\",\n\x14RegisterConnectorMsg\x12\x14\n\x0c\x63onnectorKey\x18\x01 \x01(\t\".\n\x16UnregisterConnectorMsg\x12\x14\n\x0c\x63onnectorKey\x18\x01 \x01(\t\"^\n\x19\x43onnectorConfigurationMsg\x12\x15\n\rconnectorName\x18\x01 \x01(\t\x12\x15\n\rconfiguration\x18\x02 \x01(\t\x12\x13\n\x0b\x63onnectorId\x18\x03 \x01(\t\"7\n\x1f\x43onnectorGetConnectedDevicesMsg\x12\x14\n\x0c\x63onnectorKey\x18\x01 \x01(\t\"b\n\'ConnectorGetConnectedDevicesResponseMsg\x12\x37\n\x10\x63onnectorDevices\x18\x01 \x03(\x0b\x32\x1d.messages.ConnectorDeviceInfo\"=\n\x13\x43onnectorDeviceInfo\x12\x12\n\ndeviceName\x18\x01 \x01(\t\x12\x12\n\ndeviceType\x18\x02 \x01(\t\"\x96\x01\n\rKeyValueProto\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x04type\x18\x02 \x01(\x0e\x32\x16.messages.KeyValueType\x12\x0e\n\x06\x62ool_v\x18\x03 \x01(\x08\x12\x0e\n\x06long_v\x18\x04 \x01(\x03\x12\x10\n\x08\x64ouble_v\x18\x05 \x01(\x01\x12\x10\n\x08string_v\x18\x06 \x01(\t\x12\x0e\n\x06json_v\x18\x07 \x01(\t\"<\n\tTsKvProto\x12\n\n\x02ts\x18\x01 \x01(\x03\x12#\n\x02kv\x18\x02 \x01(\x0b\x32\x17.messages.KeyValueProto\"@\n\rTsKvListProto\x12\n\n\x02ts\x18\x01 \x01(\x03\x12#\n\x02kv\x18\x02 \x03(\x0b\x32\x17.messages.KeyValueProto\"=\n\x10PostTelemetryMsg\x12)\n\x08tsKvList\x18\x01 \x03(\x0b\x32\x17.messages.TsKvListProto\"7\n\x10PostAttributeMsg\x12#\n\x02kv\x18\x01 \x03(\x0b\x32\x17.messages.KeyValueProto\"c\n\x1e\x41ttributeUpdateNotificationMsg\x12*\n\rsharedUpdated\x18\x01 \x03(\x0b\x32\x13.messages.TsKvProto\x12\x15\n\rsharedDeleted\x18\x02 \x03(\t\"N\n\x15ToDeviceRpcRequestMsg\x12\x11\n\trequestId\x18\x01 \x01(\x05\x12\x12\n\nmethodName\x18\x02 \x01(\t\x12\x0e\n\x06params\x18\x03 \x01(\t\"K\n\x16ToDeviceRpcResponseMsg\x12\x11\n\trequestId\x18\x01 \x01(\x05\x12\x0f\n\x07payload\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"N\n\x15ToServerRpcRequestMsg\x12\x11\n\trequestId\x18\x01 \x01(\x05\x12\x12\n\nmethodName\x18\x02 \x01(\t\x12\x0e\n\x06params\x18\x03 \x01(\t\"K\n\x16ToServerRpcResponseMsg\x12\x11\n\trequestId\x18\x01 \x01(\x05\x12\x0f\n\x07payload\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"4\n\x0b\x43laimDevice\x12\x11\n\tsecretKey\x18\x01 \x01(\t\x12\x12\n\ndurationMs\x18\x02 \x01(\x03\";\n\x11\x41ttributesRequest\x12\x12\n\nclientKeys\x18\x01 \x01(\t\x12\x12\n\nsharedKeys\x18\x02 \x01(\t\",\n\nRpcRequest\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0e\n\x06params\x18\x02 \x01(\t\"#\n\rDisconnectMsg\x12\x12\n\ndeviceName\x18\x01 \x01(\t\"4\n\nConnectMsg\x12\x12\n\ndeviceName\x18\x01 \x01(\t\x12\x12\n\ndeviceType\x18\x02 \x01(\t\"K\n\x0cTelemetryMsg\x12\x12\n\ndeviceName\x18\x01 \x01(\t\x12\'\n\x03msg\x18\x03 \x01(\x0b\x32\x1a.messages.PostTelemetryMsg\"L\n\rAttributesMsg\x12\x12\n\ndeviceName\x18\x01 \x01(\t\x12\'\n\x03msg\x18\x02 \x01(\x0b\x32\x1a.messages.PostAttributeMsg\"Q\n\x0e\x43laimDeviceMsg\x12\x12\n\ndeviceName\x18\x01 \x01(\t\x12+\n\x0c\x63laimRequest\x18\x02 \x01(\x0b\x32\x15.messages.ClaimDevice\":\n\x13GatewayTelemetryMsg\x12#\n\x03msg\x18\x01 \x03(\x0b\x32\x16.messages.TelemetryMsg\"8\n\x0fGatewayClaimMsg\x12%\n\x03msg\x18\x01 \x03(\x0b\x32\x18.messages.ClaimDeviceMsg\"<\n\x14GatewayAttributesMsg\x12$\n\x03msg\x18\x01 \x03(\x0b\x32\x17.messages.AttributesMsg\"E\n\x15GatewayRpcResponseMsg\x12\x12\n\ndeviceName\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\"n\n\x1bGatewayAttributeResponseMsg\x12\x12\n\ndeviceName\x18\x01 \x01(\t\x12;\n\x0bresponseMsg\x18\x02 \x01(\x0b\x32&.messages.GatewayAttributesResponseMsg\"~\n%GatewayAttributeUpdateNotificationMsg\x12\x12\n\ndeviceName\x18\x01 \x01(\t\x12\x41\n\x0fnotificationMsg\x18\x02 \x01(\x0b\x32(.messages.AttributeUpdateNotificationMsg\"h\n\x1aGatewayDeviceRpcRequestMsg\x12\x12\n\ndeviceName\x18\x01 \x01(\t\x12\x36\n\rrpcRequestMsg\x18\x02 \x01(\x0b\x32\x1f.messages.ToDeviceRpcRequestMsg\"[\n\x1bGatewayAttributesRequestMsg\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ndeviceName\x18\x02 \x01(\t\x12\x0e\n\x06\x63lient\x18\x03 \x01(\x08\x12\x0c\n\x04keys\x18\x04 \x03(\t\"\xac\x01\n\x1cGatewayAttributesResponseMsg\x12\x11\n\trequestId\x18\x01 \x01(\x05\x12\x34\n\x13\x63lientAttributeList\x18\x02 \x03(\x0b\x32\x17.messages.KeyValueProto\x12\x34\n\x13sharedAttributeList\x18\x03 \x03(\x0b\x32\x17.messages.KeyValueProto\x12\r\n\x05\x65rror\x18\x05 \x01(\t*F\n\x0eResponseStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\r\n\tNOT_FOUND\x10\x02\x12\x0b\n\x07\x46\x41ILURE\x10\x03*Q\n\x0cKeyValueType\x12\r\n\tBOOLEAN_V\x10\x00\x12\n\n\x06LONG_V\x10\x01\x12\x0c\n\x08\x44OUBLE_V\x10\x02\x12\x0c\n\x08STRING_V\x10\x03\x12\n\n\x06JSON_V\x10\x04\x32_\n\x15TBGatewayProtoService\x12\x46\n\x06stream\x12\x1e.messages.FromConnectorMessage\x1a\x1c.messages.FromServiceMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_RESPONSESTATUS']._serialized_start = 3999
    _globals['_RESPONSESTATUS']._serialized_end = 4069
    _globals['_KEYVALUETYPE']._serialized_start = 4071
    _globals['_KEYVALUETYPE']._serialized_end = 4152
    _globals['_RESPONSE']._serialized_start = 29
    _globals['_RESPONSE']._serialized_end = 193
    _globals['_FROMCONNECTORMESSAGE']._serialized_start = 196
    _globals['_FROMCONNECTORMESSAGE']._serialized_end = 871
    _globals['_FROMSERVICEMESSAGE']._serialized_start = 874
    _globals['_FROMSERVICEMESSAGE']._serialized_end = 1416
    _globals['_REGISTERCONNECTORMSG']._serialized_start = 1418
    _globals['_REGISTERCONNECTORMSG']._serialized_end = 1462
    _globals['_UNREGISTERCONNECTORMSG']._serialized_start = 1464
    _globals['_UNREGISTERCONNECTORMSG']._serialized_end = 1510
    _globals['_CONNECTORCONFIGURATIONMSG']._serialized_start = 1512
    _globals['_CONNECTORCONFIGURATIONMSG']._serialized_end = 1606
    _globals['_CONNECTORGETCONNECTEDDEVICESMSG']._serialized_start = 1608
    _globals['_CONNECTORGETCONNECTEDDEVICESMSG']._serialized_end = 1663
    _globals['_CONNECTORGETCONNECTEDDEVICESRESPONSEMSG']._serialized_start = 1665
    _globals['_CONNECTORGETCONNECTEDDEVICESRESPONSEMSG']._serialized_end = 1763
    _globals['_CONNECTORDEVICEINFO']._serialized_start = 1765
    _globals['_CONNECTORDEVICEINFO']._serialized_end = 1826
    _globals['_KEYVALUEPROTO']._serialized_start = 1829
    _globals['_KEYVALUEPROTO']._serialized_end = 1979
    _globals['_TSKVPROTO']._serialized_start = 1981
    _globals['_TSKVPROTO']._serialized_end = 2041
    _globals['_TSKVLISTPROTO']._serialized_start = 2043
    _globals['_TSKVLISTPROTO']._serialized_end = 2107
    _globals['_POSTTELEMETRYMSG']._serialized_start = 2109
    _globals['_POSTTELEMETRYMSG']._serialized_end = 2170
    _globals['_POSTATTRIBUTEMSG']._serialized_start = 2172
    _globals['_POSTATTRIBUTEMSG']._serialized_end = 2227
    _globals['_ATTRIBUTEUPDATENOTIFICATIONMSG']._serialized_start = 2229
    _globals['_ATTRIBUTEUPDATENOTIFICATIONMSG']._serialized_end = 2328
    _globals['_TODEVICERPCREQUESTMSG']._serialized_start = 2330
    _globals['_TODEVICERPCREQUESTMSG']._serialized_end = 2408
    _globals['_TODEVICERPCRESPONSEMSG']._serialized_start = 2410
    _globals['_TODEVICERPCRESPONSEMSG']._serialized_end = 2485
    _globals['_TOSERVERRPCREQUESTMSG']._serialized_start = 2487
    _globals['_TOSERVERRPCREQUESTMSG']._serialized_end = 2565
    _globals['_TOSERVERRPCRESPONSEMSG']._serialized_start = 2567
    _globals['_TOSERVERRPCRESPONSEMSG']._serialized_end = 2642
    _globals['_CLAIMDEVICE']._serialized_start = 2644
    _globals['_CLAIMDEVICE']._serialized_end = 2696
    _globals['_ATTRIBUTESREQUEST']._serialized_start = 2698
    _globals['_ATTRIBUTESREQUEST']._serialized_end = 2757
    _globals['_RPCREQUEST']._serialized_start = 2759
    _globals['_RPCREQUEST']._serialized_end = 2803
    _globals['_DISCONNECTMSG']._serialized_start = 2805
    _globals['_DISCONNECTMSG']._serialized_end = 2840
    _globals['_CONNECTMSG']._serialized_start = 2842
    _globals['_CONNECTMSG']._serialized_end = 2894
    _globals['_TELEMETRYMSG']._serialized_start = 2896
    _globals['_TELEMETRYMSG']._serialized_end = 2971
    _globals['_ATTRIBUTESMSG']._serialized_start = 2973
    _globals['_ATTRIBUTESMSG']._serialized_end = 3049
    _globals['_CLAIMDEVICEMSG']._serialized_start = 3051
    _globals['_CLAIMDEVICEMSG']._serialized_end = 3132
    _globals['_GATEWAYTELEMETRYMSG']._serialized_start = 3134
    _globals['_GATEWAYTELEMETRYMSG']._serialized_end = 3192
    _globals['_GATEWAYCLAIMMSG']._serialized_start = 3194
    _globals['_GATEWAYCLAIMMSG']._serialized_end = 3250
    _globals['_GATEWAYATTRIBUTESMSG']._serialized_start = 3252
    _globals['_GATEWAYATTRIBUTESMSG']._serialized_end = 3312
    _globals['_GATEWAYRPCRESPONSEMSG']._serialized_start = 3314
    _globals['_GATEWAYRPCRESPONSEMSG']._serialized_end = 3383
    _globals['_GATEWAYATTRIBUTERESPONSEMSG']._serialized_start = 3385
    _globals['_GATEWAYATTRIBUTERESPONSEMSG']._serialized_end = 3495
    _globals['_GATEWAYATTRIBUTEUPDATENOTIFICATIONMSG']._serialized_start = 3497
    _globals['_GATEWAYATTRIBUTEUPDATENOTIFICATIONMSG']._serialized_end = 3623
    _globals['_GATEWAYDEVICERPCREQUESTMSG']._serialized_start = 3625
    _globals['_GATEWAYDEVICERPCREQUESTMSG']._serialized_end = 3729
    _globals['_GATEWAYATTRIBUTESREQUESTMSG']._serialized_start = 3731
    _globals['_GATEWAYATTRIBUTESREQUESTMSG']._serialized_end = 3822
    _globals['_GATEWAYATTRIBUTESRESPONSEMSG']._serialized_start = 3825
    _globals['_GATEWAYATTRIBUTESRESPONSEMSG']._serialized_end = 3997
    _globals['_TBGATEWAYPROTOSERVICE']._serialized_start = 4154
    _globals['_TBGATEWAYPROTOSERVICE']._serialized_end = 4249
# @@protoc_insertion_point(module_scope)