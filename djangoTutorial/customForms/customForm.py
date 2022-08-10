from django import forms


class TestForm(forms.Form):
    test_choices = (
        ("1", "first"),
        ("2", "second"),
        ("3", "third"),
    )
    test1 = forms.ChoiceField(choices=test_choices)
    test2 = forms.MultipleChoiceField(choices=test_choices, required=False, help_text='컨트롤 키를 누른 채로 선택하면 다중 선택이 가능합니다.')
    test3 = forms.CharField(initial='wow', widget=forms.HiddenInput())
    test4 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    field_order = ['test2', 'test4', 'test1']
