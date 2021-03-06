from django import forms
from inventory.models import Item, StudySessions, Course
#from django.core.exceptions improt ValidationError

class newReadingForm(forms.ModelForm): 
	title = forms.CharField(label='Name of Reading', help_text="Title of the reading", required=True)
	startPage = forms.IntegerField(label='Start Page', help_text="Start Page", required=True)
	endPage = forms.IntegerField(label='length', help_text="Number of pages", required=True)
	dueDate = forms.DateField(label="Due Date",help_text="Due Date", required=True)
	course = forms.CharField(widget=forms.HiddenInput(), initial="1")
	
	class Meta:
		model = Item
		fields = ('title','startPage', 'endPage', 'dueDate', 'course')
	

class newSessionForm(forms.ModelForm): 
	date = forms.DateField(label="Date Completed",help_text="date you did the study session", required=True)
	startPage = forms.IntegerField(label='Start Page', help_text="Start Page", required=True)
	pagesRead = forms.IntegerField(label='pagesRead', help_text="How many pages did you read?", required=True)
	timeSpent = forms.IntegerField(label='minutes spent reading', help_text="How many minutes did you spend reading?",required=True)
	
	class Meta:
		model = StudySessions
		fields = ('date','startPage', 'pagesRead', 'timeSpent')
		
		
	
