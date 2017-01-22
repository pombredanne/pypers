import os.path as op
from django.http import HttpResponse
from django.conf import settings
from papers.models import Paper


def get_paper(request):
    if 'paper_id' not in request.GET:
        return HttpResponse("Please specify a paper id.")
    paper = Paper.objects.get(pk=request.GET.get('paper_id'))
    print(paper)
    if not paper.pdf_path:
        return HttpResponse('Not found.')
    root = settings.PAPERS_LIBRARY_PATH
    path = op.join(root, paper.pdf_path or '')
    with open(path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=paper.pdf'
        return response
