from django.shortcuts import render, redirect  # Add this import
from .forms import UserForm, PersonalInfoForm, MedicalInfoForm, BiometricDataForm

# Your view remains the same
def upload_data(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES)
        personal_info_form = PersonalInfoForm(request.POST)
        medical_info_form = MedicalInfoForm(request.POST, request.FILES)
        biometric_data_form = BiometricDataForm(request.POST, request.FILES)

        if (user_form.is_valid() and personal_info_form.is_valid() and
            medical_info_form.is_valid() and biometric_data_form.is_valid()):

            # Save User data
            user = user_form.save()

            # Save PersonalInfo data with the related User instance
            personal_info = personal_info_form.save(commit=False)
            personal_info.user = user
            personal_info.save()

            # Save MedicalInfo data with the related User instance
            medical_info = medical_info_form.save(commit=False)
            medical_info.user = user
            medical_info.save()

            # Save BiometricData data with the related User instance
            biometric_data = biometric_data_form.save(commit=False)
            biometric_data.user = user
            biometric_data.save()

            return redirect("upload_success")  # Replace with your success URL.

    else:
        user_form = UserForm()
        personal_info_form = PersonalInfoForm()
        medical_info_form = MedicalInfoForm()
        biometric_data_form = BiometricDataForm()

    return render(
        request,
        "ki/upload_data.html",
        {
            "user_form": user_form,
            "personal_info_form": personal_info_form,
            "medical_info_form": medical_info_form,
            "biometric_data_form": biometric_data_form,
        },
        
        
    )
    
    
