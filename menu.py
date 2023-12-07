

class Welcome:
    def __init__(self, tool_name):
        self.tool_name = tool_name

    def display_welcome_message(self):
        welcome_message = f"\n========================= Welcome to ============================= {self.tool_name}"
        print(welcome_message)


if __name__ == "__main__":
    penkraken_welcome = Welcome("""
==================================================================                      
                      ____  __.              __ 
______   ____   ____ |    |/ _|___________  |  | __ ____   ____  
\____ \_/ __ \ /    \|      < \_  __ \__  \ |  |/ // __ \ /    \ 
|  |_> >  ___/|   |  \    |  \ |  | \// __ \|    <\  ___/|   |  \\
|   __/ \___  >___|  /____|__ \|__|  (____  /__|_ \\___  >___|  /
|__|        \/     \/        \/           \/     \/    \/     \/  \n
==================================================================
=================================================================="""
    )

    # Display Welcome message
    penkraken_welcome.display_welcome_message()