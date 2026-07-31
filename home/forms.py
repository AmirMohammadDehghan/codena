from django import forms
from .models import Course_Comment, Tickets
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Course_Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'cols': '30', 'rows': '10', 'id': 'massage'}),
        }


class TicketForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['title', 'course_ep', 'content']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'ticket_title_form', 'placeholder': 'عنوان تیکت جدید '}),
            'course_ep': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'ticket_course_ep_form', 'placeholder': 'قسمت مرتبط به این تیکت'}),
            'content': forms.Textarea(attrs={ 'placeholder': 'Enter content'}),
        }
