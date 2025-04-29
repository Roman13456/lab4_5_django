from django.shortcuts import render, get_object_or_404
from .models import Channel, Program 

def home(request):
    """Представлення для домашньої сторінки."""
    return render(request, 'tvguide/home.html')

def channel_list(request):
    """Представлення для списку телеканалів."""
    channels = Channel.objects.all().order_by('name')
    context = {
        'channels': channels
    }
    return render(request, 'tvguide/channel_list.html', context)

def channel_detail(request, pk): 
    """Представлення для детальної сторінки телеканалу."""
    channel = get_object_or_404(Channel, pk=pk) 
    channel_programs = Program.objects.filter(channel=channel).order_by('start_time')

    context = {
        'channel': channel,
        'programs': channel_programs,
    }
    return render(request, 'tvguide/channel_detail.html', context)

def program_list(request):
    """Представлення для списку всіх телепрограм."""
    all_programs = Program.objects.select_related('channel').order_by('start_time')
    context = {
        'programs': all_programs,
    }
    return render(request, 'tvguide/program_list.html', context)


# --- CRUD Views for Programs ---
from django.shortcuts import redirect 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required, user_passes_test 
from .forms import ProgramForm 

@user_passes_test(lambda u: u.is_staff) 
def program_create(request):
    """View to create a new program."""
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            program = form.save() 
            messages.success(request, f"Program '{program.title}' created successfully.")
            return redirect('program_list') # Redirect to the list after successful creation
    else:
        form = ProgramForm() # Display an empty form for GET request
    return render(request, 'tvguide/program_form.html', {'form': form, 'action': 'Create'})

@user_passes_test(lambda u: u.is_staff) 
def program_update(request, pk):
    """View to update an existing program."""
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            program = form.save() 
            messages.success(request, f"Program '{program.title}' updated successfully.")
            return redirect('program_list') # Redirect after successful update
    else:
        form = ProgramForm(instance=program) # Pre-populate form with existing data
    return render(request, 'tvguide/program_form.html', {'form': form, 'action': 'Update', 'program': program})

@user_passes_test(lambda u: u.is_staff) 
def program_delete(request, pk):
    """View to delete a program."""
    program = get_object_or_404(Program, pk=pk)
    program_title = program.title # Store title before deleting
    if request.method == 'POST':
        program.delete()
        messages.success(request, f"Program '{program_title}' deleted successfully.")
        return redirect('program_list') # Redirect after deletion
    # For GET request, show confirmation page
    return render(request, 'tvguide/program_confirm_delete.html', {'program': program})

# --- Registration View ---
from .forms import RegistrationForm
from django.urls import reverse_lazy 
from django.views import generic 

def register(request):
    """View to handle user registration."""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() # Creates the new user
            messages.success(request, 'Registration successful. Please log in.') # Add success message
            return redirect('login') # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# --- CRUD Views for Channels ---
from .forms import ChannelForm 

@user_passes_test(lambda u: u.is_staff)
def channel_create(request):
    """View to create a new channel."""
    if request.method == 'POST':
        form = ChannelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Channel '{form.cleaned_data['name']}' created successfully.")
            return redirect('channel_list') # Redirect to the list after successful creation
    else:
        form = ChannelForm() # Display an empty form for GET request
    return render(request, 'tvguide/channel_form.html', {'form': form, 'action': 'Create', 'model_name': 'Channel'})

@user_passes_test(lambda u: u.is_staff)
def channel_update(request, pk):
    """View to update an existing channel."""
    channel = get_object_or_404(Channel, pk=pk) # Get the channel 
    if request.method == 'POST':
        form = ChannelForm(request.POST, instance=channel) 
        if form.is_valid():
            form.save()
            messages.success(request, f"Channel '{channel.name}' updated successfully.")
            return redirect('channel_list') # Redirect after successful update
    else:
        form = ChannelForm(instance=channel) # Pre-populate form with existing data
    return render(request, 'tvguide/channel_form.html', {'form': form, 'action': 'Update', 'model_name': 'Channel', 'channel': channel})

@user_passes_test(lambda u: u.is_staff)
def channel_delete(request, pk):
    """View to delete a channel."""
    channel = get_object_or_404(Channel, pk=pk)
    channel_name = channel.name # Store name before deleting
    if request.method == 'POST':
        channel.delete()
        messages.success(request, f"Channel '{channel_name}' deleted successfully.")
        return redirect('channel_list') # Redirect after deletion
    # For GET request, show confirmation page
    return render(request, 'tvguide/channel_confirm_delete.html', {'object': channel, 'model_name': 'Channel'})
