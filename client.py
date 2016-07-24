# Import the 21 Developer Libraries
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests


# Client side wallet
wallet = Wallet()
requests = BitTransferRequests(wallet)


# server address
server_url = 'http://localhost:5000/'


def buy_translation():

    # Ask user for input text in english
    print("Welcome to English-to-Chinese Translation.\n")
    inp_text = input("Enter the English text that you would like translated into Chinese:\n")

    sel_url = server_url+'translate?text={0}&payout_address={1}'
    response = requests.get(url=sel_url.format(inp_text, wallet.get_payout_address()))

    # Print the Chinese translation
    print("The following is the translation of the text you input.\n")
    print(response.text)

if __name__=='__main__':
    buy_translation()
