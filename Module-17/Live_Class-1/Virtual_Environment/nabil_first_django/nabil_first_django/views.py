
# If we hit a URL, that URL has a VIEW against it
# Then that View is shown from the db
# View could be any design, text



# There are 2 types of VIEW -> i. Function Based, ii. Class based
# Here we used Function based



from django.http import HttpResponse


# 1 URL can hit only 1 function
# Here we are requesting and getting a response against it
def home(request):
    return HttpResponse ("Hello Djangooo");