from nltk import word_tokenize

from Models.InputModel import InputModel


def tokenize(input: InputModel):
    """
        Tokeniza o texto fornecido.

        Args:
            input (InputModel): O objeto de entrada contendo o texto a ser tokenizado.

        Returns:
            list: Uma lista de tokens (palavras) extraídos do texto fornecido.
     """
    tokens = word_tokenize(input)
    return tokens
