from rest_framework import serializers
from topic.models import Topic, NewWords, Speaking, Listening, Reading
from partofspeech.models import PartOfSpeechs
from exams.models import Exams, Choices, Questions
from grammars.models import Grammars


class GetAllTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'Chude')


class GetNewwordSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewWords
        fields = ('id', 'Topic', 'TenTA', 'NghiaTV', 'PoS', 'PhatAm', 'Sound')


class GetPoSSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartOfSpeechs
        fields = ('id', 'Tuloai')


class GetSpeakingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaking
        fields = ('id', 'Topic', 'CachDoc', "DapAn")


class GetListeningSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listening
        fields = ('id', 'Topic', 'Sound', "CauHoi", "DapAn")


class GetReadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reading
        fields = ('id', 'Topic', 'NoiDungTA', "NoiDungTV", "Exams")


class GetExamsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exams
        fields = ('id', 'TenExam')


class GetQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ('id', 'Exams', 'CauHoi', "Diem", "DapAnA", "DapAnB", "DapAnC", "DapAnD", "DapAnDung")


class GetGrammarsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grammars
        fields = ('id', 'TenNguPhap', 'NoiDung', 'Exams')