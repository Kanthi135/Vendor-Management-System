from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
import os
from django.core.files.storage import FileSystemStorage
import pymysql


global uname

def ViewUser(request):
    if request.method == 'GET':
        output = '<table border=1 align=center width=100%>'
        font = '<font size="" color="black">'
        arr = ['Username','Password','Contact No','Gender','Email ID','Address','User Type']
        output += "<tr>"
        for i in range(len(arr)):
            output += "<th>"+font+arr[i]+"</th>"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'vendorapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM signup where usertype='User'")
            rows = cur.fetchall()
            for row in rows:
                username = row[0]
                password = row[1]
                contact = row[2]
                gender = row[3]
                email = row[4]
                address = row[5]
                utype = row[6]
                output += "<tr><td>"+font+str(username)+"</td>"
                output += "<td>"+font+password+"</td>"
                output += "<td>"+font+contact+"</td>"
                output += "<td>"+font+str(gender)+"</td>"
                output += "<td>"+font+str(email)+"</td>"
                output += "<td>"+font+str(address)+"</td>"
                output += "<td>"+font+str(utype)+"</td>"              
        context= {'data':output}        
        return render(request, 'ViewDetails.html', context)

def ViewFarmer(request):
    if request.method == 'GET':
        output = '<table border=1 align=center width=100%>'
        font = '<font size="" color="black">'
        arr = ['Username','Password','Contact No','Gender','Email ID','Address','User Type']
        output += "<tr>"
        for i in range(len(arr)):
            output += "<th>"+font+arr[i]+"</th>"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'vendorapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM signup where usertype='Farmer'")
            rows = cur.fetchall()
            for row in rows:
                username = row[0]
                password = row[1]
                contact = row[2]
                gender = row[3]
                email = row[4]
                address = row[5]
                utype = row[6]
                output += "<tr><td>"+font+str(username)+"</td>"
                output += "<td>"+font+password+"</td>"
                output += "<td>"+font+contact+"</td>"
                output += "<td>"+font+str(gender)+"</td>"
                output += "<td>"+font+str(email)+"</td>"
                output += "<td>"+font+str(address)+"</td>"
                output += "<td>"+font+str(utype)+"</td>"              
        context= {'data':output}        
        return render(request, 'ViewDetails.html', context)

def ViewFruits(request):
    if request.method == 'GET':
        output = '<table border=1 align=center width=100%>'
        font = '<font size="" color="black">'
        arr = ['Product ID','Vendor/Farmer Name','Product Name','Available Quantity','Price','Product Location','Product Image']
        output += "<tr>"
        for i in range(len(arr)):
            output += "<th>"+font+arr[i]+"</th>"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'vendorapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM cropinfo")
            rows = cur.fetchall()
            for row in rows:
                crop_id = row[0]
                farmer_name = row[1]
                crop = row[2]
                quantity = row[3]
                price = row[4]
                location = row[5]
                image = row[6]
                output += "<tr><td>"+font+str(crop_id)+"</td>"
                output += "<td>"+font+farmer_name+"</td>"
                output += "<td>"+font+crop+"</td>"
                output += "<td>"+font+str(quantity)+"</td>"
                output += "<td>"+font+str(price)+"</td>"
                output += "<td>"+font+str(location)+"</td>"
                output += '<td><img src="/static/files/'+image+'" height="100" width="100"/></td>'                
        context= {'data':output}        
        return render(request, 'ViewDetails.html', context)

def ViewFruitDetails(request):
    if request.method == 'GET':
        output = '<table border=1 align=center width=100%>'
        font = '<font size="" color="black">'
        arr = ['Product ID','Vendor/Farmer Name','Product Name','Available Quantity','Price','Product Location','Product Image']
        output += "<tr>"
        for i in range(len(arr)):
            output += "<th>"+font+arr[i]+"</th>"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'vendorapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM cropinfo")
            rows = cur.fetchall()
            for row in rows:
                crop_id = row[0]
                farmer_name = row[1]
                crop = row[2]
                quantity = row[3]
                price = row[4]
                location = row[5]
                image = row[6]
                output += "<tr><td>"+font+str(crop_id)+"</td>"
                output += "<td>"+font+farmer_name+"</td>"
                output += "<td>"+font+crop+"</td>"
                output += "<td>"+font+str(quantity)+"</td>"
                output += "<td>"+font+str(price)+"</td>"
                output += "<td>"+font+str(location)+"</td>"
                output += '<td><img src="/static/files/'+image+'" height="100" width="100"/></td>'                
        context= {'data':output}        
        return render(request, 'ViewFruitDetails.html', context)

def PriceUpdateAction(request):
    if request.method == 'POST':
        global uname
        cid = request.POST.get('t1', False)
        qty = request.POST.get('t2', False)
        price = request.POST.get('t3', False)
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'vendorapp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "update cropinfo set crop_quantity=crop_quantity+"+str(float(qty))+", crop_price="+str(float(price))+" where crop_id='"+cid+"'" 
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            output = "Product quantity or price updated"
        context= {'data':output}
        return render(request, 'FarmerScreen.html', context)
    

def PriceUpdateScreen(request):
    if request.method == 'GET':
        global uname
        cid = request.GET['t1']
        quantity = request.GET['t2']
        price = request.GET['t3']
        output = '<tr><td><font size="" color="black">Product&nbsp;Name</font></td><td><input type="text" name="t1" value="'+cid+'" size="30" readonly/></td></tr>'
        output += '<tr><td><font size="" color="black">New&nbsp;Quantity</font></td><td><input type="text" name="t2" value="0" size="30"/></td></tr>'
        output += '<tr><td><font size="" color="black">New&nbsp;Price</font></td><td><input type="text" name="t3" value="'+price+'" size="30"/></td></tr>'
        context= {'data':output}        
        return render(request, 'PriceUpdateScreen.html', context)

