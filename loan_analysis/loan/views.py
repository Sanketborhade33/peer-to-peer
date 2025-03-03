# from django.shortcuts import render
# import pandas as pd
# import numpy as np
# import joblib

# # Load trained model
# model = joblib.load("./loan_model.pkl")

# def home(request):
#     if request.method == "POST":
#         monthly_income = float(request.POST["monthly_income"])
#         existing_loans = int(request.POST["existing_loans"])
#         credit_score = float(request.POST["credit_score"])
#         loan_amount_requested = float(request.POST["loan_amount_requested"])
#         debt_to_income_ratio = float(request.POST["debt_to_income_ratio"])

#         # Create a DataFrame
#         user_data = pd.DataFrame([[monthly_income, existing_loans, credit_score, loan_amount_requested, debt_to_income_ratio]],
#                                  columns=['monthly_income', 'existing_loans', 'credit_score', 'loan_amount_requested', 'debt_to_income_ratio'])

#         # Predict risk
#         risk_prediction = model.predict(user_data)[0]
#         risk_status = "High Risk" if risk_prediction == 1 else "Low Risk"

#         return render(request, "loan/index.html", {"risk_status": risk_status})

#     return render(request, "loan/index.html")

# def user_login(request):  # Renamed function to avoid conflict
#     return render(request, "loan/login.html")






# ///////////////////////////////////////////////////////








from django.shortcuts import render
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("./loan_model.pkl")

def home(request):
    if request.method == "POST":
        monthly_income = float(request.POST["monthly_income"])
        existing_loans = int(request.POST["existing_loans"])
        credit_score = float(request.POST["credit_score"])
        loan_amount_requested = float(request.POST["loan_amount_requested"])
        debt_to_income_ratio = float(request.POST["debt_to_income_ratio"])

        # Create a DataFrame
        user_data = pd.DataFrame([[monthly_income, existing_loans, credit_score, loan_amount_requested, debt_to_income_ratio]],
                                 columns=['monthly_income', 'existing_loans', 'credit_score', 'loan_amount_requested', 'debt_to_income_ratio'])

        # Predict risk
        risk_prediction = model.predict(user_data)[0]
        risk_status = "High Risk" if risk_prediction == 1 else "Low Risk"

        return render(request, "loan/index.html", {"risk_status": risk_status})

    return render(request, "loan/index.html")

def user_login(request):  # Renamed function to avoid conflict
    return render(request, "loan/login.html")


from django.shortcuts import render, redirect
from .forms import LenderForm
from .models import Lender

def lender_registration(request):
    if request.method == "POST":
        form = LenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lender_list')  # Redirect to a lender list page after submission
    else:
        form = LenderForm()

    return render(request, 'loan/lender_registration.html', {'form': form})

def lender_list(request):
    lenders = Lender.objects.all()
    return render(request, 'loan/lender_list.html', {'lenders': lenders})





from django.shortcuts import render, redirect
from .forms import BorrowerForm
from .models import Borrower

def borrower_registration(request):
    if request.method == "POST":
        form = BorrowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrower_list')  # Redirect to a borrower list page after submission
    else:
        form = BorrowerForm()

    return render(request, 'loan/borrower_registration.html', {'form': form})


def borrower_list(request):
    borrowers = Borrower.objects.all()
    return render(request, 'loan/borrower_list.html', {'borrowers': borrowers})



# for chat

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import ChatMessage

User = get_user_model()

@login_required
def chat_room(request, receiver_id):
    receiver = User.objects.get(id=receiver_id)
    messages = ChatMessage.objects.filter(
        sender__in=[request.user, receiver],
        receiver__in=[request.user, receiver]
    ).order_by('timestamp')

    return render(request, 'loan/chat.html', {'receiver': receiver, 'messages': messages})





from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ChatMessage

@login_required
def borrower_list(request):
    borrowers = User.objects.filter(groups__name="Borrowers")  # Assuming Borrowers belong to a group
    return render(request, 'loan/borrower_list.html', {'borrowers': borrowers})
