import weasyprint
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
import tempfile

from untitled import settings


def generate_pdf(request):
    paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
    html_string = render_to_string('report.html', {'paragraphs': paragraphs})
    # return render(request,'report.html')
    html = HTML(string=html_string)
    # html=HTML(string=rendered_html,
    #      base_url=settings.SITE_URL).write_pdf(stylesheets=[CSS(settings.STATIC_ROOT + '/assets/static/report.css')])
    # html.write_pdf(target='/tmp/mypdf.pdf')
    weasyprint.HTML(string=html_string,
         base_url=settings.SITE_URL).write_pdf(stylesheets=[CSS('/home/ali/pr/rsttest/untitled/assets/static/report.css')],target="sss222s.pdf")
    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    # with open('report.html', 'r') as myfile:
    #     html_str = myfile.read()
    #
    # template = Template(html_message)
    # context = Context({'some_key': 'some_value'})
    # rendered_str = template.render(context)
    #
    #
    # weasyprint.HTML(string=rendered_str).write_pdf('generated.pdf')