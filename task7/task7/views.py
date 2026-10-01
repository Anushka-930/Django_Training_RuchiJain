from django.shortcuts import render


def operations(request):
    result = None
    error = None

    if request.method == "POST":
        try:
            first_number = float(request.POST.get("first_number", ""))
            second_number = float(request.POST.get("second_number", ""))
            operation = request.POST.get("operation")

            if operation == "add":
                result = first_number + second_number
            elif operation == "subtract":
                result = first_number - second_number
            elif operation == "multiply":
                result = first_number * second_number
            elif operation == "divide":
                if second_number == 0:
                    error = "Zero se divide nahi kar sakte."
                else:
                    result = first_number / second_number
        except (TypeError, ValueError):
            error = "Dono fields mein valid numbers enter karein."

    return render(request, "task7/operations.html", {"result": result, "error": error})