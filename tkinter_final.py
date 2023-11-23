import tkinter as tk
import mysql.connector
from tkinter import messagebox
import customtkinter


LARGE_FONT = ("Arial", 12)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Chet123$',
    'database': 'elective_management',
}
customtkinter.set_appearance_mode("dark")
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.geometry("800x600")
        
        self.frames = {}

        for F in (StartPage, AdminPage, StudentPage, FacultyPage, ClassroomsPage, CoursesPage, DepartmentsPage, StudentInsertPage, StudentUpdatePage, StudentDeletePage,StudentCGPAPage,StudentDetailsPage,TeacherNumberPage,Facutly_Location,Average_Class,TeacherDetailsPage, FacultyInsertPage, FacultyUpdatePage, FacultyDeletePage, CourseInsertPage, CourseUpdatePage, CourseDeletePage, ClassroomInsertPage, ClassroomUpdatePage, ClassroomDeletePage, DepartmentInsertPage, DepartmentUpdatePage, DepartmentDeletePage, TeacherPreferencesPage, TeacherPreferencesInsertPage, TeacherPreferencesDeletePage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="HI ADMIN", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        username_label = customtkinter.CTkLabel(self, text="Username",text_color="black",padx=5,pady=5)
        username_label.configure(text_color="black",padx=5,pady=5)  # Set text color to black
        username_label.pack()
        username_entry = customtkinter.CTkEntry(self)
        username_entry.pack()

        password_label = customtkinter.CTkLabel(self, text="Password")
        password_label.configure(text_color="black")  # Set text color to black
        password_label.pack()
        password_entry = customtkinter.CTkEntry(self, show="*")
        password_entry.pack()


        def login():
            username = username_entry.get()
            password = password_entry.get()

            # Establish a database connection
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Chet123$",
                database="elective_management"
            )
            cursor = conn.cursor()

            # Execute the query to retrieve the password for the provided username
            cursor.execute("SELECT password FROM login_details WHERE username = %s", (username,))
            result = cursor.fetchone()

            if result and result[0] == password:
                messagebox.showinfo("Login Successful", "You are logged in as admin.")
                controller.show_frame(AdminPage)
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

            cursor.close()
            conn.close()

        login_button = customtkinter.CTkButton(self, text="Login", command=login)
        login_button.place(relx=200, rely=200, anchor="center")
        login_button.pack()

class AdminPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Admin Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        student_button = customtkinter.CTkButton(self, text="Student", command=lambda: controller.show_frame(StudentPage))
        student_button.pack()

        faculty_button = customtkinter.CTkButton(self, text="Faculty", command=lambda: controller.show_frame(FacultyPage))
        faculty_button.pack()

        classrooms_button = customtkinter.CTkButton(self, text="Classrooms", command=lambda: controller.show_frame(ClassroomsPage))
        classrooms_button.pack()

        courses_button = customtkinter.CTkButton(self, text="Courses", command=lambda: controller.show_frame(CoursesPage))
        courses_button.pack()

        departments_button = customtkinter.CTkButton(self, text="Departments", command=lambda: controller.show_frame(DepartmentsPage))
        departments_button.pack()

        TeacherPreferences_button = customtkinter.CTkButton(self, text="Teacher Preferences", command=lambda: controller.show_frame(TeacherPreferencesPage))
        TeacherPreferences_button.pack()

        allotted_button = customtkinter.CTkButton(self, text="Allot Students", command=lambda: self.allottments())
        allotted_button.pack()



        logout_button = customtkinter.CTkButton(self, text="Logout", command=lambda: controller.show_frame(StartPage))
        logout_button.pack()
    def allottments(self):
        import allotted_logic
        messagebox.showinfo("Success","Allottment Successful")

class StudentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Student Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        insert_button = customtkinter.CTkButton(self, text="Insert Student", command=lambda: controller.show_frame(StudentInsertPage))
        insert_button.pack()

        update_button = customtkinter.CTkButton(self, text="Update Student", command=lambda: controller.show_frame(StudentUpdatePage))
        update_button.pack()

        delete_button = customtkinter.CTkButton(self, text="Delete Student", command=lambda: controller.show_frame(StudentDeletePage))
        delete_button.pack()

        cgpa_button=customtkinter.CTkButton(self, text="Student CGPA", command=lambda: controller.show_frame(StudentCGPAPage))
        cgpa_button.pack()

        details_button=customtkinter.CTkButton(self, text="Student Details", command=lambda: controller.show_frame(StudentDetailsPage))
        details_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Admin Page", command=lambda: controller.show_frame(AdminPage))
        back_button.pack()

class StudentInsertPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Insert Student", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for student attributes
        srn_label = tk.Label(self, text="SRN:")
        srn_label.pack()
        srn_entry = tk.Entry(self)
        srn_entry.pack()

        name_label = tk.Label(self, text="Student Name:")
        name_label.pack()
        name_entry = tk.Entry(self)
        name_entry.pack()

        dept_id_label = tk.Label(self, text="Dept ID:")
        dept_id_label.pack()
        dept_id_entry = tk.Entry(self)
        dept_id_entry.pack()

        section_label = tk.Label(self, text="Section:")
        section_label.pack()
        section_entry = tk.Entry(self)
        section_entry.pack()

        cgpa_label = tk.Label(self, text="CGPA:")
        cgpa_label.pack()
        cgpa_entry = tk.Entry(self)
        cgpa_entry.pack()

        email_label = tk.Label(self, text="Email ID:")
        email_label.pack()
        email_entry = tk.Entry(self)
        email_entry.pack()

        # Button to perform the insert operation
        insert_button = customtkinter.CTkButton(self, text="Insert Student", command=lambda: self.insert_student(srn_entry.get(), name_entry.get(), dept_id_entry.get(), section_entry.get(), cgpa_entry.get(), email_entry.get()))
        insert_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Student Page", command=lambda: controller.show_frame(StudentPage))
        back_button.pack()

    def insert_student(self, srn, name, dept_id, section, cgpa, email):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the INSERT query to insert a new student record
            insert_query = "INSERT INTO student (SRN, Student_name, Dept_id, Section, CGPA, email_id) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (srn, name, dept_id, section, cgpa, email)
            cursor.execute(insert_query, values)

            conn.commit()
            messagebox.showinfo("Insert Successful", "Record inserted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Insert Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class StudentUpdatePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Update Student", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for student attributes
        srn_label = tk.Label(self, text="SRN:")
        srn_label.pack()
        srn_entry = tk.Entry(self)
        srn_entry.pack()

        # Add input fields for the attributes to be updated
        cgpa_label = tk.Label(self, text="CGPA:")
        cgpa_label.pack()
        cgpa_entry = tk.Entry(self)
        cgpa_entry.pack()

        # Button to perform the update operation
        update_button = customtkinter.CTkButton(self, text="Update Student", command=lambda: self.update_student(srn_entry.get(),cgpa_entry.get()))
        update_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Student Page", command=lambda: controller.show_frame(StudentPage))
        back_button.pack()

    def update_student(self, srn, new_cgpa):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the UPDATE query to update student record
            update_query = "UPDATE student SET CGPA = %s WHERE SRN = %s"
            values = (new_cgpa, srn)
            cursor.execute(update_query, values)

            conn.commit()
            messagebox.showinfo("Update Successful", "Record updated successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Update Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class StudentDeletePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Delete Student", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for student attributes
        srn_label = tk.Label(self, text="SRN:")
        srn_label.pack()
        srn_entry = tk.Entry(self)
        srn_entry.pack()

        # Button to perform the delete operation
        delete_button = customtkinter.CTkButton(self, text="Delete Student", command=lambda: self.delete_student(srn_entry.get()))
        delete_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Student Page", command=lambda: controller.show_frame(StudentPage))
        back_button.pack()

    def delete_student(self, srn):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the DELETE query to delete a student record
            delete_query = "DELETE FROM student WHERE SRN = %s"
            values = (srn,)
            cursor.execute(delete_query, values)

            conn.commit()
            messagebox.showinfo("Delete Successful", "Record deleted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Delete Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class StudentCGPAPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Checking CGPA", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for student attributes
        lower_cgpa = tk.Label(self, text="Lower CGPA:")
        lower_cgpa.pack()
        lower_cgpa_entry = tk.Entry(self)
        lower_cgpa_entry.pack()

        higher_cgpa = tk.Label(self, text="Higher CGPA:")
        higher_cgpa.pack()
        higher_cgpa_entry = tk.Entry(self)
        higher_cgpa_entry.pack()

        # Button to perform the insert operation
        insert_button = customtkinter.CTkButton(self, text="Find Students", command=lambda: self.student_cgpa(lower_cgpa_entry.get(), higher_cgpa_entry.get()))
        insert_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Student Page", command=lambda: controller.show_frame(StudentPage))
        back_button.pack()

    def student_cgpa(self, lower, higher):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cgpa_query = "SELECT COUNT(*) AS student_count FROM student WHERE cgpa >= %s AND cgpa <= %s;"
            values =(float(lower),float(higher))
            cursor.execute(cgpa_query, values)
            result = cursor.fetchone()
            student_count = result[0]
            count_label = tk.Label(self, text=f"Number of students with CGPA between {lower} and {higher}: {student_count}")
            count_label.pack()

        except mysql.connector.Error as err:
            messagebox.showerror("Query Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()


class StudentDetailsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Student Details", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for student attributes
        srn = tk.Label(self, text="Enter SRN:")
        srn.pack()
        srn_entry = tk.Entry(self)
        srn_entry.pack()


        # Button to perform the insert operation
        insert_button = customtkinter.CTkButton(self, text="Find Student Details", command=lambda: self.student_details(srn_entry.get()))
        insert_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Student Page", command=lambda: controller.show_frame(StudentPage))
        back_button.pack()

    def student_details(self, srn):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            params = (srn,)
            cursor.callproc("GetStudentDetails", params)
            results=[]
            for result in cursor.stored_results():
                results.extend(result.fetchall())
            result_label = tk.Label(self, text=f"SRN, Elective ID, Course Name, Faculty Name, Room, Building, Floor, Type")
            result_label.pack()
            result_label1 = tk.Label(self, text=f"{results[0]}")
            result_label1.pack()
            result_label2 = tk.Label(self, text=f"{results[1]}")
            result_label2.pack()
                    

        except mysql.connector.Error as err:
            messagebox.showerror("Query Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()


class FacultyPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Faculty Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        insert_button = customtkinter.CTkButton(self, text="Insert Faculty", command=lambda: controller.show_frame(FacultyInsertPage))
        insert_button.pack()

        update_button = customtkinter.CTkButton(self, text="Update Faculty", command=lambda: controller.show_frame(FacultyUpdatePage))
        update_button.pack()

        delete_button = customtkinter.CTkButton(self, text="Delete Faculty", command=lambda: controller.show_frame(FacultyDeletePage))
        delete_button.pack()
        
        student_number=customtkinter.CTkButton(self, text="Number of Students", command=lambda: controller.show_frame(TeacherNumberPage))
        student_number.pack()

        faulty_allottment=customtkinter.CTkButton(self, text="Location of Faculty", command=lambda: controller.show_frame(Facutly_Location))
        faulty_allottment.pack()

        t_details=customtkinter.CTkButton(self, text="Teacher Details", command=lambda: controller.show_frame(TeacherDetailsPage))
        t_details.pack()
        
        back_button = customtkinter.CTkButton(self, text="Back to Admin Page", command=lambda: controller.show_frame(AdminPage))
        back_button.pack()

class FacultyInsertPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Insert faculty", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for faculty attributes
        faculty_id_label = tk.Label(self, text="Faculty ID:")
        faculty_id_label.pack()
        faculty_id_entry = tk.Entry(self)
        faculty_id_entry.pack()

        # Add input fields for the attributes to be inserted
        faculty_name_label = tk.Label(self, text="Faculty Name:")
        faculty_name_label.pack()
        faculty_name_entry = tk.Entry(self)
        faculty_name_entry.pack()

        dept_id_label = tk.Label(self, text="Department ID:")
        dept_id_label.pack()
        dept_id_entry = tk.Entry(self)
        dept_id_entry.pack()


        course_id_label = tk.Label(self, text="Course ID:")
        course_id_label.pack()
        course_id_entry = tk.Entry(self)
        course_id_entry.pack()

        experience_label = tk.Label(self, text="Experience:")
        experience_label.pack()
        experience_entry = tk.Entry(self)
        experience_entry.pack()


        # Button to perform the insert operation
        insert_button = customtkinter.CTkButton(self, text="Insert Faculty", command=lambda: self.insert_faculty(faculty_id_entry.get(), faculty_name_entry.get(), dept_id_entry.get(), course_id_entry.get(), experience_entry.get()))
        insert_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Faculty Page", command=lambda: controller.show_frame(FacultyPage))
        back_button.pack()

    def insert_faculty(self, faculty_id, faculty_name, dept_id, course_id, experience):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the INSERT query to insert a new faculty record
            insert_query = "INSERT INTO faculty VALUES (%s, %s, %s, %s, %s)"
            values = (faculty_id, faculty_name, dept_id, course_id, experience)
            cursor.execute(insert_query, values)

            conn.commit()
            messagebox.showinfo("Insert Successful", "Record inserted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Insert Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class FacultyUpdatePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Update Faculty", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for faculty attributes
        faculty_id_label = tk.Label(self, text="Faculty ID:")
        faculty_id_label.pack()
        faculty_id_entry = tk.Entry(self)
        faculty_id_entry.pack()

        experience_label = tk.Label(self, text="Experience:")
        experience_label.pack()
        experience_entry = tk.Entry(self)
        experience_entry.pack()
  
        # Button to perform the update operation
        update_button = customtkinter.CTkButton(self, text="Update Faculty", command=lambda: self.update_faculty(faculty_id_entry.get(),experience_entry.get()))
        update_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Faculty Page", command=lambda: controller.show_frame(FacultyPage))
        back_button.pack()

    def update_faculty(self, faculty_id,experience):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the UPDATE query to update faculty record
            update_query = "UPDATE faculty SET experience = %s WHERE faculty_id = %s"
            values = (experience, faculty_id)
            cursor.execute(update_query, values)

            conn.commit()
            messagebox.showinfo("Update Successful", "Record updated successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Update Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class FacultyDeletePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Delete Faculty", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for faculty attributes
        faculty_id_label = tk.Label(self, text="faculty id:")
        faculty_id_label.pack()
        faculty_id_entry = tk.Entry(self)
        faculty_id_entry.pack()

        # Button to perform the delete operation
        delete_button = customtkinter.CTkButton(self, text="Delete faculty", command=lambda: self.delete_faculty(faculty_id_entry.get()))
        delete_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to faculty Page", command=lambda: controller.show_frame(FacultyPage))
        back_button.pack()

    def delete_faculty(self, faculty_id):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the DELETE query to delete a faculty record
            delete_query = "DELETE FROM faculty WHERE faculty_id = %s"
            values = (faculty_id,)
            cursor.execute(delete_query, values)

            conn.commit()
            messagebox.showinfo("Delete Successful", "Record deleted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Delete Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class TeacherNumberPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Number of Students", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for student attributes
        facultyid = tk.Label(self, text="Enter Faculty ID:")
        facultyid.pack()
        fid_entry = tk.Entry(self)
        fid_entry.pack()


        # Button to perform the insert operation
        insert_button = customtkinter.CTkButton(self, text="Get Number of Students", command=lambda: self.student_number(fid_entry.get()))
        insert_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Faculty Page", command=lambda: controller.show_frame(FacultyPage))
        back_button.pack()

    def student_number(self, faculty):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.callproc("GetStudentDetails", (faculty,))

            # Fetch the result from the function
            result = cursor.fetchone()
            
            
            course_id = result[0]
            label = tk.Label(self, text="Number of Students being taught by {faculty} is {course_id}")
            label.pack(pady=10, padx=10)
        
        
        except mysql.connector.Error as err:
            messagebox.showerror("Query Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class Facutly_Location(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Location of Faculty", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for student attributes


        # Button to perform the insert operation
        insert_button = customtkinter.CTkButton(self, text="Get Faculty Allotments", command=lambda: self.faculty_al())
        insert_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Faculty Page", command=lambda: controller.show_frame(FacultyPage))
        back_button.pack()

    def faculty_al(self):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = "SELECT f.Faculty_id, f.Faculty_name, CASE WHEN a.count_srn > 60 THEN 'seminar hall' ELSE 'classroom' END AS Teaching_Location FROM faculty f JOIN ( SELECT faculty_id, COUNT(srn) AS count_srn FROM allotted_for GROUP BY faculty_id) a ON f.Faculty_id = a.faculty_id;"
            cursor.execute(query)
            results = cursor.fetchall()
            for result in results:
                count_label = tk.Label(self, text=f"{result}")
                count_label.pack()
        
        except mysql.connector.Error as err:
            messagebox.showerror("Query Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class TeacherDetailsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Teacher Details", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for student attributes
        fid = tk.Label(self, text="Enter FID:")
        fid.pack()
        fid_entry = tk.Entry(self)
        fid_entry.pack()


        # Button to perform the insert operation
        insert_button = customtkinter.CTkButton(self, text="Find Teacher Details", command=lambda: self.teacher_details(fid_entry.get()))
        insert_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Teachers Page", command=lambda: controller.show_frame(FacultyPage))
        back_button.pack()

    def teacher_details(self, fid):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            params = (fid,)
            cursor.callproc("GetTeacherDetails", params)
            result_label = tk.Label(self, text=f"SRN, Student Name, E_ID, Course Name, Faculty Name, Room Name, Building Name, Floor, Type")
            result_label.pack()
            results=[]
            for result in cursor.stored_results():
                results.extend(result.fetchall())
                
            for i in range(len(results)) :  
                result_label1 = tk.Label(self, text=f"{results[i]}")
                result_label1.pack()
            
           

        except mysql.connector.Error as err:
            messagebox.showerror("Query Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()



class ClassroomsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Classrooms Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        insert_button = customtkinter.CTkButton(self, text="Insert Classroom", command=lambda: controller.show_frame(ClassroomInsertPage))
        insert_button.pack()

        update_button = customtkinter.CTkButton(self, text="Update Classroom", command=lambda: controller.show_frame(ClassroomUpdatePage))
        update_button.pack()

        delete_button = customtkinter.CTkButton(self, text="Delete Classroom", command=lambda: controller.show_frame(ClassroomDeletePage))
        delete_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Admin Page", command=lambda: controller.show_frame(AdminPage))
        back_button.pack()

class ClassroomInsertPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Insert Classroom", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for Classroom attributes
        Class_id_label = tk.Label(self, text="Class ID:")
        Class_id_label.pack()
        Class_id_entry = tk.Entry(self)
        Class_id_entry.pack()

        room_name_label = tk.Label(self, text="Room Name:")
        room_name_label.pack()
        room_name_entry = tk.Entry(self)
        room_name_entry.pack()

        capacity_label = tk.Label(self, text="Capacity:")
        capacity_label.pack()
        capacity_entry = tk.Entry(self)
        capacity_entry.pack()

        class_no_label = tk.Label(self, text="Class No:")
        class_no_label.pack()
        class_no_entry = tk.Entry(self)
        class_no_entry.pack()

        building_name_label = tk.Label(self, text="Building Name:")
        building_name_label.pack()
        building_name_entry = tk.Entry(self)
        building_name_entry.pack()

        floor_no_label = tk.Label(self, text="Floor No:")
        floor_no_label.pack()
        floor_no_entry = tk.Entry(self)
        floor_no_entry.pack()

        class_type_label = tk.Label(self, text="Class Type:")
        class_type_label.pack()
        class_type_entry = tk.Entry(self)
        class_type_entry.pack()
  

        # Button to perform the insert operation
        insert_button = customtkinter.CTkButton(self, text="Insert Classroom", command=lambda: self.insert_Classroom(Class_id_entry.get(), room_name_entry.get(), capacity_entry.get(), class_no_entry.get(), building_name_entry.get(), floor_no_entry.get(), class_type_entry.get()))
        insert_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Classroom Page", command=lambda: controller.show_frame(ClassroomsPage))
        back_button.pack()

    def insert_Classroom(self, Class_id, room_name, capacity, class_no, building_name, floor_no, class_type):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the INSERT query to insert a new Classroom record
            insert_query = "INSERT INTO Classroom (Class_id, room_name, capacity, class_no, building_name, floor_no, class_type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (Class_id, room_name, capacity, class_no, building_name, floor_no, class_type)
            cursor.execute(insert_query, values)

            conn.commit()
            messagebox.showinfo("Insert Successful", "Record inserted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Insert Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class ClassroomUpdatePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Update Classroom", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for Classroom attributes
        Class_id_label = tk.Label(self, text="Classroom ID:")
        Class_id_label.pack()
        Class_id_entry = tk.Entry(self)
        Class_id_entry.pack()

        capacity_label = tk.Label(self, text="Capacity:")
        capacity_label.pack()
        capacity_entry = tk.Entry(self)
        capacity_entry.pack()

        # Button to perform the update operation
        update_button = customtkinter.CTkButton(self, text="Update Classroom", command=lambda: self.update_Classroom(Class_id_entry.get(), capacity_entry.get()))
        update_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Classroom Page", command=lambda: controller.show_frame(ClassroomsPage))
        back_button.pack()

    def update_Classroom(self, Class_id, capacity):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the UPDATE query to update Classroom record
            update_query = "UPDATE Classroom SET capacity = %s WHERE Class_id = %s"
            values = (capacity, Class_id)
            cursor.execute(update_query, values)

            conn.commit()
            messagebox.showinfo("Update Successful", "Record updated successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Update Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class ClassroomDeletePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Delete Classroom", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for Classroom attributes
        Class_id_label = tk.Label(self, text="Classroom id:")
        Class_id_label.pack()
        Class_id_entry = tk.Entry(self)
        Class_id_entry.pack()

        # Button to perform the delete operation
        delete_button = customtkinter.CTkButton(self, text="Delete Classroom", command=lambda: self.delete_Classroom(Class_id_entry.get()))
        delete_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Classroom Page", command=lambda: controller.show_frame(ClassroomsPage))
        back_button.pack()

    def delete_Classroom(self, Class_id):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the DELETE query to delete a Classroom record
            delete_query = "DELETE FROM Classroom WHERE Class_id = %s"
            values = (Class_id,)
            cursor.execute(delete_query, values)

            conn.commit()
            messagebox.showinfo("Delete Successful", "Record deleted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Delete Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()


class CoursesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Courses Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        insert_button = customtkinter.CTkButton(self, text="Insert Course", command=lambda: controller.show_frame(CourseInsertPage))
        insert_button.pack()

        update_button = customtkinter.CTkButton(self, text="Update Course", command=lambda: controller.show_frame(CourseUpdatePage))
        update_button.pack()

        delete_button = customtkinter.CTkButton(self, text="Delete Course", command=lambda: controller.show_frame(CourseDeletePage))
        delete_button.pack()
        
        averageclass = customtkinter.CTkButton(self, text="Most Popular Electives", command=lambda: controller.show_frame(Average_Class))
        averageclass.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Admin Page", command=lambda: controller.show_frame(AdminPage))
        back_button.pack()
class CourseInsertPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Insert Course", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for Course attributes
        Course_id_label = tk.Label(self, text="Course ID:")
        Course_id_label.pack()
        Course_id_entry = tk.Entry(self)
        Course_id_entry.pack()

        elective_id_label = tk.Label(self, text="Elective ID:")
        elective_id_label.pack()
        elective_id_entry = tk.Entry(self)
        elective_id_entry.pack()

        # Add input fields for the attributes to be inserted
        Course_name_label = tk.Label(self, text="Course Name:")
        Course_name_label.pack()
        Course_name_entry = tk.Entry(self)
        Course_name_entry.pack()

        credits_label = tk.Label(self, text="Credits:")
        credits_label.pack()
        credits_entry = tk.Entry(self)
        credits_entry.pack()

        anchorteacher_label = tk.Label(self, text="anchor Teacher:")
        anchorteacher_label.pack()
        anchorteacher_entry = tk.Entry(self)
        anchorteacher_entry.pack()

        dept_id_label = tk.Label(self, text="Department ID:")
        dept_id_label.pack()
        dept_id_entry = tk.Entry(self)
        dept_id_entry.pack()


        # Button to perform the insert operation
        insert_button = customtkinter.CTkButton(self, text="Insert Course", command=lambda: self.insert_Course(Course_id_entry.get(), Course_name_entry.get(), dept_id_entry.get(), elective_id_entry.get(), credits_entry.get(), anchorteacher_entry.get()))
        insert_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Course Page", command=lambda: controller.show_frame(CoursesPage))
        back_button.pack()

    def insert_Course(self, Course_id, Course_name, dept_id, elective_id, credits, anchorteacher):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the INSERT query to insert a new Course record
            insert_query = "INSERT INTO Course (Course_id, elec_id, Course_name, credits, anchorteacher, dept_id) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (Course_id, elective_id, Course_name, credits, anchorteacher, dept_id)
            cursor.execute(insert_query, values)

            conn.commit()
            messagebox.showinfo("Insert Successful", "Record inserted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Insert Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class CourseUpdatePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Update Course", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for Course attributes
        Course_id_label = tk.Label(self, text="Course ID:")
        Course_id_label.pack()
        Course_id_entry = tk.Entry(self)
        Course_id_entry.pack()

        anchorteacher_label = tk.Label(self, text="anchorteacher Teacher:")
        anchorteacher_label.pack()
        anchorteacher_entry = tk.Entry(self)
        anchorteacher_entry.pack()


        # Button to perform the update operation
        update_button = customtkinter.CTkButton(self, text="Update Course", command=lambda: self.update_Course(Course_id_entry.get(), anchorteacher_entry.get()))
        update_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Course Page", command=lambda: controller.show_frame(CoursesPage))
        back_button.pack()

    def update_Course(self, Course_id, anchorteacher):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the UPDATE query to update Course record
            update_query = "UPDATE Course SET anchorteacher = %s WHERE Course_id = %s"
            values = (anchorteacher, Course_id)
            cursor.execute(update_query, values)

            conn.commit()
            messagebox.showinfo("Update Successful", "Record updated successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Update Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class CourseDeletePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Delete Course", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for Course attributes
        Course_id_label = tk.Label(self, text="Course id:")
        Course_id_label.pack()
        Course_id_entry = tk.Entry(self)
        Course_id_entry.pack()

        # Button to perform the delete operation
        delete_button = customtkinter.CTkButton(self, text="Delete Course", command=lambda: self.delete_Course(Course_id_entry.get()))
        delete_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Course Page", command=lambda: controller.show_frame(CoursesPage))
        back_button.pack()

    def delete_Course(self, Course_id):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the DELETE query to delete a Course record
            delete_query = "DELETE FROM Course WHERE Course_id = %s"
            values = (Course_id,)
            cursor.execute(delete_query, values)

            conn.commit()
            messagebox.showinfo("Delete Successful", "Record deleted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Delete Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class Average_Class(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Popular Courses", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        insert_button = customtkinter.CTkButton(self, text="Get Electives", command=lambda: self.pop_courses())
        insert_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Courses Page", command=lambda: controller.show_frame(CoursesPage))
        back_button.pack()

    def pop_courses(self):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = "SELECT af.course_id, c.course_name, COUNT(*) AS student_count FROM allotted_for af,course c WHERE af.course_id=c.course_id GROUP BY af.course_id HAVING COUNT(*) > (SELECT AVG(student_count) FROM (SELECT course_id, COUNT(*) AS student_count FROM allotted_for GROUP BY course_id) AS avg_counts );"
            cursor.execute(query)
            results = cursor.fetchall()
            for result in results:
                count_label = tk.Label(self, text=f"{result}")
                count_label.pack()
        
        except mysql.connector.Error as err:
            messagebox.showerror("Query Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()


class DepartmentsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Departments Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        insert_button = customtkinter.CTkButton(self, text="Insert Department", command=lambda: controller.show_frame(DepartmentInsertPage))
        insert_button.pack()

        update_button = customtkinter.CTkButton(self, text="Update Department", command=lambda: controller.show_frame(DepartmentUpdatePage))
        update_button.pack()

        delete_button = customtkinter.CTkButton(self, text="Delete Department", command=lambda: controller.show_frame(DepartmentDeletePage))
        delete_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Admin Page", command=lambda: controller.show_frame(AdminPage))
        back_button.pack()

class DepartmentInsertPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Insert Department", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for Department attributes
        dept_id_label = tk.Label(self, text="Department ID:")
        dept_id_label.pack()
        dept_id_entry = tk.Entry(self)
        dept_id_entry.pack()

        dept_name_label = tk.Label(self, text="Department Name:")
        dept_name_label.pack()
        dept_name_entry = tk.Entry(self)
        dept_name_entry.pack()

        HOD_id_label = tk.Label(self, text="HOD ID:")
        HOD_id_label.pack()
        HOD_id_entry = tk.Entry(self)
        HOD_id_entry.pack()

        no_of_students_label = tk.Label(self, text="No. of Students:")
        no_of_students_label.pack()
        no_of_students_entry = tk.Entry(self)
        no_of_students_entry.pack()

        no_of_faculty_label = tk.Label(self, text="No. of Faculty:")
        no_of_faculty_label.pack()
        no_of_faculty_entry = tk.Entry(self)
        no_of_faculty_entry.pack()

  

        # Button to perform the insert operation
        insert_button = customtkinter.CTkButton(self, text="Insert Department", command=lambda: self.insert_Department(dept_id_entry.get(), dept_name_entry.get(), HOD_id_entry.get(), no_of_students_entry.get(), no_of_faculty_entry.get()))
        insert_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Department Page", command=lambda: controller.show_frame(DepartmentsPage))
        back_button.pack()

    def insert_Department(self, dept_id, dept_name, HOD_id, no_of_students, no_of_faculty):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the INSERT query to insert a new Department record
            insert_query = "INSERT INTO Department (dept_id, dept_name, HOD_id, no_of_students, no_of_faculty) VALUES (%s, %s, %s, %s, %s)"
            values = (dept_id, dept_name, HOD_id, no_of_students, no_of_faculty)
            cursor.execute(insert_query, values)

            conn.commit()
            messagebox.showinfo("Insert Successful", "Record inserted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Insert Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class DepartmentUpdatePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Update Department", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for Department attributes
        dept_id_label = tk.Label(self, text="Department ID:")
        dept_id_label.pack()
        dept_id_entry = tk.Entry(self)
        dept_id_entry.pack()

        HOD_id_label = tk.Label(self, text="HOD ID:")
        HOD_id_label.pack()
        HOD_id_entry = tk.Entry(self)
        HOD_id_entry.pack()

        no_of_students_label = tk.Label(self, text="No. of Students:")
        no_of_students_label.pack()
        no_of_students_entry = tk.Entry(self)
        no_of_students_entry.pack()

        no_of_faculty_label = tk.Label(self, text="No. of Faculty:")
        no_of_faculty_label.pack()
        no_of_faculty_entry = tk.Entry(self)
        no_of_faculty_entry.pack()


        # Button to perform the update operation
        update_button = customtkinter.CTkButton(self, text="Update Department", command=lambda: self.update_Department(dept_id_entry.get(), HOD_id_entry.get(), no_of_students_entry.get(), no_of_faculty_entry.get()))
        update_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Department Page", command=lambda: controller.show_frame(DepartmentsPage))
        back_button.pack()

    def update_Department(self, dept_id, HOD_id, no_of_students, no_of_faculty):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the UPDATE query to update Department record
            update_query = "UPDATE Department SET HOD_id = %s, no_of_students = %s, no_of_faculty = %s WHERE dept_id = %s"
            values = (HOD_id, no_of_students, no_of_faculty, dept_id)
            cursor.execute(update_query, values)

            conn.commit()
            messagebox.showinfo("Update Successful", "Record updated successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Update Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class DepartmentDeletePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Delete Department", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for Department attributes
        dept_id_label = tk.Label(self, text="Department ID:")
        dept_id_label.pack()
        dept_id_entry = tk.Entry(self)
        dept_id_entry.pack()


        # Button to perform the delete operation
        delete_button = customtkinter.CTkButton(self, text="Delete Department", command=lambda: self.delete_Department(dept_id_entry.get()))
        delete_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Department Page", command=lambda: controller.show_frame(DepartmentsPage))
        back_button.pack()

    def delete_Department(self, dept_id):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the DELETE query to delete a Department record
            delete_query = "DELETE FROM Department WHERE dept_id = %s"
            values = (dept_id,)
            cursor.execute(delete_query, values)

            conn.commit()
            messagebox.showinfo("Delete Successful", "Record deleted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Delete Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

class TeacherPreferencesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Teacher Preferences Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        insert_button = customtkinter.CTkButton(self, text="Insert Teacher Preferences", command=lambda: controller.show_frame(TeacherPreferencesInsertPage))
        insert_button.pack()

        delete_button = customtkinter.CTkButton(self, text="Delete Teacher Preferences", command=lambda: controller.show_frame(TeacherPreferencesDeletePage))
        delete_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to Admin Page", command=lambda: controller.show_frame(AdminPage))
        back_button.pack()

class TeacherPreferencesInsertPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Insert TeacherPreference", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for TeacherPreference attributes from chooses table

        SRN_label = tk.Label(self, text="SRN:")
        SRN_label.pack()
        SRN_entry = tk.Entry(self)
        SRN_entry.pack()

        course_id_label = tk.Label(self, text="Course ID:")
        course_id_label.pack()
        course_id_entry = tk.Entry(self)
        course_id_entry.pack()

        f1_label = tk.Label(self, text="Faculty 1:")
        f1_label.pack()
        f1_entry = tk.Entry(self)
        f1_entry.pack()

        f2_label = tk.Label(self, text="Faculty 2:")
        f2_label.pack()
        f2_entry = tk.Entry(self)
        f2_entry.pack()

        f3_label = tk.Label(self, text="Faculty 3:")
        f3_label.pack()
        f3_entry = tk.Entry(self)
        f3_entry.pack()

        f4_label = tk.Label(self, text="Faculty 4:")
        f4_label.pack()
        f4_entry = tk.Entry(self)
        f4_entry.pack()

        # Button to perform the insert operation
        insert_button = customtkinter.CTkButton(self, text="Insert TeacherPreference", command=lambda: self.insert_TeacherPreference(SRN_entry.get(), course_id_entry.get(), f1_entry.get(), f2_entry.get(), f3_entry.get(), f4_entry.get()))
        insert_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to TeacherPreference Page", command=lambda: controller.show_frame(TeacherPreferencesPage))
        back_button.pack()

    def insert_TeacherPreference(self, SRN, course_id, f1, f2, f3, f4):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the INSERT query to insert a new TeacherPreference record
            insert_query = "INSERT INTO chooses (SRN, course_id, f1, f2, f3, f4) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (SRN, course_id, f1, f2, f3, f4)
            cursor.execute(insert_query, values)

            conn.commit()
            messagebox.showinfo("Insert Successful", "Record inserted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Insert Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()


class TeacherPreferencesDeletePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Delete TeacherPreference", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Input fields for TeacherPreference attributes
        srn_label = tk.Label(self, text="SRN:")
        srn_label.pack()
        srn_entry = tk.Entry(self)
        srn_entry.pack()

        course_id_label = tk.Label(self, text="Course ID:")
        course_id_label.pack()
        course_id_entry = tk.Entry(self)
        course_id_entry.pack()
        # Button to perform the delete operation
        delete_button = customtkinter.CTkButton(self, text="Delete TeacherPreference", command=lambda: self.delete_TeacherPreference(srn_entry.get(), course_id_entry.get()))
        delete_button.pack()

        back_button = customtkinter.CTkButton(self, text="Back to TeacherPreference Page", command=lambda: controller.show_frame(TeacherPreferencesPage))
        back_button.pack()

    def delete_TeacherPreference(self, srn, course_id):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Execute the DELETE query to delete a TeacherPreference record
            delete_query = "DELETE FROM chooses WHERE srn = %s AND course_id = %s"
            values = (srn, course_id)
            cursor.execute(delete_query, values)
            
            conn.commit()
            messagebox.showinfo("Delete Successful", "Record deleted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Delete Failed", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

app = SeaofBTCapp()
app.mainloop()
