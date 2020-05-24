from os import path
import sys
import traceback

import argparse

from oauth2client.service_account import ServiceAccountCredentials

__author__ = "Vitaly Saversky"
__date__ = "2020-05-24"
__credits__ = ["Vitaly Saversky"]
__version__ = "1.0.0"
__maintainer__ = "Vitaly Saversky"
__email__ = "larandvit@hotmail.com"
__status__ = "Production"

# The scope for the OAuth2 request.
SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'

class ExitCode():
    SUCCESS = 0
    JSON_KEY_FILE_NOT_FOUND = 1
    TOKEN_FILE_FOLDER_NOT_EXIST = 2

# Defines a method to get an access token from the ServiceAccount object.
def access_token(key_file_path):
    return ServiceAccountCredentials.from_json_keyfile_name(key_file_path, SCOPE).get_access_token()

def app_folder():
    return path.dirname(__file__)

if __name__ == "__main__":
    
    try:
    
        parser = argparse.ArgumentParser(description="Generate Google Analytics token v. {}".format(__version__))
        
        parser.add_argument('-k', 
                            '--keyfilepath', 
                            dest='keyfilepath',
                            required=True,
                            help='Google Analytics json key file path')
        
        parser.add_argument('-t', 
                            '--tokenfilepath', 
                            dest='tokenfilepath',
                            required=True,
                            help='Google Analytics token destination path')
        
        args = parser.parse_args()
        
        key_file_path = args.keyfilepath
        token_file_path = args.tokenfilepath
        
        key_file_folder = path.dirname(key_file_path)
        
        if key_file_folder=='':
            key_file_path = path.join(app_folder(), key_file_path)
        
        if not path.exists(key_file_path):
            print('"{}" json key file is not found'.format(key_file_path))
            sys.exit(ExitCode.JSON_KEY_FILE_NOT_FOUND)
            
        token_file_folder = path.dirname(token_file_path)
        
        if token_file_folder=='':
            token_file_path = path.join(app_folder(), token_file_path)
        else:
            if not path.exists(token_file_folder):
                print('"{}" token destination folder does not exist'.format(token_file_folder))
                sys.exit(ExitCode.TOKEN_FILE_FOLDER_NOT_EXIST)
        
        with open(token_file_path, "w") as f_out:
            token = access_token(key_file_path).access_token
            token_code = 'var ANALYTICS_TOKEN = \'{}\';'.format(token)
            f_out.write(token_code)
            
        print('Google Analytics token has been created succesfully')
            
    except SystemExit:
        pass
    
    except:
        print('Google Analytics token creation has been failed')
        print(traceback.format_exc())