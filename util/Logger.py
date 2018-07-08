PREFIX = "\t[BlenderVR-Desktop]"
POSTFIX = "\n"


class Logger:

    @staticmethod
    def i(*msg):
        global PREFIX
        global POSTFIX
        print(PREFIX, "[INFO]", msg, POSTFIX)

    @staticmethod
    def d(*msg):
        global PREFIX
        global POSTFIX
        print(PREFIX, "[DEBUG]", msg, POSTFIX)

    @staticmethod
    def e(*msg):
        global PREFIX
        global POSTFIX
        print(PREFIX, "[ERROR]", msg, POSTFIX)
