from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import time
from Qshop.settings import ERROR_PATH
from CeleryTask.tasks import sendDing

class MiddleWareTest(MiddlewareMixin):
    def prodess_request(self,request):
        request_ip = request.META["REMOTE_ADDR"]
        if request_ip == "10.10.14.176":
            return HttpResponse("非法ip")

    def process_view(self,request,callback,callback_args,):
        print("")

    def process_exception(self,request,exception):
        if exception:
            with open(ERROR_PATH,"a") as f:
                now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
                content = "[%s]:%s\n"%(now,exception)
                f.write(content)
                sendDing.delay(content)
            return HttpResponse("报错啦:<br> %s"%exception)