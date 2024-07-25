from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    
    return render(request, "header.html")


def introduction(request):
    return render(request, "introduction.html")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    # 如果是 POST 请求,获取用户提交的数据
    print(request.POST)
    username = request.POST.get("Inputusername")
    password = request.POST.get("InputPassword")
    if username == "123" and password == "123":
        return redirect("introduction") 
      
    #return HttpResponse("登录失败")
    return render(request, "login.html", {"error_msg": "用户名或密码错误"})

    
