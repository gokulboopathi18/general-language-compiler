# Python package root

## ToDo
- Lexical Translator : conventions on using `__contains__()` method - ref (https://stackoverflow.com/questions/1964934/what-does-contains-do-what-can-call-contains-function)
- Lexical Traslator : change shebang to intermediate code
- Lexical Translator : python library for tokenization(for lexical analysis / building a lexicial analyser using pythong)
- Lexical Translator : handle strings and quotes (use a state machine)
- Lexical Translator : change variables to ids and create symbol table (blocked by the previous one)
    - State Machine?
    - Everything that is not a translatable token, regular token is an indentifier
    - make an entry in the symbol table (identifier(in language), unique_id, type, current value)
