import pymysql as db
import matplotlib.pyplot as py

cnx = db.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='cars24',
                              charset='utf8')

print("Connected successfully")
cmd = cnx.cursor()
  
while True:
    print('1.Post ')
    print('2.Search')
    print('3.Update status')
    print('4.Delete details')
    print('5.Analysis')
    print('6.Exit')
    ch= int(input('Enter choice '))
    if ch == 1:
        vno = input('Enter vehicle number ')
        vno = vno.upper()
        owner = input('Enter owner ')
        mobile = input('Enter owner mobile ')
        model = input('Enter model ')
        price = input('Enter price ')
        company= input('Enter company ')
        company = company.upper()
        owncnt = input('Enter owners count ')
        kms = input('Enter kms ')
        fueltype = input('Enter fueltype ')
        fueltype = fueltype.upper()
        
        q = f"insert into car(vno,owner,mobile,model,    \
              price,company,status,owncnt,kms,fueltype) values \
              ('{vno}','{owner}','{mobile}',{model},   \
               {price},'{company}','N',{owncnt},  \
               {kms},'{fueltype}')"   
               
        cmd.execute(q)
        cnx.commit()
        
    elif ch == 2:
        print('Welcome to search option'.center(30))
        print('1. Search by model')
        print('2. Search by cost')
        print('3. Search by state')
        print('4. Search by company')
        print('5. Search by driven kms')
        print('6. Search by owners count')
        print('7. Fuel type ')
        sropt = int(input('Enter your search option '))
        if sropt == 1 :
            modelval = int(input('Enter model '))
            q = f"select * from car where status = 'N' and model = {modelval}"
            
        elif sropt == 2:
            cost1 = float(input('Enter cost '))
            cost2 = float (input('Enter cost '))
            q = f"select * from car where status = 'N' and price >= {cost1} and price <= {cost2}"
        
        elif sropt == 3:
            stateval = input('Enter state ')
            stateval = stateval.upper()
            q = f"select * from car where status = 'N' and vno like '{stateval}%'"
        
        elif sropt == 4:
            companyval = input('Enter state ')
            companyval = companyval.upper()
            q = f"select * from car where status = 'N' and company = '{companyval}'" 
            
        elif sropt == 5:
            kmsval = int(input('Enter kms '))
            q = f"select * from car where status = 'N' and kms <= {kmsval}"
            
        elif sropt == 6:
            ownercnt = int(input('Enter owners count '))
            q = f"select * from car where status = 'N' and owncnt = {ownercnt}"
        
        elif sropt == 7:
            fuelval = input('Enter fuel type ')
            fuelval = fuelval.upper()
            q = f"select * from car where status = 'N' and fueltype = '{fuelval}'"
        
        cmd.execute(q)
        for c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 in cmd:
            print('-' * 40)
            print('Vehicle number  :', c1)
            print('Vehicle owner   :', c2)
            print('Owner mobile    :', c3)
            print('Vehicle model   :', c4)
            print('Vehicle price   :', c5)
            print('Vehicle company :', c6)
            print('Owners count    :', c8)
            print('Kms driven      :', c9)
            print('Vehicle fueltype:', c10)
            print('-' * 40)
            
    elif ch == 3:
        vno = input('Enter vehicle number ')
        vno = vno.upper()
        q = f"update car set status = 'Y' where vno='{vno}'" 
        cmd.execute(q)
        cnx.commit()
        
    elif ch == 4:
        vno = input('Enter vehicle number ')
        vno = vno.upper()
        q = f"delete from car where vno='{vno}'" 
        cmd.execute(q)
        cnx.commit()
    
    elif ch == 5:
        
        q = "select company,count(*) from car where status = 'N' group by company"
        cmd.execute(q)
        
        x=[]
        y=[]
        for (c1,c2) in cmd:
            x.append(c1)
            y.append(c2)
            
        py.xlabel("Company")
        py.ylabel("Count")
        py.title("Cars on sale")
        py.bar(x,y)
        py.show()
    
    elif ch == 6:
        break
