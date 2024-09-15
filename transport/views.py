from django.shortcuts import render, get_object_or_404, redirect
from .models import Bus, Student
from .forms import BusForm, StudentForm

# Display list of buses
def bus_list(request):
    buses = Bus.objects.all()
    return render(request, 'bus_list.html', {'buses': buses})

# Display detailed info about a specific bus
def bus_detail(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    students = Student.objects.filter(bus=bus);
    return render(request, 'bus_detail.html', {'bus': bus, 'students': students})

# Add a new bus
def add_bus(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bus_list')
    else:
        form = BusForm()
    return render(request, 'add_bus.html', {'form': form})

# Add a new student
def add_student(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bus_detail', pk=pk)
    else:
        form = StudentForm(initial={'bus': bus})
    return render(request, 'add_student.html', {'form': form, 'bus': bus})

# Update bus details
def update_bus(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    if request.method == 'POST':
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            return redirect('bus_detail', pk=pk)
    else:
        form = BusForm(instance=bus)
    return render(request, 'update_bus.html', {'form': form, 'bus': bus})

# Remove a bus
def delete_bus(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    if request.method == "POST":
        bus.delete()
        return redirect('bus_list')
    else: return render(request, 'remove_bus_confirm.html', {'bus':bus})
#Remove Student from a Bus
def remove_student(request, bus_id, student_id):
    bus = get_object_or_404(Bus, id=bus_id)
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        if student.bus_id == bus_id: 
            student.bus = None
            student.save()
            return redirect('bus_detail', pk=bus.id)  # Redirect back to bus details after removal
    else:
        return render(request, 'remove_student_confirm.html', {'bus': bus, 'student': student})