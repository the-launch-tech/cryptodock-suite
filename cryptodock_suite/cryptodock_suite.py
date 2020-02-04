from abc import ABC, abstractmethod
from cryptodock_sdk import CryptoDockSdk
from .actions import *

class CryptoDockSuite(ABC) :
    """
    Collection of analysis tools. Can be extended as a base class.
    Commands are entered from the CryptoDock interface and this is spawned as a NodeJS child process.
    The results are displayed in a matplotlib plot using pandas, numpy, and matplotlib among other popular Python packages.

    To extend the base class add your dictionary map to the custom_map abstractmethod in your own class. Then provide the method for charting.

    In test scenarios (like right now) the alternative test data is used.
    """

    def __init__(self, args) :
        self.map = {**self.get_map(), **self.custom_map()}

        if isinstance(args, list) and len(args) > 3 :
            self.params = args[4]
            self.Sdk = CryptoDockSdk(args)
        else :
            self.Sdk = {}
            self.params = {
                'command': 'AVG_SESSION_TIME',
                'session': 1,
                'strategy': 3,
                'window': 1800,
                'test': True
            }

        self.function = self.map.get(self.params['command'], lambda: "Invalid Command")

        super().__init__()

    @abstractmethod
    def custom_map(self) : pass

    def get_map(self) :
        return {
            'SIGNAL_RATE_OT': self.signal_rate_over_time,
            'ORDER_RATE_OT': self.order_rate_over_time,
            'FILL_RATE_OT': self.fill_rate_over_time,
            'CANCEL_RATE_OT': self.cancel_rate_over_time,
            'AVG_FEE_OT': self.avg_fee_over_time,
            'FUNDS_CHANGE_OT': self.funds_change_over_time,
            'SIDE_RATIO': self.side_ratio,
            'SIDE_RATIO_OT': self.side_ratio_over_time,
            'ORDER_TYPE_RATIO': self.order_type_ratio,
            'ORDER_TYPE_RATIO_OT': self.order_type_ratio_over_time,
            'AVG_SESSION_TIME': self.avg_session_time,
        }

    def has_command(self) :
        return callable(self.function)

    def signal_rate_over_time(self) :
        signal_rate_over_time(params=self.params, Sdk=self.Sdk)

    def order_rate_over_time(self) :
        order_rate_over_time(params=self.params, Sdk=self.Sdk)

    def fill_rate_over_time(self) :
        fill_rate_over_time(params=self.params, Sdk=self.Sdk)

    def cancel_rate_over_time(self) :
        cancel_rate_over_time(params=self.params, Sdk=self.Sdk)

    def avg_fee_over_time(self) :
        avg_fee_over_time(params=self.params, Sdk=self.Sdk)

    def funds_change_over_time(self) :
        funds_change_over_time(params=self.params, Sdk=self.Sdk)

    def side_ratio(self) :
        side_ratio(params=self.params, Sdk=self.Sdk)

    def side_ratio_over_time(self) :
        side_ratio_over_time(params=self.params, Sdk=self.Sdk)

    def order_type_ratio(self) :
        order_type_ratio(params=self.params, Sdk=self.Sdk)

    def order_type_ratio_over_time(self) :
        order_type_ratio_over_time(params=self.params, Sdk=self.Sdk)

    def avg_session_time(self) :
        avg_session_time(params=self.params, Sdk=self.Sdk)
