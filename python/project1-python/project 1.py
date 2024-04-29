import random
class student:
    def __init__(self):
        self.name = None
        self.id = None
        self.age = None
        self.grade = None
        self.generated_ids = set() # "set" Donot allow repete


    def addstudent(self,name,age, grade):
        self.name=name
        self.age=age
        self.grade=grade

        while True:
            # Generate a random ID
            self.id = random.randint(10000, 99999)
            if self.id not in self.generated_ids:
                # If the ID is unique, add it to the set and break the loop
                self.generated_ids.add(self.id)
                break


       # s = open("student.txt", "a")
               
        with open(r"C:\Users\DELL\Desktop\RAS\AI\project1-python/student.txt", "a") as s:
            s.write(f"Name: {self.name}, ID: {self.id}, Age: {self.age}, Grade: {self.grade}\n")
        s.close()

    def viewstudent(self):
         file_path = "C:/Users/DELL/Desktop/RAS/AI/project1-python/student.txt"
         with open(file_path, "r") as f: 
          print(f.read())   

    def search_student_by_id(self, student_id):
        file_path = "C:/Users/DELL/Desktop/RAS/AI/project1-python/student.txt"
        with open(file_path, "r") as f:

            for line in f:
                # Split the line into parts based on ","
                parts = line.split(",")
                if len(parts) >= 2:  # Check if the parts list has at least two elements..and not empaty line

                # Extract the ID from the parts
                    id_str = parts[1].split(":")[1].strip()
                    # Convert the ID to integer
                    id_int = int(id_str)
                    # Check if the ID matches the search query

                    if id_int == student_id:
                        print(parts)
                        return True  # Return the entire line
            print("Student not found")
            return False

                        

         

    def search_student_by_name(self, name):

        file_path = "C:/Users/DELL/Desktop/RAS/AI/project1-python/student.txt"
        with open(file_path, "r") as f:         
         for line in f:
                # Split the line into parts based on ","
                parts = line.split(",")
                if len(parts) >= 2:  # Check if the parts list has at least two elements..and not empaty line

                    # Extract the name from the parts
                    name_str = parts[0].split(":")[1].strip()
                    # Check if the name matches the search query
                    if name_str == name:
                        print(parts)
                        return True  # Return the entire line
        print( "Student not found")         
        return False

  
    def updatestudent(self, student_id, new_name, new_age, new_grade):

        if self.search_student_by_id(student_id) is False:
            return
        file_path = "C:/Users/DELL/Desktop/RAS/AI/project1-python/student.txt"
        with open(file_path, "r") as f:  
         for line in f:
            parts = line.split(", ")
            if len(parts) >= 2:  # Check if the parts list has at least two elements..and not empaty line
                id_str = parts[1].split(": ")[1].strip()
                id_int = int(id_str)
                if id_int == student_id:
                    # Split the student information into parts
                    parts = line.split(", ")
                    # Update the student's information if new values are provided

                    parts[0] = f"Name: {new_name}"
                    parts[2] = f"Age: {new_age}"
                    parts[3] = f"Grade: {new_grade}"
                    
                    # Join the parts to reconstruct the updated student information
                    updated_info = ", ".join(parts)

                    # Open the file and update the student information
                    with open(file_path, "r") as f:
                        lines = f.readlines()

                    with open(file_path, "w") as f:
                        for line in lines:
                            parts = line.split(", ")
                            id_str = parts[1].split(": ")[1].strip()
                            id_int = int(id_str)

                            if id_int == student_id:
                                line = updated_info + '\n'
                            f.write(line)

                    print("Student information updated successfully")
                    return

        


    def deletestudent(self, student_id):
        file_path = "C:/Users/DELL/Desktop/RAS/AI/project1-python/student.txt"
        try:
            # Open the file in read mode and read all lines into memory
            with open(file_path, "r") as f:
                lines = f.readlines()

            # Open the file again in write mode to overwrite it with updated information
            with open(file_path, "w") as f:
                student_found = False
                for line in lines:
                    parts = line.split(",")
                    if len(parts) >= 2:
                        id_str = parts[1].split(":")[1].strip()
                        try:
                            id_int = int(id_str)
                        except ValueError:
                            print("Invalid ID format in the file")
                            continue  # Skip processing this line

                        if id_int == student_id:
                            student_found = True
                            continue  # Skip writing this line to the file (effectively deleting it)
                        else:
                            f.write(line)  # Write the line to the file

                # Print a message if the student was not found
                if not student_found:
                    print("Student not found")
                else:
                    print("Student deleted successfully")

        except FileNotFoundError:
            print("File not found:", file_path)
        except Exception as e:
            print("An error occurred:", e)        
    
    

        

def mian():
    obj=student()

    while True:
        print("--------choose number----------")
        print("")
        print("1-Add Student")
        print("2-view all Students")
        print("3-search about student")
        print("4-updata student")
        print("5-delete student")
        print("6-exist")
        choose=int(input("choose number: "))

        if choose==1: 
         print("-------Add Student-------")
         name=input("Name: ") 
         age=input("Age: ")
         grade=input("Grade: ")
         obj.addstudent(name,age,grade)
         print("")

        elif choose ==2:
         print("--------viea all Students--------")
         obj.viewstudent()
         print("")


        elif choose==3:
                print("------search about student---------")
                print("")
                print("1-search about student by ID:")
                print("2-search about student by name:")
                print("")


                c=int(input("Your choose :"))

                if c==1:
                    id=input("ID: ")
                    print("")
                    obj.search_student_by_id(id)

                elif c==2: 
                    name=input("Name: ")
                    print("")
                    obj.search_student_by_name(name)
                print(" ")

        elif choose==4:
           print("--------updata student-----------")
           id=input("ID: ")
           newname=input("NEW name: ")
           newage=input("NEW age: ")
           newgrade=input("NEW grade: ")
           obj.updatestudent(id,newname,newage,newgrade)
           print("")


        elif choose==5:
            print("-----Delte student---------")
            ID=input("ID: ")
            obj.deletestudent(id)
            print("")


        elif choose==6:
            print("Bye Bye")
            break
        else :
            print("please Enter valied number")










mian()





         



