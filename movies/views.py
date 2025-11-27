from django.shortcuts import render , HttpResponse

moviesList = ['Wolf of wall street' , 'Need for Speed' , 'Scarface' , 'Casino']
seriesList = ['True Detective' , 'Breaking Bad' , 'Better Call Soul' , 'Rick and Morty']

# Create your views here.
def base(request):
	return render(request, "movies/base.html" , {})



def movie(request):
	context = {
		'movies' : moviesList
	}
	return render(request , "movies/movie.html" , context)
#movies/templates/movies/movie.html


def contact(request):
	return render(request , "movies/contact.html" , {})
#movies/templates/movies/about.html

