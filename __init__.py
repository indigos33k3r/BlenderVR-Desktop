from util.Logger import Logger
import blendervr

ready = blendervr.check_system_ready()

if ready:
    blendervr.run_system_startup()

    blendervr.run_system_shutdown()
else:
    Logger.e("Please install SteamVR and connect your HMD")
    blendervr.run_system_shutdown()
