import random
import requests
import re, math
from collections import Counter
from django.shortcuts import render, redirect
from django.http import HttpResponse
from topic.models import Topic, NewWords, Speaking, Reading, Listening
from exams.models import Exams, Questions, Choices
from partofspeech.models import PartOfSpeechs
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GetAllTopicSerializer, GetNewwordSerializer, GetPoSSerializer, GetSpeakingSerializer, \
GetListeningSerializer, GetReadingSerializer, GetExamsSerializer, GetQuestionsSerializer, GetGrammarsSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from grammars.models import Grammars
# Create your views here.


class homepage(View):
    def get(self, request):
        return render(request, 'index.html')


class topic(View):
    def get(self, request):
        topic = Topic.objects.all()
        return render(request, 'topic.html', {'topic': topic})


class TuVung(View):
    def get(self, request):
        word = NewWords.objects.filter()
        return render(request, 'tuvung.html', {'newword': word})


class NguPhap(View):
    def get(self, request):
        nguphap = Grammars.objects.filter()
        return render(request, 'nguphap.html', {'nguphap': nguphap})


class newword(View):
    def get(self, request, **kwargs):
        newword = NewWords.objects.get(id=kwargs.get('pk'))
        allnewword = NewWords.objects.filter()
        return render(request, 'newword.html', {'newword': newword, 'allnewword': allnewword})


class speaking(View):
    word = Speaking.objects.filter()
    for a in random.choices(word):
        def get(self, request):
            for b in random.choices(speaking.word):
                speaking.a = b
                return render(request, 'speaking.html', {'oneword': speaking.a})

        def post(self, request):
            data = request.POST.get('record')
            mau = 'white'
            import speech_recognition as sr
            # get audio from the microphone
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak:")
                audio = r.listen(source)

            try:
                output = " " + r.recognize_google(audio)
            except sr.UnknownValueError:
                output = "Could not understand audio"
            except sr.RequestError as e:
                output = "Could not request results; {0}".format(e)
            data = output

            return render(request, 'speaking.html', {'data': data, 'mau': mau, 'speak': speaking.a})



class listening(View):
    sound = Listening.objects.filter()
    for a in random.choices(sound):
        def get(self, request):
            for b in random.choices(listening.sound):
                listening.a = b
            return render(request, 'listening.html', {'sound': listening.a})

        def post(self, request):
            check = request.POST['check']
            Word = re.compile(r'\w+')

            def get_cosine(vec1, vec2):
                intersection = set(vec1.keys()) & set(vec2.keys())
                numerator = sum([vec1[x] * vec2[x] for x in intersection])

                sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
                sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
                denominator = math.sqrt(sum1) * math.sqrt(sum2)

                if not denominator:
                    return 0.0
                else:
                    return float(numerator) / denominator

            def text_to_vector(text):
                words = Word.findall(text)
                return Counter(words)

            text1 = str(check)
            text2 = str(listening.a.DapAn)

            vector1 = text_to_vector(text1)
            vector2 = text_to_vector(text2)
            percent = 'Độ chính xác'
            cosine = get_cosine(vector1, vector2)
            return render(request, 'listening.html', {'test': round(cosine*100, 2), 'sound3': listening.a, 'percent': percent})


class listening2(View):
    def get(self, request):
        value = request.GET['inp']
        sound = value
        import pyttsx3
        ojb = pyttsx3.init()
        ojb.setProperty('rate', 120)
        ojb.setProperty('volume', 1.0)
        ojb.say(value)
        ojb.runAndWait()
        #return redirect('http://127.0.0.1:8000/luyennghe/')
        return render(request, 'listening.html', {'sound2': sound})


class reading(View):
    def get(self, request):
        return render(request, 'reading.html')


class ReadingEducation(View):
    read = Reading.objects.filter(Topic=1)
    for a in random.choices(read):
        def get(self, request):
            for b in random.choices(ReadingEducation.read):
                ReadingEducation.a = b

            question = Questions.objects.all()
            return render(request, 'readingeducation.html', {'read': ReadingEducation.a, 'question': question})


class ReadingTravels(View):
    read = Reading.objects.filter(Topic=10)
    for a in random.choices(read):
        def get(self, request):
            for b in random.choices(ReadingTravels.read):
                ReadingTravels.a = b

            question = Questions.objects.all()
            return render(request, 'readingtravels.html', {'read': ReadingTravels.a, 'question': question})


class ReadingHistory(View):
    read = Reading.objects.filter(Topic=7)
    for a in random.choices(read):
        def get(self, request):
            for b in random.choices(ReadingHistory.read):
                ReadingHistory.a = b

            question = Questions.objects.all()
            return render(request, 'raedinghistory.html', {'read': ReadingHistory.a, 'question': question})


class GetAllSpeaking(ListCreateAPIView):
    model = Speaking
    serializer_class = GetSpeakingSerializer

    def get_queryset(self):
        return Speaking.objects.all()


