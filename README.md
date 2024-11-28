# Ex.05 Design a Website for Server Side Processing
## Date:29/11/2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
<html>
<head>
<style>

.edge{
 display: ruby-base;
    margin-top: 400px;
    margin-bottom: auto;
    margin-left: auto;
    margin-right: auto;
    border-style: dotted;
    border-color: black;
   background-color: greenyellow;
    padding-top: 65px;
    padding-right: 80px;
    padding-bottom: 65px;
    padding-left: 80px;
    width: 40%;
    flex-direction: column;  
  }
  body{
    background-color: grey;
  }
div.formelt{
    font-size: 150%;
   color: black;   
}
div.box{
  color:rgb(13, 202, 226);
  text-align: center;
  font-style: inherit;  
}
input{
  padding: 10px;
  border: 3px solid;
  border-radius: 3px;
  width: 100%;
  align-items: center;
}
</style>
</head>
<body>
<div class="edge">
<div class="box">
 <h1>POWER OF A FILAMENT</h1>
<form method="POST">
{% csrf_token %}
</div>
<h1 align="center"> Jayagar.T (24901219)</h1>
<div class="formelt">
<br>
intensity<input type="text" name="intensity" value="{{i}}" ></input>(W/m <sup> 2 </sup>) <br>
</div>
<div class="formelt">
<br>
resistance <input type="text" name="resistance" value="{{r}}"></input>(ohm)<br>

</div>
                
<div  class="formelt">
<br>
<input type="submit" value="calculate"></input><br>
</div>
<div class="formelt">
<br>
power <input type="text" name="Power" value="{{power}}"></input>(w)<br>
</div>
 
</form>
</div>
</body>

</html>

views.py

from django.shortcuts import render 
def powerbulb(request): 
    context={} 
    context['power'] = "0" 
    context['I'] = "0" 
    context['R'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        I = request.POST.get('Intensity','0')
        R = request.POST.get('Resistance','0')
        print('request=',request) 
        print('Intensity=',I) 
        print('Resistance=',R) 
        power = (int(I) * int(I))*int(R)
        context['power'] = power 
        context['I'] = I
        context['R'] = R
        print('power=',power) 
    return render(request,'mathapp/math.html',context)

    urls.py

    from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powerlamp/',views.powerbulb,name="powerlamp"),
    path('',views.powerbulb,name="powerlamp")
]

```

## SERVER SIDE PROGRAMMING:
![alt text](<Screenshot 2024-11-28 131943.png>)



## HOMEPAGE:

![alt text](<Screenshot 2024-11-28 131924.png>)



## RESULT:
The program for performing server side processing is completed successfully.
