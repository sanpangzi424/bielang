from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import LoginForm, RegisterForm, UserProfileForm, UserForm, UserInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserInfo, UserProfile

# Create your views here.

'''
判断请求方式，post进入到账号密码的合法性阶段，get直接展示表单提交页面。如果数据合法，进入到账号密码校验阶段，
正确，提示登录成功，错误，提示账号或密码错误。如果数据不合法，提示数据不合法。
'''


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('blog:blog_title'))
            else:
                return HttpResponse('sorry your username or password is not right')
        else:
            return HttpResponse('sorry Invalid login')
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'account/login.html', {'form': login_form})


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)

            return HttpResponse('register success!')

        else:
            return HttpResponse('register failed!')
    else:
        user_form = RegisterForm
        profile = UserProfileForm
        return render(request, 'account/register.html', {'form': user_form, 'profile': profile})


# user-info展示
@login_required(login_url='/account/login/')
def myself(request):
    user = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(user=user)
    user_info = UserInfo.objects.get(user=user)

    return render(request, 'account/myself.html', {'user': user, 'userinfo': user_info, 'userprofile': user_profile})


@login_required(login_url='/account/login/')
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(user=request.user)
    user_info = UserInfo.objects.get(user=request.user)

    #   如果是post请求 把所有的from实例化
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        user_info_form = UserInfoForm(request.POST)
        #   如果数据合法 就把接收的表单转换成字典形式的数据（cleaned_data属性）
        if user_form.is_valid() and user_profile_form.is_valid() and user_info_form.is_valid():
            user_cd = user_form.cleaned_data
            user_profile_cd = user_profile_form.cleaned_data
            user_info_cd = user_info_form.cleaned_data

            #   把用户post过来的值付给对应的字段，以备保存
            user.email = user_cd['email']
            user_profile.birth = user_profile_cd['birth']
            user_profile.phone = user_profile_cd['phone']
            user_info.school = user_info_cd['school']
            user_info.company = user_info_cd['company']
            user_info.profession = user_info_cd['profession']
            user_info.address = user_info_cd['address']
            user_info.aboutme = user_info_cd['aboutme']

            #   保存修改结果
            user.save()
            user_profile.save()
            user_info.save()
        # 如果数据不合法，则返回到个人信息页面
        return HttpResponseRedirect('/account/my-information/')

    # 如果是其他请求方式，则展示个人信息编辑页面
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={'birth': user_profile.birth, 'phone': user_profile.phone})
        userinfo_form = UserInfoForm(
            initial={'school': user_info.school, 'company': user_info.company, 'profession': user_info.profession,
                     'address': user_info.address, 'aboutme': user_info.aboutme})
        return render(request, 'account/myself_edit.html',
                      {'user_form': user_form, 'user_profile_form': userprofile_form, 'user_info_form': userinfo_form})
