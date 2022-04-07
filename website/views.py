from django.shortcuts import render


def index(request, uuid, template_name='website/index.html'):
    return render(
        request,
        template_name,
        {
            'uuid': uuid,
        },
    )
