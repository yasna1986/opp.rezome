# کلاس Movie
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print(f"Movie '{self.title}' rented")
        else:
            print(f"Movie '{self.title}' is already rented")

    def return_movie(self):
        if not self.available:
            self.available = True
            print(f"Movie '{self.title}' returned")
        else:
            print(f"Movie '{self.title}' was not rented")

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.director} ({self.year}) - {status}"

# کلاس VideoStore
class VideoStore:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"Movie added: {movie.title}")

    def show_movies(self):
        print("Available movies:")
        for movie in self.movies:
            print(movie)

    def search(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        print(f"No movie found with title '{title}'")
        return None

# تعریف فیلم‌ها
movie1 = Movie("Inception", "Christopher Nolan", 2010)
movie2 = Movie("The Godfather", "Francis Ford Coppola", 1972)
movie3 = Movie("Spirited Away", "Hayao Miyazaki", 2001)
movie4 = Movie("The Dark Knight", "Christopher Nolan", 2008)
movie5 = Movie("Pulp Fiction", "Quentin Tarantino", 1994)

# اضافه کردن به فروشگاه
store = VideoStore()
for m in [movie1, movie2, movie3, movie4, movie5]:
    store.add_movie(m)

store.show_movies()
