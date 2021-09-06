import json
import time
record ={100:{'Name':'Amul_Milk    1L','Category':'Dairy','Price':80,'Expire_Date':'10-09-2021','In_Stock':30},
         101:{'Name':'Amul_Paneer  500g','Category':'Dairy','Price':200,'Expire_Date':'1-09-2022','In_Stock':10},
         102:{'Name':'Amul_Cheese      ','Category':'Dairy','Price':30,'Expire_Date':'12-09-2021','In_Stock':10},
         103:{'Name':'Amul_Butter      ','Category':'Dairy','Price':50,'Expire_Date':'13-09-2021','In_Stock':12},
         104:{'Name':'Thumbs Up 1L     ','Category':'Drinks','Price':90,'Expire_Date':'10-09-2021','In_Stock':30},
         105:{'Name':'Thumbs Up  750ml ','Category':'Drinks','Price':50,'Expire_Date':'30-08-2023','In_Stock':30},
         106:{'Name':'Marie Gold  60g  ','Category':'Biscuit','Price':20,'Expire_Date':'1-12-2021','In_Stock':20},
         107:{'Name':'Good Day  60g    ','Category':'Biscuit','Price':20,'Expire_Date':'1-12-2021','In_Stock':20},
         108:{'Name':'Vita Marie Gold 60g','Category':'Biscuit','Price':20,'Expire_Date':'1-12-2021','In_Stock':20},
         109:{'Name':'Parle G  60g   ','Category':'Biscuit','Price':20,'Expire_Date':'1-12-2021','In_Stock':20},
         110:{'Name':'Bourbon  60g   ','Category':'Biscuit','Price':20,'Expire_Date':'11-12-2021','In_Stock':20},
         111:{'Name':'Crack Jack  60g','Category':'Biscuit','Price':20,'Expire_Date':'1-12-2021','In_Stock':20},
         112:{'Name':'Maggie          ','Category':'Noodles','Price':20,'Expire_Date':'10-12-2021','In_Stock':30},
         113:{'Name':'Top Ramen       ','Category':'Noodles','Price':20,'Expire_Date':'22-12-2021','In_Stock':30},
         114:{'Name':'Colgate  100g   ','Category':'ToothPaste','Price':54,'Expire_Date':'10-04-2022','In_Stock':15},
         115:{'Name':'dettol  75g     ','Category':'Soap','Price':40,'Expire_Date':'10-12-2021','In_Stock':20},
         116:{'Name':'Lux  75g        ','Category':'Soap','Price':40,'Expire_Date':'10-12-2021','In_Stock':20},
         117:{'Name':'5 star 20g      ','Category':'Chocolate','Price':20,'Expire_Date':'20-03-2022','In_Stock':20},118:{'Name':'Dairy Milk 20g  ','Category':'Chocolate','Price':20,'Expire_Date':'20-03-2022','In_Stock':20},119:{'Name':'KitKat 20g      ','Category':'Chocolate','Price':20,'Expire_Date':'21-04-2022','In_Stock':20},120:{'Name':'Kurkure         ','Category':'Snaks','Price':30,'Expire_Date':'10-04-2022','In_Stock':20},
         121:{'Name':'Lays            ','Category':'Snacks','Price':30,'Expire_Date':'20-04-2022','In_Stock':20},
         122:{'Name':'Chettos         ','Category':'Snacks','Price':30,'Expire_Date':'20-04-2022','In_Stock':20},
         123:{'Name':'NoteBook 200pages','Category':'stationary','Price':60,'Expire_Date':'NA       ','In_Stock':20},
         124:{'Name':'Cello Gripper pen','Category':'stationary','Price':8,'Expire_Date':'NA       ','In_Stock':20},
         125:{'Name':'Gatsby HairWax 100g ','Category':'Grooming','Price':200,'Expire_Date':'1-12-2023','In_Stock':10},
         126:{'Name':'Nevia FaceWash  ','Category':'Grooming','Price':200,'Expire_Date':'10-12-2023','In_Stock':20},
         127:{'Name':'Bread 100g      ','Category':'Bread','Price':40,'Expire_Date':'10-09-2021','In_Stock':20},
         128:{'Name':'Kissan JAM 250g ','Category':'Jam','Price':100,'Expire_Date':'10-05-2021','In_Stock':10},
         129:{'Name':'Tomato Ketchup  ','Category':'Ketchup','Price':40,'Expire_Date':'10-12-2021','In_Stock':20},
         130:{'Name':'Penaut Butter 1kg','Category':'Dairy','Price':500,'Expire_Date':'10-12-2021','In_Stock':10}}
