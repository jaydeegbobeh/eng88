class MovieRating:
    def rated_u(self):
        return "Everyone can watch"

    def rated_pg(self):
        return "General viewing, but some scenes may be unsuitable for young children"

    def rated_12(self):
        return "No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult."

    def rated_15(self):
        return "No one younger than 15 may see a 15 film in a cinema."

    def rated_18(self):
        return "No one younger than 18 may see an 18 film in a cinema."

print("Film Ratings:\nU\nPG\n12a\n15\n18")
sel = MovieRating()

select_rating = (input("Please enter the film rating you would like information about or enter 'exit' to quit\n"))
while select_rating.lower() != "exit":
    if select_rating.upper() == "U":
        print(sel.rated_u())
    elif select_rating.upper() == "PG":
        print(sel.rated_pg())
    elif select_rating == "12a":
        print(sel.rated_12())
    elif select_rating == "15":
        print(sel.rated_15())
    elif select_rating == "18":
        print(sel.rated_18())

