from django.shortcuts import render
import logging

# 创建日志记录器
logger = logging.getLogger('log')


def index(request):
    # 输出日志
    logger.debug('测试logging模块debug')
    logger.info('测试logging模块info')
    logger.error('测试logging模块error')

    context = {'value': "这是jinja2"}
    return render(request, 'index.html', locals())
