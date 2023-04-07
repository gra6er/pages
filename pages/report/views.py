from django.shortcuts import render
from .models import Report, Block
from .services.block_calculations import BlockCalculation


def home(request):
    report_list = Report.objects.order_by('-gen_time')
    context = {'report_list': report_list}
    return render(request, 'report/home.html', context)


def report_detail(request, report_id):
    block_list = Block.objects.filter(report__id=report_id)

    block_calc_list = [BlockCalculation(block) for block in block_list]

    for block_calc in block_calc_list:
        block_calc.block.text = str(block_calc.calculation.data)

    report = Report.objects.get(id=report_id)
    context = dict(block_calc_list=block_calc_list, report=report)
    return render(request, 'report/report.html', context)