def UpdatePrice(request):
    if request.method == 'GET':
        global uname
        output = '<table border=1 align=center width=100%>'
        font = '<font size="" color="black">'
        arr = ['Product ID','Vendor/Farmer Name','Product Name','Available Quantity','Price','Product Location','Product Image','Update Details']
        output += "<tr>"
        for i in range(len(arr)):
            output += "<th>"+font+arr[i]+"</th>"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'vendorapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM cropinfo where farmer_name='"+uname+"'")
            rows = cur.fetchall()
            for row in rows:
                crop_id = row[0]
                farmer_name = row[1]
                crop = row[2]
                quantity = row[3]
                price = row[4]
                location = row[5]
                image = row[6]
                output += "<tr><td>"+font+str(crop_id)+"</td>"
                output += "<td>"+font+farmer_name+"</td>"
                output += "<td>"+font+crop+"</td>"
                output += "<td>"+font+str(quantity)+"</td>"
                output += "<td>"+font+str(price)+"</td>"
                output += "<td>"+font+str(location)+"</td>"
                output += '<td><img src="/static/files/'+image+'" height="100" width="100"/></td>'
                output += '<td><a href="PriceUpdateScreen?t1='+str(crop_id)+'&t2='+str(quantity)+'&t3='+str(price)+'">Click Here</a></td>'
        context= {'data':output}        
        return render(request, 'ViewPrices.html', context)


def AddDetailsAction(request):
    if request.method == 'POST':
        global uname
        cname = request.POST.get('t1', False)
        qty = request.POST.get('t2', False)
        price = request.POST.get('t3', False)
        desc = request.POST.get('t4', False)
        image = request.FILES['t5']
        imagename = request.FILES['t5'].name
        fs = FileSystemStorage()
        output = "Error in adding details"
        count = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'vendorapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select count(*) from cropinfo")
            rows = cur.fetchall()
            for row in rows:
                count = row[0]
        count = count + 1
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'vendorapp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO cropinfo(crop_id,farmer_name,crop_name,crop_quantity,crop_price,crop_location,crop_image) VALUES('"+str(count)+"','"+uname+"','"+cname+"','"+qty+"','"+price+"','"+desc+"','"+imagename+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            fs.save('VendorApp/static/files/'+imagename, image)
            output = cname+' details added in database wit ID '+str(count)
        context= {'data':output}
        return render(request, 'AddDetails.html', context)
        

def AddDetails(request):
    if request.method == 'GET':
       return render(request, 'AddDetails.html', {})

def UserLogin(request):
    if request.method == 'GET':
       return render(request, 'UserLogin.html', {})  

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def AdminLogin(request):
    if request.method == 'GET':
       return render(request, 'AdminLogin.html', {})

def FarmerLogin(request):
    if request.method == 'GET':
       return render(request, 'FarmerLogin.html', {})    

def Signup(request):
    if request.method == 'GET':
       return render(request, 'Signup.html', {})

def AdminLoginAction(request):
    global uname
    if request.method == 'POST':
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        if username == 'admin' and password == 'admin':
            uname = username
            context= {'data':'welcome '+username}
            return render(request, 'AdminScreen.html', context)
        else:
            context= {'data':'login failed'}
            return render(request, 'AdminLogin.html', context)
        
def FarmerLoginAction(request):
    global uname
    if request.method == 'POST':
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        index = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'vendorapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username,password,usertype FROM signup")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and password == row[1] and row[2] == 'Farmer':
                    uname = username
                    index = 1
                    break		
        if index == 1:
            context= {'data':'welcome '+uname}
            return render(request, 'FarmerScreen.html', context)
        else:
            context= {'data':'login failed'}
            return render(request, 'FarmerLogin.html', context)

def UserLoginAction(request):
    global uname
    if request.method == 'POST':
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        index = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'vendorapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username,password,usertype FROM signup")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and password == row[1] and row[2] == 'User':
                    uname = username
                    index = 1
                    break		
        if index == 1:
            context= {'data':'welcome '+uname}
            return render(request, 'UserScreen.html', context)
        else:
            context= {'data':'login failed'}
            return render(request, 'UserLogin.html', context)        

def SignupAction(request):
    if request.method == 'POST':
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        contact = request.POST.get('t3', False)
        gender = request.POST.get('t4', False)
        email = request.POST.get('t5', False)
        address = request.POST.get('t6', False)
        utype = request.POST.get('t7', False)
        output = "none"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'vendorapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username FROM signup")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username:
                    output = username+" Username already exists"
                    break
        if output == 'none':
            db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'vendorapp',charset='utf8')
            db_cursor = db_connection.cursor()
            student_sql_query = "INSERT INTO signup(username,password,contact_no,gender,email,address,usertype) VALUES('"+username+"','"+password+"','"+contact+"','"+gender+"','"+email+"','"+address+"','"+utype+"')"
            db_cursor.execute(student_sql_query)
            db_connection.commit()
            print(db_cursor.rowcount, "Record Inserted")
            if db_cursor.rowcount == 1:
                output = 'Signup Process Completed'
        context= {'data':output}
        return render(request, 'Signup.html', context)
      


