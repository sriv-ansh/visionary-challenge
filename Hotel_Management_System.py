import random
import json


print("-------------------------------------------------->>>>  Welcome To Sitara Hotel <<<<------------------------------------------------\n")
print('''@author - Ansh Srivastav\nDate :- 10/04/2023\n''')

class Hotel:
    def __init__(self) -> None:
        pass
    
    def add_items(self,Food_ID,food_json,Food_Name,Qty,Price,Total_Stock):
        Food_ID = random.randint(100,999)
        d = {"Food Id":Food_ID,"Food Name":Food_Name,"Quentity":Qty,"Price":Price,"Total Stock":Total_Stock}
        f = open(food_json,'r+')
        content = json.load(f)
        content.append(d)
        f.seek(0)
        f.truncate()
        json.dump(content,f)
        print("---------->>> Preview <<------------\n")
        print(f"""
Food ID          :                 {Food_ID} 
Food Name        :                 {Food_Name}
Quentity         :                 {Qty}
Price            :                 {Price}
Total Stock      :                 {Total_Stock}\n""")
        return "    🍔🥖🍕🧀🥐🍿  Food Added Sucessfully  🍔🥖🍕🧀🥐🍿"
    
    def View_all_item(self,Food_json):
        f = open(Food_json,"r+")
        content = json.load(f)
        for i in range(len(content)):
            print(f"--------------->>>> Your {i+1} Items is  <<<------------\n")
            print(f'''
Food ID          :                 {content[i]["Food Id"]} 
Food Name        :                 {content[i]["Food Name"]}
Quentity         :                 {content[i]["Quentity"]}
Price            :                 {content[i]["Price"]}
Total Stock      :                 {content[i]["Total Stock"]}\n
''')
        return ""
    

    def view_item_by_FoodID(self,Food_ID,Food_Json):
        f = open(Food_Json,"r+")        
        l = []
        d = 0
        content = json.load(f)
        for i in range(len(content)):
            if content[i]["Food Id"] == Food_ID:
                l.append(content[i])
                d = 1
        if d == 0:
            return False
        return l
    

    def update_item(self,Food_json,details_to_updated,Food_ID,updated_value):
        f = open(Food_json,"r+")        
        content = json.load(f)
        for i in range(len(content)):
            if content[i]["Food Id"] == Food_ID:
                content[i][details_to_updated] = updated_value
                f.seek(0)
                f.truncate()
                json.dump(content,f)
                return "    🌟🌟 Your Details Get Updated 🌟🌟   "
    
    def delete_items(self,Food_Json,Food_ID):
        f = open(Food_Json,"r+")        
        content = json.load(f)
        for i in range(len(content)):
            if content[i]["Food Id"] == Food_ID:
                del content[i]
                f.seek(0)
                f.truncate()
                json.dump(content,f)
                return "   ✔✔ Your Items Got Delete Sucessfully ✔✔ "
        else:
            return "      ❌❌ Enter A Valid ID ❌❌    "


    def Menu(self,Food_json):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~>>> Menu Card <<<~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        f = open(Food_json,"r+")
        content = json.load(f)
        for i in range(len(content)):
            print(f''' {content[i]['Food Id']}  {content[i]["Food Name"]}............................................... {content[i]["Price"]}.00 Rs.  
            ''')
        return ""
    
    def order(self,Food_json,Food_ID , QTY):
        f = open(Food_json,"r+")        
        l = []
        d = 0
        content = json.load(f)
        for i in range(len(content)):
            if content[i]["Food Id"] == Food_ID:
                l.append(content[i])
                d = 1
        if d == 0:
            return False
        return l

test = Hotel()

while True:
    print("~"*55)
    print(" 1. Add Items in Menu Card ")
    print(" 2. View Menu Card ")
    print(" 3. View Item ")
    print(" 4. Delete Item ")
    print(" 5  Update Item ")
    print(" 6. Order Item ")
    print(" 0. For Exit ")
    print("~"*55)
    choose = input("Plese Select Your Choose :")
    if choose == "1":
        print("--------------------->>>>> Add Food Domain <<<<---------------------\n")
        Food_Name = input(" Enter Food Name :")
        Qty = int(input(" Enter the Quentity :"))
        Price = int(input(" Enter the Price  :"))
        Total_Stock = int(input(" Enter the Total Stock For Food :"))
        print(test.add_items("","Food.json",Food_Name,Qty,Price,Total_Stock))
    if choose == "3":
        print("--------------------->>>>> View Food Domain <<<<---------------------\n")
        print("+="*25)
        print(" 1. View All Items ")
        print(" 2. View Items By ID ")
        print("+="*25)
        chc_id = input(" Enter Your Choise :")
        if chc_id == "1":
            print(test.View_all_item("Food.json"))
        if chc_id =="2":
            food_id = int(input('Enter Food Id Which You Want to See :'))
            details = test.view_item_by_FoodID(food_id,'Food.json')
            if details==False:
                print("  ❌❌ Invalid ID  ❌❌ ")
            else:
                print("-------->>>> Details Are <<<----")
                print(f'''
Food ID          :                 {details[0]["Food Id"]} 
Food Name        :                 {details[0]["Food Name"]}
Quentity         :                 {details[0]["Quentity"]}
Price            :                 {details[0]["Price"]}
Total Stock      :                 {details[0]["Total Stock"]}\n
''')

    if choose == '2':
        print(test.Menu("Food.json"))

    if choose == "4":
        print("--------------------->>>>> Delete Items  <<<<---------------------\n")
        Food_id= int(input("Enter Which ID You Want to Delete :"))
        print()
        print(test.delete_items("Food.json",Food_id))
    
    if choose == "5":
        print("--------------------->>>>> Update Items <<<<---------------------\n")
        Food_id = int(input("Enter Which Food Id you want to upated :"))
        field = input("Select a Filed Which You Wnat to be Updated :")
        update_details = input("Enter Your Updated Details :")
        print(test.update_item('Food.json',field,Food_id,update_details))
    
    if choose == "6":
        print("---------------->>>> Oder Domain <<<------------------------\n")
        print(test.Menu("Food.json"))
        Food_ID = int(input("Enter Food ID Which You Want to Order :"))
        Qut = int(input("Enter Who Much Quentity You Want :"))
        details = test.order('Food.json',Food_ID,Qut)
        if details == False:
            print("    ❌❌ Invalid Food ID ❌❌       ")
        else:
            for i in range(len(details)):
                print()
                print("            🌟🌟 Your Have Ordered Sucessfully   🌟🌟        \n   ")
                print("------->> Your Order is <<--------- ")
                print(f'''
Order ID              :       {details[i]["Food Id"]}
Order Food Name       :       {details[i]["Food Name"]}
Order Quentity        :       {Qut}  
                        \n''')
                print("         🍔🍔🍿Have It and Enjoy         🍔🍔🍿    ")
    if choose == "0":
        print("Thanks For Using Ba-bye ")
        break
            



