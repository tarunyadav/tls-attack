from enum import *

from tls_attack.structure.TLSStructure import TLSStructure
from tls_attack.structure.TLSAnnotation import *
from tls_attack.structure.TLSHeader import TLSVersion

class TLSServerHello(TLSStructure):
    version            = TLSField(size = 2,  type = "enum", type_enum = TLSVersion)
    gmt_unix_timestamp = TLSField(size = 4,  type = "int")
    random_bytes       = TLSField(size = 28, type = "bytes")
    session_id_length  = TLSField(size = 1,  type = "int", default = TLSAuto())
    session_id         = TLSField(
                                size = TLSFieldRef(name = "session_id_length"), 
                                type = "bytes"
                            )
    
    cipher_suite        = TLSField(size = 2, type = "TLSCipherSuiteStruct")
    compression_methods = TLSField(size = 1, type = "TLSCompressionStruct")

    extensions_length = TLSField(size = 2,  type = "int", optional = True, default = TLSAuto())
    extensions        = TLSField(
                                size = TLSFieldRef(name = "extensions_length"),
                                type = "TLSExtension",
                                type_list = True,
                                optional = True
                            )