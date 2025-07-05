# Insert cnsultant data by user.
name= input("نام مشاور:")
specialty= input("تخصص مntشاور:")

# Import cosultants list.
import json
with open("consultants.json","r",encoding="utf-8") as f:
    consultants=json.load(f)

# Create new cosultant with uniq ID
new_id= consultants[-1]["id"]+ 1 if consultants else 1
new_consultant = {
    "id": new_id,
    "name": name,
    "specialty": specialty
}
consultants.append(new_consultant)

# Saved new data in Json file
with open("consultants.json", "w", encoding= "utf-8") as f:
    json.dump(consultants,f,ensure_ascii=False,indent=2)
print("مشاور با موفقیت افزوده شد!")  
  