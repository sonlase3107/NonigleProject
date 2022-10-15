from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.emails.models import Unity
from apps.emails.serializers import UnitySerializer
from datetime import date

class UnityAPIView(APIView):
    def get(self, request):
        try:
            unity_list = Unity.objects.all()
            serializer_unity = UnitySerializer(unity_list, many=True)
            return Response(serializer_unity.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Faill"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            if request.method == 'POST':
                print(request.data)
                serializer_unity = UnitySerializer(data=request.data)
                if serializer_unity.is_valid():
                    print('OK')
                    serializer_unity.save()
                return Response({"message": "OK"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"message": "Faill"}, status=status.HTTP_400_BAD_REQUEST)


def renderCar(request):
    today = date.today()
    d2 = today.strftime("%B %Y")
    unity_list = Unity.objects.all()
    serializer_unity = UnitySerializer(unity_list, many=True)
    context = {
        'emails_list': serializer_unity.data,
        'current_date': d2
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))
