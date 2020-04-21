from django.http import JsonResponse
from rest_framework.decorators import api_view

from .tkb_ptit import *


@api_view(['GET', 'POST'])
def get_tkb_ptit(request, *args, **kwargs):
    # os.environ['HTTP_PROXY'] = "http://127.0.0.1:8888"
    # os.environ['HTTPS_PROXY'] = "http://127.0.0.1:8888"
    if request.method == 'GET':
        _type = kwargs.get('type')
        data_req = request.GET
        masv = data_req.get('masv')
        tkb = extractTKB_PTIT(masv=masv)
        if _type == 'text':
            info = tkb.get_text()
        elif _type == 'img':
            info = tkb.get_img()
        else:
            info = None
        if info:
            return JsonResponse(info, json_dumps_params={
                "ensure_ascii": False,
                'indent': 4
            })
        return JsonResponse({'message': 'error'}, json_dumps_params={
            "ensure_ascii": False,
            'indent': 4
        })
    if request.method == 'POST':
        _type = kwargs.get('type')
        data_req = request.POST
        masv = data_req.get('masv')
        tkb = extractTKB_PTIT(masv=masv)
        if _type == 'text':
            info = tkb.get_text()
        elif _type == 'img':
            info = tkb.get_img()
        else:
            info = None
        if info:
            return JsonResponse(info, json_dumps_params={
                "ensure_ascii": False,
                'indent': 4
            })
        return JsonResponse({'message': 'error'}, json_dumps_params={
            "ensure_ascii": False,
            'indent': 4
        })
