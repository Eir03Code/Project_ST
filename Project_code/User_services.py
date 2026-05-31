import json
from Users import User
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,HRFlowable,Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
import statistics
import matplotlib.pyplot as plt
import random
users=[]
q=[]
boldstyle=ParagraphStyle("bold")
def create_users():
    with open("users.json","r") as file: 
        json_users= json.load(file)

    for i in json_users:
        user= User(i["id"],i["email"],i["first_name"],i["last_name"],i["password"],i["flag"])
        users.append(user)

def check(email,password):
      for i in users:
        if i.email==email and i.password==password:
             global user_id ,name,lname
             user_id=i.user_id
             name=i.first_name
             lname=i.last_name
             return 1,i.flag
            
def check_if_answers():
    with open("user_answers.json","r",encoding="utf-8") as file: 
        data= json.load(file)
    global user_id
    for i in data:
        if data==[]:
            return 0
        if i["user_id"] == user_id:
             return 1
             



def load_questions():
    with open("garage_questions_improve.json","r",encoding="utf-8") as file: 
        return json.load(file)
  

def Submit_answers(answers,rating,description):
    with open("user_answers.json","r",encoding="utf-8") as file: 
        data= json.load(file)


    new_user_answers={ 
        
        
                "user_id":user_id,
                "answers":answers,
                "rating":rating  ,
                "description":description,
                "timestamp":datetime.now().isoformat()
                

             }
    
    data.append(new_user_answers)

    with open("user_answers.json","w",encoding="utf-8") as file: 
        json.dump(data,file,indent=4,ensure_ascii=False)


def customers_pdf():
        with open("user_answers.json","r",encoding="utf-8") as file: 
            data= json.load(file)
        with open("users.json","r",encoding="utf-8") as file: 
            data2= json.load(file)
        with open("garage_questions_improve.json","r",encoding="utf-8") as file: 
            data3= json.load(file)
        for l in data3["questions"]:
            q.append(l["question"])
        count=0 
        styles = getSampleStyleSheet()
        content=[]
        results=[]
        for i in data2:
            if i["flag"]=="C":
                count+=1 
                for j in data:
                    if i["id"]==j["user_id"]:
                        filename=f"{i["first_name"]}_{i["last_name"]}.pdf"
                        the_pdf=SimpleDocTemplate(f"{i["first_name"]}_{i["last_name"]}.pdf")
                        content.append(Paragraph("FEEDBACK CUSTOMER DATA",styles["Title"]))
                        content.append(HRFlowable(width="100%",thickness=2,color=colors.blue))
                        content.append(Spacer(1,12))
                        content.append(Paragraph(f"CUSTOMER ID : {j["user_id"]}",boldstyle))
                        content.append(Paragraph(f"NAME: {i["first_name"]}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LASTNAME: {i["last_name"]}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-MAIL: {i["email"]}",styles["Normal"]))
                        content.append(Spacer(1,20))
                        content.append(Paragraph("ΕΡΩΤΗΣΕΙΣ",boldstyle))
                        content.append(HRFlowable(width="100%",thickness=2,color=colors.blue))
                        content.append(Spacer(1,20))
                        content.append(Paragraph(f" 1 : {q[0]}",styles["Normal"]))
                        content.append(Paragraph(f"- {j["answers"][0]}",styles["Normal"]))
                        content.append(Spacer(1,10))
                        content.append(Paragraph(f" 2 : {q[1]}",styles["Normal"]))
                        content.append(Paragraph(f"- {j["answers"][1]} ",styles["Normal"]))
                        content.append(Spacer(1,10))
                        content.append(Paragraph(f" 3 : {q[2]}",styles["Normal"]))
                        content.append(Paragraph(f"- {j["answers"][2]}",styles["Normal"]))
                        content.append(Spacer(1,10))
                        content.append(Paragraph(f" 4 : {q[3]}",styles["Normal"]))
                        content.append(Paragraph(f"- {j["answers"][3]}",styles["Normal"]))
                        content.append(Spacer(1,20))
                        content.append(Paragraph("ΒΑΘΜΟΛΟΓΙΑ ΕΜΠΕΙΡΙΑΣ",boldstyle))
                        content.append(HRFlowable(width="100%",thickness=2,color=colors.blue))
                        content.append(Paragraph(f"RATING: {j["rating"]} ★",styles["Normal"]))
                        content.append(Spacer(1,20))
                        content.append(Paragraph("ΠΕΡΙΓΡΑΦΗ",boldstyle))
                        content.append(HRFlowable(width="100%",thickness=2,color=colors.blue))
                        content.append(Paragraph(f"{j["description"]}",styles["Normal"]))
                        content.append(Spacer(1,20))
                        content.append(Paragraph("ΗΜΕΡΟΜΗΝΙΑ",boldstyle))
                        content.append(HRFlowable(width="100%",thickness=2,color=colors.blue))
                        content.append(Paragraph(f" DATE/TIME OF SUBMITION :{j["timestamp"]}",styles["Normal"]))
                        the_pdf.build(content) 
                        results.append([f"{count} {i["first_name"]} {i["last_name"]}",filename])
        
        return results
                

