from applications.home.models import Home

def footer_data(request):
    try:
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
    except:
        #In case you don't have anything loaded, return:
        return {
            'title':'title',
            'description':'description',
            'about_title':'about_title',
            'about_text':'about_text',
            'contact_email':'contact_email',
            'subject_email':'subject_email',
            'body_email':'body_email',
            'web':'web',
            'repository':'repository',
            'phone':'phone'
        }
