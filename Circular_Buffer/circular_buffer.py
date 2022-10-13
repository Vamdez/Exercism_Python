class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lst_add = []

    def read(self):
        if len(self.lst_add) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        resp = self.lst_add[0]
        self.lst_add.pop(0)
        return resp

    def write(self, data):
        if len(self.lst_add) >= self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.lst_add.append(data)

    def overwrite(self, data):
        if len(self.lst_add) < self.capacity:
            self.lst_add.append(data)
        else:
            self.lst_add.pop(0)
            self.lst_add.append(data)

    def clear(self):
        self.lst_add.clear()

