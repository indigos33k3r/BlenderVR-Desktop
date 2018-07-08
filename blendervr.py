from util.Logger import Logger
import openvr
import socket


server = None
client = None


def check_system_ready():
    establish_server_connection()
    return openvr.isRuntimeInstalled() and openvr.isHmdPresent()


def establish_server_connection():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8181))

    Logger.i("Awaiting connection. Please click 'Start VR' in Blender")
    server.listen(2)

    global client
    (client, address) = server.accept()

    Logger.d("Esablished connection from: ", address)
    Logger.i("Connection to BlenderVR-addon established")


def run_system_startup():
    Logger.i("Starting VR")
    # openvr.init(openvr.VRApplication_Scene)


def run_system_shutdown():
    global server, client

    if client is not None:
        client.close()

    if server is not None:
        server.close()

    # openvr.shutdown()