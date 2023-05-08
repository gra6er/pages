from django.shortcuts import render
from .models import Report, Block
from .services.block_processor import BlockProcessor


def home(request):
    report_list = Report.objects.order_by('-gen_time')
    context = {'report_list': report_list}
    return render(request, 'report/home.html', context)


def report_detail(request, report_id):
    block_list = Block.objects.filter(report__id=report_id)

    block_processor_list = [BlockProcessor(block) for block in block_list]

    report = Report.objects.get(id=report_id)
    context = dict(block_processor_list=block_processor_list, report=report)
    return render(request, 'report/report.html', context)
