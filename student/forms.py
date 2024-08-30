from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

from .models import *


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CourseSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Course'}))

class BatchSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter BatchNo'}))

class SemSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Semester'}))

class PaperSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Papercode'}))

class ExamSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Examtype'}))

class StudentSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter StudentName'}))

class TransactionSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Student'}))
    

class CourseMasterForm(forms.ModelForm):
    class Meta:
        model = CourseMasterModel
        fields = "__all__"
    
    def clean(self):
        super(CourseMasterForm,self).clean()
        courseid = self.cleaned_data.get('courseid')
        course = self.cleaned_data.get('course')

        if not re.match(r'^\d{1,3}$', str(courseid)):
            self._errors['courseid'] = self.error_class(['Course ID must be Integer of Maximum 3 Digits.'])
        
        if not re.match(r'^[A-Z]{3}$', str(course)):
            self._errors['course'] = self.error_class(['Course should be Exactly 3 uppercase letters.'])

        return self.cleaned_data


class BatchMasterForm(forms.ModelForm):
    class Meta:
        model = BatchMasterModel
        fields = "__all__"

    def clean(self):
        super(BatchMasterForm,self).clean()
        batchid = self.cleaned_data.get('batchid')
        batchno = self.cleaned_data.get('batchno')

        if not re.match(r'^\d{1,3}$', str(batchid)):
            self._errors['batchid'] = self.error_class(['Batch ID must be Integer of Maximum 3 Digits.'])
        
        if not re.match(r'^\d{4}-\d{4}$', str(batchno)):
            self._errors['batchno'] = self.error_class(['Batch No must be in the format YYYY-YYYY.'])

        return self.cleaned_data


class SemMasterForm(forms.ModelForm):
    class Meta:
        model = SemMasterModel
        fields = "__all__"
    
    def clean(self):
        super(SemMasterForm,self).clean()
        semid = self.cleaned_data.get('semid')
        sem = self.cleaned_data.get('sem')

        if not re.match(r'^\d{1,3}$', str(semid)):
            self._errors['semid'] = self.error_class(['Sem ID must be Integer of Maximum 3 Digits.'])
        
        valid_roman_num = ['I', 'II', 'III', 'IV']
        if sem not in valid_roman_num:
            self._errors['sem'] = self.error_class(['Sem must be a valid Roman numerals (Ex:- I, II, III, IV).'])

        return self.cleaned_data


class PaperMasterForm(forms.ModelForm):
    class Meta:
        model = PaperMasterModel
        fields = "__all__"

    def clean(self):
        super(PaperMasterForm,self).clean()
        papercode    = self.cleaned_data.get('papercode')
        papertype    = self.cleaned_data.get('papertype')
        papershtname = self.cleaned_data.get('papershtname')
        papername    = self.cleaned_data.get('papername')

        if not re.match(r'^[A-Z]{3} \d{3}[A-Z]?[P]?$|^[A-Z]{3} \d{3}$', papercode):
            self._errors['papercode'] = self.error_class(['PaperCode must be in the format (COURSE XXX), (COURSE XXXP), (COURSE XXXA) (Ex:- MCA 101)'])
         
        valid_paper_types = [
            'Compul Foundation', 'Core', 'Generic Elective', 
            'Lab', 'Compulsory', 'Open Elective'
        ]
        if papertype not in valid_paper_types:
            self._errors['papertype'] = self.error_class(['PaperType must be one of: Compul Foundation, Core, Generic Elective, Lab, Compulsory, Open Elective.'])

        if not re.match(r'^[A-Z\s\&\(\)\-]+$', papershtname):
            self._errors['papershtname'] = self.error_class(['Paper SHORTName can only contain uppercase letters, spaces, and valid punctuation.'])

        if not re.match(r'^[\w\s\&\(\)\-]+$', papername):
            self._errors['papername'] = self.error_class(['PaperName can contain alphanumeric characters, spaces, and valid punctuation.'])

        return self.cleaned_data


class ExamMasterForm(forms.ModelForm):
    class Meta:
        model = ExamMasterModel
        fields = "__all__"

    def clean(self):
        super(ExamMasterForm,self).clean()
        examid = self.cleaned_data.get('examid')
        examtype = self.cleaned_data.get('examtype')

        if not re.match(r'^\d{1,3}$', str(examid)):
            self._errors['examid'] = self.error_class(['Exam ID must be Integer of Maximum 3 Digits.'])
        
        valid_exam_type = ['Internal-I', 'Internal-II', 'External']
        if examtype not in valid_exam_type:
            self._errors['examtype'] = self.error_class(['ExamType must be one of: Internal-I, Internal-II, External.'])

        return self.cleaned_data


class StudentMasterForm(forms.ModelForm):
    batchno = forms.ModelChoiceField(queryset=BatchMasterModel.objects.all())
    sem = forms.ModelChoiceField(queryset=SemMasterModel.objects.all())
    course = forms.ModelChoiceField(queryset=CourseMasterModel.objects.all())
    
    class Meta:
        model = StudentMasterModel
        fields = ['batchno', 'sem', 'course', 'studregno', 'studname']

    def clean(self):
        super(StudentMasterForm,self).clean()
        studregno = self.cleaned_data.get('studregno')
        studname = self.cleaned_data.get('studname')

        if not re.match(r'^\d{2}\d{2}\d{3}$', str(studregno)):
            self._errors['studregno'] = self.error_class(['Student Registration Number must be in the format: DDYYNNN (Date, Year, Number).'])
        
        if not re.match(r'^[A-Z\s]+$', studname) or len(studname) > 30:
            self._errors['studname'] = self.error_class(['Student Name must be only in uppercase letters MaxLength is 30 .'])

        return self.cleaned_data


class StudentInternalTansForm(forms.ModelForm):
    course    = forms.ModelChoiceField(queryset=CourseMasterModel.objects.all())
    batchno   = forms.ModelChoiceField(queryset=BatchMasterModel.objects.all())
    sem       = forms.ModelChoiceField(queryset=SemMasterModel.objects.all())
    examtype  = forms.ModelChoiceField(queryset=ExamMasterModel.objects.all())
    studname  = forms.ModelChoiceField(queryset=StudentMasterModel.objects.all())
    papername = forms.ModelChoiceField(queryset=PaperMasterModel.objects.all())
    
    class Meta:
        model = StudentInternalTransModel
        fields = ['batchno', 'sem', 'course', 'examtype', 'studname', 'papername', 'marks']

    def clean(self):
        super(StudentInternalTansForm,self).clean()
        marks = self.cleaned_data.get('marks')

        if not re.match(r'^\d{1,3}$', str(marks)):
            self._errors['marks'] = self.error_class(['Maximun Marks =100.'])
        
        return self.cleaned_data

    