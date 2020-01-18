import os
import click
import keyring


class KeyringParamType(click.ParamType):
    """Helper for converting values through types.  The following is
    necessary for a valid type:
    *   it needs a name
    *   it needs to pass through None unchanged
    *   it needs to convert from a string
    *   it needs to convert its result type through unchanged
        (eg: needs to be idempotent)
    *   it needs to be able to deal with param and context being `None`.
        This can be the case when the object is used with prompt
        inputs.
    """
    name = "keyring"

    def __init__(self, servicename=os.environ.get('USER')):
        self.servicename = servicename


    def convert(self, value, param, ctx):
        try:
            entry = keyring.get_password(self.servicename, value)
        except TypeError:
            self.fail(
                "expected string for int() conversion, got "
                f"{value!r} of type {type(value).__name__}",
                param,
                ctx,
            )
        except ValueError:
            self.fail(f"{value!r} is not a valid integer", param, ctx)


    def __repr__(self):
        return 'KEYRING'
        #return 'KeyringParamType(%r, %r)' % (self.servicename)

KEYRING = BasedKeyringParamType()