def Metrics_pdf():
     with open("user_answers.json","r",encoding="utf-8") as file: 
            data= json.load(file)
     styles = getSampleStyleSheet()
     content=[]
     avg=statistics.mean(i["rating"]for i in data)
     avg=round(avg,2)
     
     median=statistics.median(i["rating"] for i in data)
     mode= statistics.mode(i["rating"] for i in data )
     range=max(i["rating"]for i in data)-min(i["rating"]for i in data)
     Highest_rating_number=sum(1 for i in data if i["rating"]==5)
     satisfied_costumers=sum(1 for i in data if i["rating"]>=4)
     percentage_of_satisfied=(satisfied_costumers/len(data))*100
     percentage_of_satisfied=round(percentage_of_satisfied,2)
     hist_dates=[  datetime.strptime(i["timestamp"],"%Y-%m-%dT%H:%M:%S.%f")for i in data  ]
     plt.hist(hist_dates,bins=5)
     plt.title("Customers submit Review date")
     plt.xlabel("Date")
     plt.ylabel("Number of Reviews")
     plt.xticks(rotation=45)
     plt.savefig("hist.png")
     plt.close()
     filename="Statistics.pdf"
     S_pdf=SimpleDocTemplate(filename)
     content.append(Paragraph("STATISTICS BASED ON CUSTOMERS",styles["Title"]))
     content.append(HRFlowable(width="100%",thickness=2,color=colors.green))
     content.append(Spacer(1,12))
     content.append(Paragraph(f"NUMBER OF CUSTOMERS WITH REVIEW : {len(data)}",boldstyle))
     content.append(HRFlowable(width="100%",thickness=2,color=colors.green))
     content.append(Spacer(1,12))
     content.append(Paragraph(f"RATING BASING STATISTICS",styles["Normal"]))
     content.append(HRFlowable(width="100%",thickness=2,color=colors.green))
     content.append(Spacer(1,12))
     content.append(Paragraph(f"AVERAGE: {avg}",boldstyle))
     content.append(Spacer(1,12))
     content.append(Paragraph(f"MEDIAN: {median}",boldstyle))
     content.append(Spacer(1,12))
     content.append(Paragraph(f"AVERAGE: {mode}",boldstyle))
     content.append(Spacer(1,12))
     content.append(Paragraph(f"RANGE: {range}",boldstyle))
     content.append(Spacer(1,20))
     content.append(Paragraph(f"RATING ADDITIONAL STATISTICS",styles["Normal"]))
     content.append(HRFlowable(width="100%",thickness=2,color=colors.green))
     content.append(Spacer(1,12))
     content.append(Paragraph(f"NUMBER OF HIGHEST RATED : {Highest_rating_number}",boldstyle))
     content.append(Spacer(1,12))
     content.append(Paragraph(f"SATISFIED COSTUMERS PERCENTAGE(>=4): {percentage_of_satisfied}",boldstyle))
     content.append(Spacer(1,20))
     content.append(HRFlowable(width="100%",thickness=2,color=colors.green))
     content.append(Spacer(1,20))
     content.append(Image("hist.png", width=300, height=200))
     S_pdf.build(content)
     return filename


def set_clock_in():
    with open("clock_in_user.json","r",encoding="utf-8") as file: 
        data= json.load(file)
   

    random_hour=random.randint(0,23)
    random_min=random.randint(0,59)
    random_sec=random.randint(0,59)
    mechanic_clock_in={ 
        
                "name":name,
                "last_name":lname,
                "user_id":user_id,
                "day":datetime.now().date().isoformat(),
                "time":f"{random_hour:02}:{random_min:02}:{random_sec:02}"

             }
    
    data.append(mechanic_clock_in)

    with open("clock_in_user.json","w",encoding="utf-8") as file: 
        json.dump(data,file,indent=4,ensure_ascii=False)



def Mechanic_clock_in():
    with open("clock_in_user.json","r",encoding="utf-8") as file: 
            data= json.load(file)
    result_clock_in=[]
    for i in data:
        result_clock_in.append([f" {i["name"]} {i["last_name"]} {i["user_id"]} {i["day"]} {i["time"]}"])

    return result_clock_in




    
