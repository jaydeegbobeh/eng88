movie_info = input("What film rating would you like information about\n")
if movie_info == "U":
    print("U rated films are suitable for all ages")
elif movie_info == "PG":
    print("General viewing, but some scenes may be unsuitable for young children")
elif movie_info == "12":
    print("Films classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult")
elif movie_info == "15":
    print("No one younger than 15 may view a 15 rated film in the cinema")
elif movie_info == "18":
    print("No one younger than 18 may view an 18 rated film in the cinema")
for exit_code in movie_info:
    if exit_code == "exit":
        break


# select_film_rating = input("Please enter the rating of the film you would like to watch:  ")
# for rating in select_film_rating:
#     if rating == "U" and customer_age >= 0:
#         print("You are old enough to view this film, please continue to ticket purchase")
#     elif rating == "PG" and customer_age >= 0:
#         print("You are old enough to view this film, please continue to ticket purchase ")
#     elif rating == 12 and customer_age >= 12:
#         print("You are old enough to view this film, please continue to ticket purchase")
#     elif rating == 15 and customer_age >= 15:
#         print("You are old enough to view this film, please continue to ticket purchase")
#     elif rating == 18 and customer_age >= 18:
#         print("You are old enough to view this film, please continue to ticket purchase")
#     else:
#         print("You are not old enough to view this film, please try again")



