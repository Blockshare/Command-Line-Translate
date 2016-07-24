# Import Developer Libraries
import json
import click

# Import 21 Developer Libraries
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

wallet = Wallet()
requests = BitTransferRequests(wallet)


server_url = 'http://localhost:4004/'

@click.command()
@click.argument('text')
def cli(text):
    """ Call the Translation API hosted on the micropayments server. """
    #click.echo("Welcome to the Instant Translation Command Line Tool.\n")

    sel_url = server_url+'translate?text={0}&payout_address={1}'
    response = requests.get(url=sel_url.format(text, wallet.get_payout_address()))

    #click.echo("The following is the translation of the text you input.\n")
    click.echo(response.text)