# js = json.dumps(record)
# fd = open("records.json", 'w')
# fd.write(js)
# fd.close()

#------ log in as Admin | customer |  suppiler --------------#
print("**********************************LOG IN AS ************************************** \n")
print(" \t 1. Admin\t\t 2.Customer\t\t 3.Suppiler")
print("\t\tNOTE - *Please! Enter Number of Your Mode *")

#----------------------------------For ADMIN ------------------------------------#
login = input("Enter Mode  :")
if(login == '1'):
    passw = str(input("Enter Password : "))
    if(passw == '12345678'):
        #_________________________________________Adding Data to  records.json file ____________________________#
        rd= open("records.json",'r')
        r=rd.read()
        rd.close()
        record=json.loads(r)
        #print(record.keys())
        s= 1
        i=100
        print("__________________OUR INVENTORY ______________\n")
        print("\t Product_id \t\t Name \t\t  Price(Rs) \t\t Exipre_Date \t\t Stock \t\t Category")
        while(s<=len(record)):
                print("\t",i,'\t\t',record[str(i)]['Name'],'\t\t',record[str(i)]['Price'],'\t\t',record[str(i)]['Expire_Date'],'\t\t',record[str(i)]['In_Stock'],'\t\t',record[str(i)]['Category'])
                i=i+1
                s=s+1
        
        print("\t You Can Add or Update The Data...\n")
        p_id = input("Enter Product Id :")
        
        if(p_id not in record.keys()):
                print("\tYou Are Adding New Data With Id"+p_id)


                name = str(input("Enter Product Name :"))
                price = int(input("Price :"))
                Ex_date = str(input("Expire Date: "))
                istock = int(input("Enter Quantity:"))
                cat = str(input("Enter Category"))
                record[p_id] ={'Name': name, 'Price': price,'Expire_Date': Ex_date, 'In_Stock': istock,'Category':cat}
#------------------------------Dumping into records.json ----------------#
                js = json.dumps(record)
                fd=open('records.json','w')
                fd.write(js)
                fd.close()
                print("\tRECORD ADDED")
#--------------------------------------------------------------------------------------------#
        elif(p_id  in record.keys()):
                print("\tYou Are Updating Data of Product With ID"+p_id)
                iname = str(input("Enter Product Name :"))
                iprice = int(input("Price :"))
                iEx_date = str(input("Expire Date: "))
                iistock = int(input("Enter New Quantity:"))
                updated= record[p_id]['In_Stock']+iistock
                record[p_id].update({'In_Stock':updated})
                ircc= record[p_id]['In_Stock']
                icat = str(input("Enter Category")) 
                record[p_id] ={'Name': iname, 'Price': iprice,'Expire_Date': iEx_date,'In_Stock':updated,'Category':icat}
# #------------------------------Dumping into records.json ----------------#
                js = json.dumps(record)
                fd=open('records.json','w')
                fd.write(js)
                fd.close()
                print("\RECORD UPDATED")

#___________________________________________ For CUSTOMER _______________________________________________-#
elif(login == '2'):
    print("\t_____________________________________Welcome To SHREE KRISHNA Super Market___________________________\n ")
    fd = open("records.json", "r")
    r = fd.read()
    fd.close()
    data= json.loads(r)
    s= 1
    i=100
    print("\t Product_id \t\t Name \t\t  Price(Rs) \t\t Exipre_Date \t\t Stock \t\t Category")
    while(s<=len(data)):
        print("\t",i,'\t\t',data[str(i)]['Name'],'\t\t',data[str(i)]['Price'],'\t\t',data[str(i)]['Expire_Date'],'\t\t',data[str(i)]['In_Stock'],'\t\t',data[str(i)]['Category'])
        i=i+1
        s=s+1   
    id_prod  = str(input("\n\tEnter the product_Id: "))
    if(id_prod not in data.keys()):
            print("\tNo Such Time With These Id Enter Correct Id")
    
    ui_quant = int(input("\tEnter the quantity:"))
    if(ui_quant >data[id_prod]['In_Stock']):         
            print("\t SORRY ! Not Enough Quantity In Stock ")
    
    elif(ui_quant<=data[id_prod]['In_Stock'] or id_prod in data.keys()):
            
            u_name= input(("\tPlease Enter Your Name: "))
            print("\t\t\n******************************* BILL *******************************\t\t")
            print("\t\t Name:",u_name)
            print("\t\t Bill No:" ,str(len(data)),"\t\t\t","Time:",time.ctime())
            print("\t\t\tProduct Id :",id_prod)
            print("\t\t\tProduct: ",data[id_prod]['Name'])
            print("\t\t\tPrice: ",data[id_prod]['Price'])
            print("\t\t\tQuantity :",ui_quant)
            # print("\t\t\tTime:",time.ctime())
            amount=data[id_prod]['Price'] * (ui_quant)
            print("\t\t---------------------------------------------------------------------\n")
            print("\t\t\tBilling Amount: ", "'",amount,"Rs'", "-Only")
            print("\t\t---------------------------------------------------------------------\n")
            print("\t\t_____________THANK YOU VISIT AGIAN 😊  _______________")
            print("\n**********************************************************************\t\t")
            data[id_prod]['In_Stock']=data[id_prod]['In_Stock']-ui_quant
