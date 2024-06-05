import json

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from myapp.models import Profile

@csrf_exempt
def ProfileView(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        data =[{'id':profile.id,'name':profile.name,'email':profile.email}  for profile in profiles]
        return JsonResponse(data,safe = False)
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request. POST.get('address')
        mobile_number = request.POST.get('mobile_number')
        if name and email:
            profile = Profile(name=name,email=email,address=address,mobile_number =mobile_number)
            profile.save()
            serialized_obj = serializers.serialize('json', [profile, ])
            data = json.loads(serialized_obj)
            return JsonResponse({'message':'Profile created successfully','data':data[0]})
        else:
            return JsonResponse({'message':'Name and Email are required field'},status =400)
    else:
        return JsonResponse({'message':'Method not allowed'} ,status = 405)

@csrf_exempt
def ProfileDetailView(request,pk):
    """
       Retrieve details of a profile.

       Args:
           request: HTTP request object.
           pk: Primary key of the profile.

       Returns:
           JSON response with profile details or error message.
       """


    try:
        profile = Profile.objects.get(id=pk)
    except Profile.DoesNotExist:
        return JsonResponse({'message':'the profile does not exist'},status =404)
    if request.method == 'GET':
         data = {'id': profile.id, 'name': profile.name, 'email': profile.email,'address':profile.address,'mobile_number':profile.mobile_number}
         return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'message':'Method not allowed'},status = 405)

@csrf_exempt
def ProfileUpdateView(request,pk):
    try:
        profile =Profile.objects.get(id =pk)
    except Profile.DoesNotExist:
        return JsonResponse({'message':'The profile does not exist'},status = 404)
    if request.method =='PUT':
        data = json.loads(request.body)
        name =data.get('name')
        email =data.get('email')
        address =data.get('address')
        mobile_number =data.get('mobile_number')
        if name:
            profile.name =name
        if email:
            profile.email =email
        if address:
            profile.address =address
        if mobile_number:
            profile.mobile_number =mobile_number
        profile.save()
        serialized_obj =serializers.serialize('json',[profile, ])
        data =json.loads(serialized_obj)
        return JsonResponse({'message':'Profile created successfully','data':data[0]})
    else:
        return JsonResponse({'message':'Method not allowed'},status =405)

@csrf_exempt
def ProfileDeleteView(request,pk):
    try:
        profile =Profile.objects.get(id=pk)
    except Profile.DoesNotExist:
        return JsonResponse({'message':'Profile does not EXIST'}, status =404)
    if request.method == 'DELETE':
        profile.delete()
        return JsonResponse({'message':'Profile deleted successfully'},status =404)
    else:
        return JsonResponse({'message':'Method not allowed'},status =405)

