import spacy
nlp = spacy.load('en_core_web_md')

# We open the movies.txt file and read it

movie_file = open("movies.txt", "r")

# We add all elements from the file to the movies_lst

movies_lst = []

for movie in movie_file:
    movies_lst.append(movie)

# We create a variable to compare to

movie_to_compare = '''Planet Hulk: Will he save their world or destroy it? When the Hulk becomes too dangerous for the 
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

model_movie = nlp(movie_to_compare)

# We create a list of similarities of each movie with the movie_to_compare

compare_list = []
for movie in movies_lst:
    similarity = nlp(movie).similarity(model_movie)
    compare_list.append((movie[0:7], similarity))
    print(movie [0:7] + " - ", similarity)

# We use the first item in the list to compare to the model_movie

high_similarity = nlp(movies_lst[0]).similarity(model_movie)

# We loop through the list and if the similarity of the comparison of any of the movies is higher than high similarity,
# we replace the value of high similarity

for movie in movies_lst:
    similarity = nlp(movie).similarity(model_movie)
    if similarity > high_similarity:
        high_similarity = similarity

# We loop through the compare_list of movies and similarities and we find the title of the movie whose probability equals to the one with the highest similarity

for movie in range(len(compare_list)):
    if compare_list[movie][1]== high_similarity:
        best_movie = compare_list[movie][0]
        
        # We print out the suggestion to the user
        
        print(f"Based on your previous choice we would recomment to watch {best_movie}")


