import sys
sys.path.insert(0, "..")
import logging
from loguru import logger

from opcua import Client


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    client = Client("opc.tcp://HUSZP5DN7FA09:4840")

    client.set_user("svc_opc_read")
    client.set_password("jVVxjaRnqP2#@#01%AK3")

    client.set_security_string("Basic256Sha256,SignAndEncrypt,.src/certificate/app_cert.der,.src/certificate/app_private_key.pem")
    client.application_uri = "urn:example.org:FreeOpcUa:python-opcua"

    client.secure_channel_timeout = 10000
    client.session_timeout = 10000
    try:
        client.connect()
        logger.success("Connection to the server is established.")

        root = client.get_root_node()
        logger.success("The root node retrieval operation is successful")

        objects = client.get_objects_node()
        logger.success("The objects node retrieval operation is successful")
        logger.info("The child nodes of the objects node are: {}", objects.get_children())
    except Exception as e:
        logger.critical("Exception occured: {}", e)
    finally:
        client.disconnect()
        logger.success("Disconnected.")