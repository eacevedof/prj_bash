class color:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    ENDC = "\033[0m"


class DeployStepException(Exception):
    """Forces exception from tag"""

    def __init__(self, message):
        self.message = f"DeployStpeException:[ {message} ]"
        super().__init__(self.message)
