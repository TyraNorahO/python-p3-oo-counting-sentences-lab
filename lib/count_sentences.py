#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        import re
        # Split the string by '.', '!', or '?'
        sentences = re.split(r'[.!?]', self._value)
        # Filter out empty strings
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)

# Example usage:
if __name__ == "__main__":
    string = MyString()
    string.value = "This is a string! It has three sentences. Right?"
    print(string.count_sentences())  # => 3

    string.value = "Is this a sentence? Yes! And this is another one."
    print(string.count_sentences())  # => 3

    print(string.is_sentence())  # => False
    print(string.is_question())  # => False
    print(string.is_exclamation())  # => False

    string.value = "This is a test."
    print(string.is_sentence())  # => True
