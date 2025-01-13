import configparser
from pathlib import Path

# Get the dynamic path to the configuration file
base_dir = Path(__file__).resolve().parent.parent  # Adjust based on your project structure
config_path = base_dir / "Configurations" / "config.ini"

# Initialize the configparser
config = configparser.RawConfigParser()
config.read(config_path)

class ReadConfig:
    @staticmethod
    def get_Application_url():
        url = config.get('common info', 'pageurl')
        return url

    @staticmethod
    def get_user_name():
        user_name = config.get('common info', 'original_username')
        return user_name

    @staticmethod
    def get_password():
        pass_word = config.get('common info', 'original_password')
        return pass_word
