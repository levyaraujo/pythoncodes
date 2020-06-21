from typing import List

books_stack: List[str] = []

# Adicionando livros ao topo da pilha
books_stack.append('Livro 1')
books_stack.append('Livro 2')
books_stack.append('Livro 3')
books_stack.append('Livro 4')

# Enquanto houve livros na pilha remova-os e retorne seus nomes
while books_stack:
    book = books_stack.pop()
    print(book)
