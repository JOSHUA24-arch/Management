from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request,"Home/index.html")



def plan(request):
    return render(request, 'Home/plan.html')




def calculate_pension(request):
    if request.method == 'POST':
        salary = float(request.POST['salary'])
        contribution_rate = float(request.POST['contribution_rate'])
        years_until_retirement = int(request.POST['years_until_retirement'])

        # Calculate the pension fund
        pension_fund = salary * (contribution_rate / 100) * years_until_retirement
        context = {
            'salary': salary,
            'contribution_rate':contribution_rate,
            'years_until_retirement':years_until_retirement,
            'pension_fund': pension_fund,
            
        }
        # Render the result
        return render(request, 'Partial/pension_result.html',context)

    return render(request, 'Home/plan.html')




