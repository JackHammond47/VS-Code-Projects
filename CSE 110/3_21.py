max_opening_weekend = 0
max_movie_name = ''

with open('CSE 110/harry-potter.txt') as movie_file:
    movie_file.readline()
    for line in movie_file:
        line = line.strip()
        movie_data = line.split(',')
        opening_weekend = int(movie_data[3])
        title_by_parts = movie_data[0].split(' ')
        if 'of' in title_by_parts:
            if opening_weekend > max_opening_weekend:
                max_opening_weekend = opening_weekend
                max_movie_name = movie_data[0]
                max_movie_data = movie_data

        

print(f'The highest opening weekend with "of" in the title is {max_movie_data[0]} with ${max_opening_weekend:,}.')

# with open('CSE 110/harry-potter.txt') as movie_file:
#     movie_file.readline()
#     for line in movie_file:
#         line = line.strip()
#         movie_data = line.split(',')
#         release_date_parts = movie_data[5].split(' ')
#         if release_date_parts[0] == 'Jul':
#             print(f'{movie_data[0]} was released on {movie_data[5]}.')
