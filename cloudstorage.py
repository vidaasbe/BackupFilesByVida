import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        #upload a file to Dropbox using API v2
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'Z9LNmxoHqjoAAAAAAAAAARuMDK8CHZaqG_9CC6Z4On1gBKQMH33cNtmnFf6aSCj9'
    transferData = TransferData(access_token)

    file_from = input("Please Enter The File Name: ")
    file_to = input("Please Enter Your Dropbox Location: ")

    transferData.upload_file(file_from,file_to)
    print("The File Has Been Successfully Copied")

main()