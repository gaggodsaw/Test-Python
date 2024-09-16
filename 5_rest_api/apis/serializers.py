from rest_framework import serializers

from .models import School, Classroom, Teacher, Student

class SchoolSerializer(serializers.ModelSerializer):
    classrooms_count = serializers.SerializerMethodField()
    teachers_count = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address', 'classrooms_count', 'teachers_count', 'students_count']
    
    def get_classrooms_count(self, obj):
        return obj.classrooms.count()

    def get_teachers_count(self, obj):
        return obj.teachers.count()

    def get_students_count(self, obj):
        return Student.objects.filter(classroom__school=obj).count()

class ClassroomSerializer(serializers.ModelSerializer):
    teachers_count = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()

    class Meta:
        model = Classroom
        fields = ['id', 'year', 'section', 'school', 'teachers_count', 'students_count']

    def get_teachers_count(self, obj):
        return obj.teachers.count()

    def get_students_count(self, obj):
        return obj.students.count()

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender', 'school', 'classrooms']

class StudentSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all())
    school = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender', 'classroom', 'school']

    def get_school(self, obj):
        return SchoolSerializer(obj.classroom.school).data.get('id')