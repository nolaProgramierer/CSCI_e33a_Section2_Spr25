from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms


class AddPianoForm(forms.Form):
    brand = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Piano brand",
    })
    )
    finish = forms.CharField(
         widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Piano finish"
    })
    )
    price = forms.IntegerField(
         widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Piano price"
    })
    )


# Helper function to return a piano object from the session
def get_piano_from_session(request, brand, finish, price):
    pianos = request.session.get('pianos', [])
    
    # Iterate through each piano and return the first match
    for piano in pianos:
        if piano["brand"] == brand and piano["finish"] == finish and piano["price"] == price:
            return piano
        
    # If no match is found, return None
    return None


# Slightly more compact version using a generator

# def get_piano_from_session(request, brand, finish, price):
#     pianos = request.session.get('pianos', [])
    
#     return next((
#         piano for piano in pianos
#         if piano["brand"] == brand and piano["finish"] == finish and piano["price"] == price
#     ), None)
    

def index(request):
    # request.session.flush()
    # Return the piano object if in the session
    pianos = request.session.get('pianos', [])
    return render(request, "pianos/index.html", {"pianos": pianos})


def add_piano(request):
    form = AddPianoForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        # Get cleaned data from form
        new_piano = {
            "brand": form.cleaned_data["brand"],
            "finish": form.cleaned_data["finish"],
            "price": form.cleaned_data["price"]
        }
        
        # Return pianos object from the session if exists
        pianos = request.session.get('pianos', [])

        # Check if the piano already exists
        for piano in pianos:
            if piano == new_piano:
                form.add_error(None, "A piano with these attributes already exists.")
                return render(request, "pianos/add_piano.html", {"form": form})
        
        # Add the new piano to the list
        pianos.append(new_piano)
        # Replace 'pianos' session object
        request.session['pianos'] = pianos
        request.session.modified = True
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "pianos/add_piano.html", {"form": form})


# Another version using a generator object

# def add_piano(request):
#     form = AddPianoForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
        
#         new_piano = {
#             "brand": form.cleaned_data["brand"],
#             "finish": form.cleaned_data["finish"],
#             "price": form.cleaned_data["price"]
#         }
        
#         pianos = request.session.get('pianos', [])

#         if any(piano == new_piano for piano in pianos):
#             form.add_error(None, "A piano with these attributes already exists.")
#             return render(request, "pianos/add_piano.html", {"form": form})
        
#         pianos.append(new_piano)
#         request.session['pianos'] = pianos
#         request.session.modified = True
#         return HttpResponseRedirect(reverse("index"))
    
#     return render(request, "pianos/add_piano.html", {"form": form})


def piano_detail(request, brand, finish, price):
    piano = get_piano_from_session(request, brand, finish, price)
    return render(request, "pianos/piano_detail.html", {"piano": piano})

    
def edit_piano(request, brand, finish, price):
    piano_to_edit = get_piano_from_session(request, brand, finish, price)
    
    if not piano_to_edit:
        # Display a message if the piano is not found
        return render(request, "pianos/piano_not_found.html")

    form = AddPianoForm(request.POST or None, initial=piano_to_edit)
    
    if request.method == "POST" and form.is_valid():
        # Update the piano in the session
        updated_piano = {
            "brand": form.cleaned_data["brand"],
            "finish": form.cleaned_data["finish"],
            "price": form.cleaned_data["price"]
        }
        pianos = request.session.get('pianos', [])

        pianos = [updated_piano if piano == piano_to_edit else piano for piano in pianos]
        
        # The above is a list comprehension for the following logic
        # new_pianos = []
        # for piano in pianos:
        #     if piano == piano_to_edit:
        #         new_pianos.append(updated_piano)
        #     else:
        #         new_pianos.append(piano)

        request.session['pianos'] = pianos
        request.session.modified = True
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "pianos/edit_piano.html", {"form": form, "piano": piano_to_edit})


def confirm_remove_piano(request, brand, finish, price):
    # Retrieve sessions object
    pianos = request.session.get('pianos', [])
    # Retrieve piano
    for piano in pianos:
        if piano['brand'] == brand and piano['finish'] == finish and piano['price'] == price:
            piano_to_remove = piano
            break

    if piano_to_remove:
        return render(request, 'pianos/confirm_remove_piano.html', {'piano': piano_to_remove})

    # messages.error(request, "Piano not found.")
    return HttpResponseRedirect(reverse('index'))


# Using a generator object
# def confirm_remove_piano(request, brand, finish, price):
#     pianos = request.session.get('pianos', [])

#     piano_to_remove = next((
#         piano for piano in pianos
#         if piano['brand'] == brand and piano['finish'] == finish and piano['price'] == price 
#     ), None)
    
#     if piano_to_remove:
#         return render(request, 'pianos/confirm_remove_piano.html', {'piano': piano_to_remove})

#     return HttpResponseRedirect(reverse('index'))
    

def remove_piano(request, brand, finish, price):
    pianos = request.session.get('pianos', [])
    # Reformulate piano list without the piano passed to view
    new_pianos = [piano for piano in pianos 
                if not (piano['brand'] == brand 
                and piano['finish'] == finish 
                and piano['price'] == price)]
    # New sessions object
    request.session['pianos'] = new_pianos
    request.session.modified = True
    return HttpResponseRedirect(reverse('index'))

