from django.shortcuts import render
from django.http import HttpResponse
from .models import Report, Block


def home(request):
    report_list = Report.objects.order_by('-gen_time')
    context = {'report_list': report_list}
    return render(request, 'report/home.html', context)


def report_detail(request, report_id):
    block_list = Block.objects.filter(report__id=report_id)
    report = Report.objects.get(id=report_id)
    context = {
        'block_list': block_list,
        'report': report
    }
    return render(request, 'report/report.html', context)