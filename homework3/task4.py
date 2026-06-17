class Movie:
    country = "USA"
    streaming_service = "CinemaPlus"

    def __init__(self, title: str, director: str, year: int, genre: str, duration: int, rating: float) -> None:
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.duration = duration
        self.rating = rating
        self.is_watched = False

    def __str__(self) -> str:
        return f"{self.title} by {self.director} ({self.year})"

    def mark_watched(self) -> None:
        self.is_watched = True

    def update_rating(self, rating: float) -> None:
        if rating < 0 or rating > 10:
            raise ValueError("Рейтинг должен быть от 0 до 10")

        self.rating = rating

    def is_long(self) -> bool:
        return self.duration > 150

    def get_age(self, current_year: int) -> int:
        return current_year - self.year

    def change_service(self, service: str) -> None:
        Movie.streaming_service = service


movie1 = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi", 148, 8.8)
movie2 = Movie("Interstellar", "Christopher Nolan", 2014, "Sci-Fi", 169, 8.7)

print(movie1)
print(movie2)
print(movie1.get_age(2025))
print(movie2.is_long())
movie1.mark_watched()
movie1.update_rating(9.0)
movie2.change_service("MovieHub")
print(movie1.rating)
print(movie1.is_watched)
print(Movie.streaming_service)
