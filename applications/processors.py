from applications.home.models import Home

def footer_data(request):
    home = Home.objects.latest('created')

    return {
        'title':home.title,
        'description':home.description,
        'about_title':home.about_title,
        'about_text':home.about_text,
        'contact_email':home.contact_email,
        'subject_email':home.subject_email,
        'body_email':home.body_email,
        'web':home.web,
        'repository':home.repository,
        'phone':home.phone
    }
