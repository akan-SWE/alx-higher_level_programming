#!/usr/bin/python3


if __name__ == '__main__':

    import hidden_4

    def hidden_discoveries():
        """ Prints all names defined by the compiled module @hidden_4

        :return: void (Nothing
        """
        names = dir(hidden_4)  # get all identifier in module

        for name in names:
            if name[:2] != '__':
                print(name)


    hidden_discoveries()
