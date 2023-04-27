
max_chapters = -1
book_with_max = ""

with open("books_and_chapters.txt") as BC_files:
    for line in BC_files:
        parts = line.split(":")
        books = parts[0].strip()
        chapters = int(parts[1])
        scriptures = parts[2].strip()
        
        print(f"Scripture: {scriptures}, Book: {books}, Chapters: {chapters}")
        
        if chapters > max_chapters:
            max_chapters = chapters
            book_with_max = books
            
        
    print(f"The book with thw most chapter is:{book_with_max}")
    print(f"It has {max_chapters} chapters.")