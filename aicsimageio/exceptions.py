

class UnsupportedFileFormatError(Exception):
    """
    This exception is intended to communicate that the file extension is not one of
    the supported file types and cannot be parsed with AICSImage.
    """

    def __init__(self, target, **kwargs):  # removed Argument Typing to allow py2.7 (W, Micro)
        super().__init__(**kwargs)
        self.target = target

    def __str__(self):
        return f"AICSImage module does not support this image file type: \t{self.target}"


class InvalidDimensionOrderingError(Exception):
    """
    A general exception that can be thrown when handling dimension ordering or validation. Should be provided a message
    for the user to be given more context.
    """

    def __init__(self, message: str, **kwargs):
        super().__init__(**kwargs)
        self.message = message

    def __str__(self):
        return self.message