class GetAllGrammars(ListCreateAPIView):
    model = Grammars
    serializer_class = GetGrammarsSerializer

    def get_queryset(self):
        return Grammars.objects.all()


class GetAllListening(ListCreateAPIView):
    model = Listening
    serializer_class = GetListeningSerializer

    def get_queryset(self):
        return Listening.objects.all()


class GetAllReading(ListCreateAPIView):
    model = Reading
    serializer_class = GetReadingSerializer

    def get_queryset(self):
        return Reading.objects.all()


class GetAllExam(ListCreateAPIView):
    model = Exams
    serializer_class = GetExamsSerializer

    def get_queryset(self):
        return Exams.objects.all()


class GetAllQuestions(ListCreateAPIView):
    model = Questions
    serializer_class = GetQuestionsSerializer

    def get_queryset(self):
        return Questions.objects.all()


class GetAllPos(ListCreateAPIView):
    model = PartOfSpeechs
    serializer_class = GetPoSSerializer

    def get_queryset(self):
        return PartOfSpeechs.objects.all()


class GetAllTopic(ListCreateAPIView):
    model = Topic
    serializer_class = GetAllTopicSerializer

    def get_queryset(self):
        return Topic.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = GetAllTopicSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Thêm chủ đề thành công!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Thêm chủ đề thất bại!'
        }, status=status.HTTP_400_BAD_REQUEST)


class GetTopic(APIView):

    def get(self, request, **kwargs):
        topic = Topic.objects.get(id=kwargs.get('pk'))
        mydata = GetAllTopicSerializer(topic)
        return Response(data=mydata.data, status=status.HTTP_200_OK)


class UpdateDeleteTopic(RetrieveUpdateDestroyAPIView):
    model = Topic
    serializer_class = GetAllTopicSerializer

    #def get_queryset(self):
    #   return Topic.objects.all()

    def put(self, request, *args, **kwargs):
        topic = get_object_or_404(Topic, id=kwargs.get('pk'))
        serializer = GetAllTopicSerializer(topic, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Sửa chủ đề thành công!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Sửa chủ đề không thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        topic = get_object_or_404(Topic, id=kwargs.get('pk'))
        topic.delete()

        return JsonResponse({
            'message': 'Xóa chủ đề thành công!'
        }, status=status.HTTP_200_OK)


class GetAllNewword(ListCreateAPIView):
    model = NewWords
    serializer_class = GetNewwordSerializer

    def get_queryset(self):
        return NewWords.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = GetNewwordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Thêm từ mới thành công!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Thêm từ mới thất bại!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteNewword(RetrieveUpdateDestroyAPIView):
    model = NewWords
    serializer_class = GetNewwordSerializer

    def get_queryset(self):
       return NewWords.objects.all()

    def put(self, request, *args, **kwargs):
        newword = get_object_or_404(NewWords, id=kwargs.get('pk'))
        serializer = GetNewwordSerializer(NewWords, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Sửa từ mới thành công!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Sửa từ mới không thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        newword = get_object_or_404(NewWords, id=kwargs.get('pk'))
        newword.delete()

        return JsonResponse({
            'message': 'Xóa từ mới thành công!'
        }, status=status.HTTP_200_OK)


class Education(ListCreateAPIView):
    def get(self, request):
        newword = NewWords.objects.filter(Topic=1)
        return render(request, 'education.html', {'newword': newword})


class Travels(ListCreateAPIView):
    def get(self, request):
        newword = NewWords.objects.filter(Topic=10)
        return render(request, 'travels.html', {'newword': newword})


class History(ListCreateAPIView):
    def get(self, request):
        newword = NewWords.objects.filter(Topic=7)
        return render(request, 'history.html', {'newword': newword})


class AddNewword(View):
    def get(self, request):
        topic_list = Topic.objects.filter()
        pos_list = PartOfSpeechs.objects.filter()
        return render(request, 'addnewword.html',{'topic_list':topic_list,'pos_list':pos_list})
    def post(self, request):
        topic_id = request.POST['topic']
        topic = Topic.objects.get(id=topic_id)
        TenTA = request.POST['TenTA']
        NghiaTV = request.POST['NghiaTV']
        pos_id = request.POST['pos']
        pos = PartOfSpeechs.objects.get(id=pos_id)
        VdTA = request.POST['VdTA']
        VdTV = request.POST['VdTV']
        PhatAm = request.POST['PhatAm']
        Sound = request.POST['Sound']
        newword = NewWords.objects.create(Topic=topic,
                                          Sound=Sound,
                                          TenTA=TenTA,
                                          NghiaTV=NghiaTV,
                                          PoS=pos,
                                          VdTA=VdTA,
                                          VdTV=VdTV,
                                          PhatAm=PhatAm)
        newword.save()
        return redirect('http://127.0.0.1:8000/tuvung/')
