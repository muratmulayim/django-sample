from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View

from myapp.forms.NameForm import NameForm

context = {
    "some_list": [
        [
            {
                "name": "1.1"
            },
            {
                "name": "1.2"
            }
        ],
        [
            {
                "name": "2.1"
            }, {
                "name": "2.2"
            }
        ]
    ]
}

GET = 'GET'
POST = 'POST'
error_message = ""


def first(request):
    if request.method == GET:
        m_context = context
        m_context.update({"title": "Regular app sample by function call"})
        return render_to_response('first.html', m_context)


class Second(View):
    template_name = 'first.html'

    def dispatch(self, *args, **kwargs):
        return super(Second, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        return context

    def get(self, request, *args, **kwargs):
        m_context = self.get_context_data()
        m_context.update({"title": "Regular app sample by class as view"})
        return render_to_response(self.template_name, m_context)


def get_name(request):
    if request.method == POST:
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/myapp/first')
        else:
            global error_message
            error_message = "Form is not valid"
            return HttpResponseRedirect('/myapp/error')
    else:
        m_context = {
            'form': NameForm(),
            "title": "Regular app sample by Form as view"
        }
        return render(request, 'name.html', m_context)


def error_page(request):
    global error_message
    m_context = {
        'error_message': error_message
    }
    error_message = ""
    return render_to_response('error.html', m_context)