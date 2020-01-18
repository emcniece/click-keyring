import click
import click_keyring
#from click_keyring import KEYRING


import ipdb

@click.command()
@click.option(
    '--keyentry',
    prompt='Keyring entry title',
    help='Name of the keyring entry',
    #type=KEYRING,
    #servicename=
)
def hello(keyentry):
    ipdb.set_trace()
    """Simple program that greets NAME for a total of COUNT times."""
    print(keyentry)

if __name__ == '__main__':
    hello()
