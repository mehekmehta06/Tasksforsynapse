from django.http import JsonResponse
from django.views.decorators.http import require_GET
#import math


@require_GET

                
def prime(request):
    a=int(request.GET.get('a'))
    b=int(request.GET.get('b'))
    
    if a<1 or b<a:
        return JsonResponse({'error':'wrong range'},status=400)
    result={}
    for num in range(a,b):
        if num>1:
            for j in range(2,num):
                if int(num)%int(j)==0:
                    break
            else:
                result[num]=bin(num)[2:]
    return JsonResponse({'prime':result})





    
    