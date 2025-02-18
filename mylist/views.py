from django.shortcuts import render
from .models import ShoppingItem
from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
def mylist(request):
    if request.method == "POST":
        print("Received data:", request.POST["itemName"])
        ShoppingItem.objects.create(name=request.POST["itemName"])

    all_items = ShoppingItem.objects.all()
    return render(request, "shopping_list.html", {"all_items": all_items})

def remove_item(request):
    if request.method == "POST":
        item_id = request.POST.get("itemId")
        ShoppingItem.objects.filter(id=item_id).delete()
        return JsonResponse({"success": True})