#----------------Updating records.json -------------------------------------#
            uf= json.dumps(data)
            fd=open('records.json','w')
            fd.write(uf)
            fd.close()

#____________________________________________________  for Sales.json file _______________________________________________#
        #     sales ={0000:{'Customer_Name':'Dummy','Item_Purchased':'Dummy','Quantity':'Dummy','Price':'Dummy','Total':'Dummy'}}
        #     js = json.dumps(sales)
        #     fd = open("sales.json", 'w')
        #     fd.write(js)
        #     fd.close()

            rd= open("sales.json",'r')
            s=rd.read()
            rd.close()
            sales=json.loads(s)
            sales[str(len(sales))]={'Customer_Name':u_name,'Item_Purchased':data[id_prod]['Name'],'Quantity':ui_quant,'Price':data[id_prod]['Price'],'Total':amount}
            sl= json.dumps(sales)
            sd= open('Sales.json','w')
            sd.write(sl)
            sd.close()
#------------------------------------------------------------------------------------------------#
    else:
            print("Enter Valid Information ")

# # _______________________________________ for  SUPPILER _____________________________#

elif(login=='3'):
        #_________________________________________Adding Data to  records.json file ____________________________#
        rd= open("records.json",'r')
        r=rd.read()
        rd.close()
        record=json.loads(r)
        print("__________________OUR INVENTORY ______________\n")
        s=1
        i=100
        print("\t Product_id \t\t Name \t\t  Price(Rs) \t\t Exipre_Date \t\t Stock \t\t Category")
        while(s<=len(record)):
                print("\t",i,'\t\t',record[str(i)]['Name'],'\t\t',record[str(i)]['Price'],'\t\t',record[str(i)]['Expire_Date'],'\t\t',record[str(i)]['In_Stock'],'\t\t',record[str(i)]['Category'])
                i=i+1
                s=s+1
        
        print("\t You Can Add or Update The Data...\n")
        
        p_id = input("Enter Product Id :")
        if(p_id not in record.keys()):
                print("\tYou Are Adding New Data With Id "+p_id)


                name = str(input("Enter Product Name :"))
                price = int(input("Price :"))
                Ex_date = str(input("Expire Date: "))
                istock = int(input("Enter Quantiy :"))
                cat = str(input("Enter Category"))
                record[p_id] ={'Name': name, 'Price': price,'Expire_Date': Ex_date, 'In_Stock': istock,'Category':cat}
#------------------------------Dumping into records.json ----------------#
                js = json.dumps(record)
                fd=open('records.json','w')
                fd.write(js)
                fd.close()
                print("\tRECORD ADDED")
#--------------------------------------------------------------------------------------------#
        elif(p_id  in record.keys()):
                print("\tYou Are Updating Data of Product With ID "+p_id)
                iname = str(input("Enter Product Name :"))
                iprice = int(input("Price :"))
                iEx_date = str(input("Expire Date: "))
                iistock = int(input("Enter Quantity :"))
                updated= record[p_id]['In_Stock']+iistock
                record[p_id].update({'In_Stock':updated})
                ircc= record[p_id]['In_Stock']
                icat = str(input("Enter Category")) 
                record[p_id] ={'Name': iname, 'Price': iprice,'Expire_Date': iEx_date,'In_Stock':updated,'Category':icat}
# #------------------------------Dumping into records.json ----------------#
                js = json.dumps(record)
                fd=open('records.json','w')
                fd.write(js)
                fd.close()
                print("\RECORD UPDATED")
else:
         print("Enter Correct Option")


# #-------------------- END --------------------------#
