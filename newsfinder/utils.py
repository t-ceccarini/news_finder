import os

def get_api_key(env_var):
    """
    Retrieve an API key from environment variables or prompt the user.
    """
    if not os.environ.get(env_var):
        os.environ[env_var] = input(f"Enter {env_var}: ")
    return os.environ[env_var]