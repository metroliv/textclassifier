from django import forms

class TextForm(forms.Form):
    PREDEFINED_TRANSACTIONS = [
        ('', '--- Select a predefined transaction ---'),
        ('Salary credited to your account', 'Salary credited to your account'),
        ('Credit card payment', 'Credit card payment'),
        ('Grocery shopping', 'Grocery shopping'),
        ('Rent payment', 'Rent payment'),
        ('Loan installment paid', 'Loan installment paid'),
        ('Freelance project payment', 'Freelance project payment'),
        # Add more predefined transactions as needed
    ]

    text = forms.CharField(widget=forms.Textarea, label='Enter transaction details', required=False)
    predefined_text = forms.ChoiceField(choices=PREDEFINED_TRANSACTIONS, required=False)
