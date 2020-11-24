class ConvertibleNbr:
    """Number used for easier conversions in all bases.
    Avoids a lot of conditions and checking in main program.
    """

    def __init__(self, value, type: str):
        """Initiates ConvertibleNbr.
        Value can be str or int, bin in form of "0100100", hex in form of "4FE1", dec in form of "123456729".
        Type must be "dec" or "bin" or "hex" : can raise ValueError if it is wrongly typed.
        """

        type = type.upper()
        if not(type == int or type == str):
            raise ValueError("Type of value must be int or str")

        if (type(value) == str and not value.isdigit()) and type == "DEC":
            raise ValueError(
                "Value must be an integer or a string full of digits if type is DEC.")
        elif type == "BIN":
            for i in value:
                if not(i == 1 or i == "1" or i == 0 or i == "0"):
                    raise ValueError(
                        "Value must contain only 0s and 1s if type is BIN")
        elif type == "HEX":
            values = ["0", "1", "2", "3", "4", "5", "6",
                      "7", "8", "9", "A", "B", "C", "D", "E", "F"]
            value = value.upper()
            for i in value:
                if not i in values:
                    raise ValueError(
                        "Value must exclusively be one of these : 0 1 2 3 4 5 6 7 8 9 A B C D E F")
        elif type == "DEC":
            value = int(value)
        else:
            raise ValueError("Type must be DEC, BIN or HEX")

        self = value
        self.type = type

    def get_dec(self) -> int:
        """Returns number in decimal base.
        """
        if self.type == "DEC":
            return self
        elif self.type == "BIN":
            ret_val = 0
            count = 0
            while count < len(self):
                if self[(count+1)*-1] == "1":
                    ret_val += 2**(count)
                count += 1
            return ret_val
        elif self.type == "HEX":
            pass  # A FAIRE
        else:
            raise AttributeError

    def get_bin(self) -> str:
        """Returns number in binary base.
        """
        if self.type == "BIN":
            return self
        elif self.type == "DEC":
            x = self
            if x == 0:
                return "0"
            nbr_bin = ""
            while x > 0:
                nbr_bin = str(x % 2) + nbr_bin
                x //= 2
            return nbr_bin
        elif self.type == "HEX":
            pass  # A FAIRE
        else:
            raise AttributeError

    def get_hex(self) -> str:
        if self.type == "HEX":
            return self
        elif self.type == "DEC":
            x = self
            hexa = ['0', '1', '2', '3', '4', '5', '6', '7',
                    '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            ret_val = ""
            while x > 0:
                ret_val = hexa[x % 16]+ret_val
                x //= 16
            return ret_val

        elif self.type == "BIN":
            pass  # A FAIRE
        else:
            raise AttributeError
