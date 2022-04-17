from django.shortcuts import render


class MainPage:
    def home(request, template='home.html'):
        
        return render(
            request=request,
            template_name=template,
        )


    def features(request): 
        raise NotImplementedError()



